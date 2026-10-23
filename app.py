import os
import math
import sqlite3
from urllib.parse import quote_plus
from flask import Flask, render_template, request, session, url_for, redirect

from data.seed_data import seed, AREAS, COORDS
from translations import (
    TRANSLATIONS,
    AREA_TRANSLATIONS,
    KIND_TRANSLATIONS,
    SORT_TRANSLATIONS,
    SERVICE_TYPE_TRANSLATIONS,
    DOSAGE_TRANSLATIONS,
    NEEDS_TRANSLATIONS,
    STATUS_REASONS_TRANSLATIONS,
)

app = Flask(__name__)
app.secret_key = 'liferoute-demo-key'
app.config['DATABASE'] = os.path.join(app.root_path, 'database.db')


def ensure_db():
    if not os.path.exists(app.config['DATABASE']):
        seed(app.config['DATABASE'])
        return
    c = sqlite3.connect(app.config['DATABASE'])
    ok = c.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='medicine_inventory'"
    ).fetchone()
    c.close()
    if not ok:
        seed(app.config['DATABASE'])


ensure_db()


def db():
    c = sqlite3.connect(app.config['DATABASE'])
    c.row_factory = sqlite3.Row
    return c


def maps_url(lat, lng, origin=None):
    origin = origin or ''
    return (
        'https://www.google.com/maps/dir/?api=1&origin='
        + quote_plus(origin)
        + '&destination='
        + quote_plus(f'{lat},{lng}')
        + '&travelmode=driving'
    )


def distance(area, lat, lng):
    a = COORDS.get(area, COORDS['Uttara'])
    return round(math.hypot((a[0] - lat) * 111, (a[1] - lng) * 102) * 1.08, 1)


class TranslationWrapper(dict):
    """Wrapper that enables both dictionary and attribute lookups with automatic fallback."""
    def __init__(self, lang, en_dict, target_dict):
        super().__init__(target_dict)
        self.lang = lang
        self.en_dict = en_dict
        self.target_dict = target_dict

    def __getattr__(self, key):
        if key in self.target_dict:
            return self.target_dict[key]
        if key in self.en_dict:
            return self.en_dict[key]
        return key

    def __getitem__(self, key):
        if key in self.target_dict:
            return self.target_dict[key]
        if key in self.en_dict:
            return self.en_dict[key]
        return key

    def get(self, key, default=None):
        if key in self.target_dict:
            return self.target_dict[key]
        if key in self.en_dict:
            return self.en_dict[key]
        return default if default is not None else key


@app.context_processor
def common():
    cur_lang = session.get('lang', 'en')
    if cur_lang not in TRANSLATIONS:
        cur_lang = 'en'
    t_obj = TranslationWrapper(cur_lang, TRANSLATIONS['en'], TRANSLATIONS[cur_lang])

    def t_area(name):
        return AREA_TRANSLATIONS.get(cur_lang, {}).get(name, name)

    def t_kind(kind):
        return KIND_TRANSLATIONS.get(cur_lang, {}).get(kind, kind)

    def t_sort(sort_val):
        return SORT_TRANSLATIONS.get(cur_lang, {}).get(sort_val, sort_val)

    def t_service_type(st):
        return SERVICE_TYPE_TRANSLATIONS.get(cur_lang, {}).get(st, st)

    def t_dosage(d):
        return DOSAGE_TRANSLATIONS.get(cur_lang, {}).get(d, d)

    def t_need(n):
        return NEEDS_TRANSLATIONS.get(cur_lang, {}).get(n, n)

    def t_num(n):
        if cur_lang != 'bn':
            return str(n)
        digits = {'0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'}
        return ''.join(digits.get(c, c) for c in str(n))

    def t_reason(r):
        if cur_lang == 'en':
            return r
        if 'blood is not currently listed as available' in r:
            blood_grp = r.split(' ')[0]
            return f'{blood_grp} রক্তের গ্রুপ বর্তমানে মজুত নেই'
        for en_phrase, bn_phrase in STATUS_REASONS_TRANSLATIONS['bn'].items():
            if en_phrase in r:
                return bn_phrase
        return r

    return {
        't': t_obj,
        'lang': cur_lang,
        'areas': AREAS,
        'maps_url': maps_url,
        't_area': t_area,
        't_kind': t_kind,
        't_sort': t_sort,
        't_service_type': t_service_type,
        't_dosage': t_dosage,
        't_need': t_need,
        't_num': t_num,
        't_reason': t_reason,
    }


@app.route('/language/<code>')
def language(code):
    session['lang'] = code if code in TRANSLATIONS else 'en'
    return redirect(request.referrer or url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/emergency')
def emergency():
    return render_template('emergency.html')


def care_for(f):
    s = f.get('situation', 'other')
    critical = f.get('conscious') == 'no' or f.get('breathing') == 'yes' or s in ('accident', 'burn')
    moderate = f.get('bleeding') == 'yes' or f.get('chest') == 'yes' or s in ('pregnancy', 'chest')
    needs = ['Emergency Care'] + (['ICU', 'Available Beds'] if critical else []) + (
        ['Required Blood'] if s in ('accident', 'bleeding') or f.get('bleeding') == 'yes' else []
    )
    return ('critical' if critical else 'moderate' if moderate else 'low'), needs


def matches(area, needs, blood=None):
    c = db()
    out = []
    for h in c.execute('SELECT * FROM hospitals').fetchall():
        h = dict(h)
        reasons = []
        ok = bool(h['emergency'])
        d = distance(area, h['lat'], h['lng'])
        if not ok:
            reasons.append('Emergency care is currently unavailable')
        if 'ICU' in needs and not h['icu']:
            ok = False
            reasons.append('ICU is currently unavailable')
        if 'Available Beds' in needs and h['beds'] < 1:
            ok = False
            reasons.append('No beds are currently listed as available')
        units = 0
        if blood:
            x = c.execute(
                'SELECT units FROM blood_inventory WHERE hospital_id=? AND blood_group=?',
                (h['id'], blood),
            ).fetchone()
            units = x['units'] if x else 0
            if units < 1:
                ok = False
                reasons.append(f'{blood} blood is not currently listed as available')
        h.update(
            units=units,
            suitable=ok,
            reasons=reasons,
            distance=d,
            score=(50 if h['emergency'] else 0)
            + (25 if h['icu'] else 0)
            + h['beds']
            + (15 if units else 0)
            - d * 0.8,
        )
        out.append(h)
    c.close()
    return sorted(out, key=lambda x: (not x['suitable'], -x['score'], x['distance']))


@app.route('/match', methods=['GET', 'POST'])
def match():
    if request.method == 'POST':
        level, needs = care_for(request.form)
        area = request.form.get('area', 'Uttara')
        blood = request.form.get('blood') or None
        results = matches(area, needs, blood)
        session['plan'] = {'level': level, 'needs': needs, 'area': area, 'blood': blood}
        best = next((x for x in results if x['suitable']), None)
        return render_template(
            'results.html',
            level=level,
            needs=needs,
            area=area,
            blood=blood,
            results=results,
            best=best,
        )
    # GET fallback allows language toggles and back-forward navigation
    plan = session.get('plan')
    if not plan:
        return redirect(url_for('emergency'))
    level = plan.get('level', 'critical')
    needs = plan.get('needs', ['Emergency Care'])
    area = plan.get('area', 'Uttara')
    blood = plan.get('blood')
    results = matches(area, needs, blood)
    best = next((x for x in results if x['suitable']), None)
    return render_template(
        'results.html',
        level=level,
        needs=needs,
        area=area,
        blood=blood,
        results=results,
        best=best,
    )


@app.route('/hospitals')
def hospitals():
    area = request.args.get('area', 'All Areas')
    kind = request.args.get('type', 'All')
    term = request.args.get('q', '').strip()
    sort = request.args.get('sort', 'Best Match')
    c = db()
    q = 'SELECT * FROM hospitals WHERE 1=1'
    p = []
    if area != 'All Areas':
        q += ' AND area=?'
        p.append(area)
    if kind != 'All':
        q += ' AND kind=?'
        p.append(kind)
    if term:
        q += ' AND (name LIKE ? OR area LIKE ?)'
        p += ['%' + term + '%', '%' + term + '%']
    rows = [dict(x) for x in c.execute(q, p)]
    c.close()
    for x in rows:
        x['distance'] = distance(area if area != 'All Areas' else 'Uttara', x['lat'], x['lng'])
    sort_keys = {
        'Nearest Suitable': lambda x: (not x['emergency'], x['distance']),
        'Most Beds Available': lambda x: -x['beds'],
        'Best Match': lambda x: -(x['emergency'] * 30 + x['icu'] * 20 + x['beds']),
    }
    key = sort_keys.get(sort, sort_keys['Best Match'])
    rows.sort(key=key)
    return render_template('hospitals.html', hospitals=rows, selected=(area, kind, sort, term))


@app.route('/ambulance')
def ambulance():
    area = request.args.get('area', 'Uttara')
    sort = request.args.get('sort', 'Nearest')
    c = db()
    rows = [dict(x) for x in c.execute('SELECT * FROM ambulances')]
    c.close()
    for x in rows:
        x['distance'] = distance(area, x['lat'], x['lng'])
    sort_keys = {
        'Nearest': lambda x: (not x['availability_status'], x['distance']),
        'Available Now': lambda x: (not x['availability_status'], x['distance']),
        'Area': lambda x: (x['area'] != area, not x['availability_status'], x['distance']),
    }
    key = sort_keys.get(sort, sort_keys['Nearest'])
    rows.sort(key=key)
    nearest = next((x for x in rows if x['availability_status']), None)
    return render_template(
        'ambulance.html',
        services=rows,
        area=area,
        sort=sort,
        nearest=nearest,
    )


@app.route('/blood')
def blood():
    group = request.args.get('group', '').strip()
    area = request.args.get('area', 'All Areas')
    rows = []
    donors = []
    if group:
        c = db()
        q = (
            'SELECT h.name,h.area,h.phone,h.lat,h.lng,b.units '
            'FROM blood_inventory b JOIN hospitals h ON h.id=b.hospital_id '
            'WHERE b.blood_group=? AND b.units>0'
        )
        p = [group]
        if area != 'All Areas':
            q += ' AND h.area=?'
            p.append(area)
        rows = [dict(x) for x in c.execute(q, p).fetchall()]
        for x in rows:
            x['distance'] = distance(area if area != 'All Areas' else 'Uttara', x['lat'], x['lng'])
        rows.sort(key=lambda x: -x['units'])

        q = 'SELECT * FROM donors WHERE blood_group=?'
        p = [group]
        if area != 'All Areas':
            q += ' AND area=?'
            p.append(area)
        donors = [dict(x) for x in c.execute(q, p).fetchall()]
        c.close()
    return render_template('blood.html', group=group, area=area, rows=rows, donors=donors)


@app.route('/pharmacy')
def pharmacy():
    term = request.args.get('q', '').strip()
    area = request.args.get('area', 'All Areas')
    rows = []
    nearby = []
    if term:
        c = db()
        base = (
            'SELECT p.name, p.area, p.address, p.phone, p.lat, p.lng, '
            'i.medicine_name, i.generic_name, i.brand_name, i.strength, i.dosage_form, i.stock_quantity '
            'FROM medicine_inventory i JOIN pharmacies p ON p.id=i.pharmacy_id '
            'WHERE i.availability=1 AND ('
            'lower(i.medicine_name)=lower(?) OR lower(i.brand_name)=lower(?) OR lower(i.generic_name)=lower(?) '
            'OR lower(i.medicine_name) LIKE lower(?) OR lower(i.brand_name) LIKE lower(?) OR lower(i.generic_name) LIKE lower(?)'
            ')'
        )
        args = [term, term, term, '%' + term + '%', '%' + term + '%', '%' + term + '%']
        order = (
            ' ORDER BY CASE WHEN lower(i.medicine_name)=lower(?) OR lower(i.brand_name)=lower(?) OR lower(i.generic_name)=lower(?) '
            'THEN 0 ELSE 1 END, i.stock_quantity DESC'
        )
        args += [term, term, term]
        if area != 'All Areas':
            rows = [dict(x) for x in c.execute(base + ' AND p.area=?' + order, args[:6] + [area] + args[6:]).fetchall()]
            if not rows:
                nearby = [dict(x) for x in c.execute(base + order, args).fetchall()]
        else:
            rows = [dict(x) for x in c.execute(base + order, args).fetchall()]
        c.close()
    return render_template('pharmacy.html', rows=rows, nearby=nearby, term=term, area=area)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/share')
def share():
    plan = session.get('plan')
    if not plan:
        return redirect(url_for('emergency'))
    best = next((x for x in matches(plan['area'], plan['needs'], plan.get('blood')) if x['suitable']), None)
    return render_template('share.html', plan=plan, best=best)


if __name__ == '__main__':
    app.run(debug=True)
