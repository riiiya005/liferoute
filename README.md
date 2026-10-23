# LifeRoute

Humanitarian emergency-healthcare prototype built with Flask, SQLite, Jinja, vanilla JavaScript, Leaflet, and OpenStreetMap. All capacity, blood, pharmacy, and contact records are fictional demonstration data.

## Run

Use Python 3.12+:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`. The SQLite database is created and seeded automatically on first startup.

## Test

```powershell
python -m unittest discover -s tests -v
```

The test suite covers emergency severity/care derivation, database-driven Hospital B → Hospital C failover, nearest ambulance ordering, medicine search, and Google Maps URL creation.

To demonstrate failover manually, use an Uttara accident search with O+ blood (Hospital B is the initial match), then run `UPDATE hospitals SET icu=0 WHERE id=2` in SQLite and search again; Hospital C becomes the best suitable match. Google Maps route links hand off navigation to Google Maps; LifeRoute does not claim live traffic or availability.
