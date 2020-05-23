import unittest
import json
from app import create_app


class TestParcels(unittest.TestCase):
    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context() 
        self.data = [{
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": 10,
            "quantity": 2,
            "order_status": "transit",
            "parcel_id": 1,
            "sender_email": "paul@gmail.com"
            
        },
        {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": 10,
            "quantity": 2,
            "parcel_id": 2,
            "order_status": "transit",
            "sender_email": "paul@gmail.com"
        }]

    def test_get_all_parcels(self):
        response = self.client.get('/api/v1/parcels', data=json.dumps(self.data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 500)

    def test_get_single_parcel(self):
        response = self.client.get("/api/v1/parcels/1", data=json.dumps(self.data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_non_existent_order(self):
        response = self.client.get("/api/v1/parcels/3", content_type="application/json")
        self.assertNotEqual(response.status_code, 404)

    def test_cancel_parcel(self):
        self.data = {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": "10kg",
            "quantity": "2",
            "parcel_id": 1,
            "order_status": "Cancelled",
            "sender_email": "paul@gmail.com"
        }
        response = self.client.put('/api/v1/parcels/1', data=json.dumps(self.data),
                                   content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_invalid_sender_name(self):
        self.data = {
            "sender_name": "",
            "pickup_location": "Nairobi",
            "destination": "Kisii",
            "weight": "10kg",
            "quantity": "2",
            "parcel_id": 1,
            "sender_email": "paul@gmail.com"
        }
        response = self.client.post(
            "/api/v1/parcel",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(response.status_code, 500)

    def test_invalid_pickup_point(self):
        self.data = {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "$^&%",
            "weight": "10kg",
            "quantity": "2",
            "parcel_id": 1,
            "order_status": "Transit",
            "sender_email": "paul@gmail.com"
        }
        response = self.client.post(
            "/api/v1/parcel",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_destination(self):
        self.data = {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": "10kg",
            "quantity": "2",
            "parcel_id": 1,
            "order_status": "Transit",
            "sender_email": "paul@gmail.com"
        }

        response = self.client.post(
            "/api/v1/parcel",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_quantity(self):
        self.data = {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": "10kg",
            "quantity": "thate fyve",
            "parcel_id": 1,
            "order_status": "Transit",
            "sender_email": "paul@gmail.com"
        }
        response = self.client.post(
            "/api/v1/parcel",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_weight(self):
        self.data = {
            "sender_name": "paul zay",
            "pickup_location": "nairobi",
            "destination": "lamu",
            "weight": "(&^(&",
            "quantity": "2",
            "parcel_id": 1,
            "order_status": "Cancelled",
            "sender_email": "paul@gmail.com"
        }

        response = self.client.post(
            "/api/v1/parcel",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)
