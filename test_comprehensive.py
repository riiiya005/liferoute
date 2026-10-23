"""
Comprehensive End-to-End Test Suite for LifeRoute
Tests all pages, forms, language switching (English and Bangla), filters, and flows.
"""

import unittest
import sqlite3
import tempfile
import os
from app import app, care_for, matches, maps_url
from data.seed_data import seed

class ComprehensiveLifeRouteTests(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False)
        self.db_file.close()
        seed(self.db_file.name)
        app.config.update(TESTING=True, DATABASE=self.db_file.name, SECRET_KEY='test-key')
        self.client = app.test_client()

    def tearDown(self):
        if os.path.exists(self.db_file.name):
            os.unlink(self.db_file.name)

    def test_all_pages_render_english_and_bangla(self):
        routes = [
            '/',
            '/emergency',
            '/hospitals',
            '/ambulance',
            '/blood',
            '/pharmacy',
            '/about',
        ]
        
        # Test English
        self.client.get('/language/en')
        for r in routes:
            resp = self.client.get(r)
            self.assertEqual(resp.status_code, 200, f"Failed on English {r}")
            self.assertIn(b'LifeRoute', resp.data)
            self.assertIn(b'Every Minute Matters', resp.data)

        # Test Bangla
        self.client.get('/language/bn')
        for r in routes:
            resp = self.client.get(r)
            self.assertEqual(resp.status_code, 200, f"Failed on Bangla {r}")
            self.assertIn('প্রতিটি মিনিট গুরুত্বপূর্ণ'.encode('utf-8'), resp.data)

    def test_emergency_triage_flow_and_share(self):
        # 1. Post to match
        resp = self.client.post('/match', data={
            'situation': 'accident',
            'area': 'Uttara',
            'conscious': 'yes',
            'breathing': 'yes',
            'bleeding': 'yes',
            'chest': 'no',
            'blood': 'O+'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Hospital B', resp.data)
        self.assertIn(b'BEST MATCH', resp.data)
        self.assertIn(b'id="map"', resp.data)

        # 2. Test GET on /match (refresh / language switch while on results)
        resp_get = self.client.get('/match')
        self.assertEqual(resp_get.status_code, 200)
        self.assertIn(b'Hospital B', resp_get.data)

        # 3. Test language switch on results page
        self.client.get('/language/bn')
        resp_bn = self.client.get('/match')
        self.assertEqual(resp_bn.status_code, 200)
        self.assertIn('সেরা মিল'.encode('utf-8'), resp_bn.data)

        # 4. Visit share page
        resp_share = self.client.get('/share')
        self.assertEqual(resp_share.status_code, 200)
        self.assertIn('Hospital B'.encode('utf-8'), resp_share.data)
        self.assertIn('জরুরি'.encode('utf-8'), resp_share.data)

        # 5. Share page in English
        self.client.get('/language/en')
        resp_share_en = self.client.get('/share')
        self.assertEqual(resp_share_en.status_code, 200)
        self.assertIn(b'LIFEROUTE EMERGENCY PLAN', resp_share_en.data)

    def test_hospital_directory_filters(self):
        # Filter by area and sort
        resp = self.client.get('/hospitals?q=Care&area=Uttara&type=Private&sort=Nearest+Suitable')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Care', resp.data)

        # Filter empty result
        resp_empty = self.client.get('/hospitals?q=NonExistentHospital')
        self.assertEqual(resp_empty.status_code, 200)
        self.assertIn(b'No hospitals found', resp_empty.data)

    def test_ambulance_directory(self):
        resp = self.client.get('/ambulance?area=Mirpur&sort=Available+Now')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Rapid Response', resp.data)
        self.assertIn(b'NEAREST AVAILABLE', resp.data)

    def test_blood_support_search(self):
        resp = self.client.get('/blood?group=A%2B&area=Uttara')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Hospital Blood Banks', resp.data)
        self.assertIn(b'Community Volunteer Donors', resp.data)

    def test_pharmacy_medicine_search(self):
        # Found
        resp = self.client.get('/pharmacy?q=Napa&area=Uttara')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Napa', resp.data)
        self.assertIn(b'Paracetamol', resp.data)

        # Generic search
        resp_gen = self.client.get('/pharmacy?q=Omeprazole&area=All+Areas')
        self.assertEqual(resp_gen.status_code, 200)
        self.assertIn(b'Seclo', resp_gen.data)

        # Not found in specific area with nearby fallback
        resp_nearby = self.client.get('/pharmacy?q=Ventolin&area=Old+Dhaka')
        self.assertEqual(resp_nearby.status_code, 200)

if __name__ == '__main__':
    unittest.main()
