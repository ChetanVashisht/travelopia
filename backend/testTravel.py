import requests
import unittest
from operator import getitem

class testInsert(unittest.TestCase):
    def testAppIsUp(self):
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def testInsert(self):
        req = {
            "name": "namus",
            "email": "4namus@fff.com",
            "destination": "Europe",
            "travellerCount": "201",
            "budget": "2200"
        }
        response = requests.post('http://localhost:8000/travellers/', json=req)
        self.assertIsNotNone(response.json()["id"])

    def testGetTraveller(self):
        req = {
            "name": "namus",
            "email": "4namus@fff.com",
            "destination": "Europe",
            "travellerCount": "201",
            "budget": "2200"
        }
        response = requests.post('http://localhost:8000/travellers/', json=req)
        id = response.json()["id"]
        self.assertIsNotNone(id)

        resp = requests.get(f'http://localhost:8000/travellers/{id}')
        self.assertEqual(resp.json()['name'], req['name'])

    def testGetAllTravellers(self):
        response = requests.get('http://localhost:8000/travellers/')
        self.assertIsInstance(response.json(), list)

    def testDeleteTraveller(self):
        req = {
            "name": "namus",
            "email": "4namus@fff.com",
            "destination": "Europe",
            "travellerCount": "201",
            "budget": "2200"
        }
        response = requests.post('http://localhost:8000/travellers/', json=req)
        id = response.json()["id"]
        self.assertIsNotNone(id)

        resp = requests.get(f'http://localhost:8000/travellers/{id}')
        self.assertEqual(resp.json()['name'], req['name'])

        resp = requests.delete(f'http://localhost:8000/travellers/{id}')
        resp = requests.get(f'http://localhost:8000/travellers/{id}')
        self.assertRaises(KeyError, getitem, resp.json(), 'id')

if __name__ == "__main__":
    unittest.main()
