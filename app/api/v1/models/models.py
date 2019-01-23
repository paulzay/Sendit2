from flask import jsonify, make_response, request
destinations = ['Nairobi', 'Nakuru', 'Mombasa', 'Kisimu', 'Kisii', 'Thika', 'Meru']
pickup_locations = ['Nairobi', 'Nakuru', 'Mombasa', 'Kisimu', 'Kisii', 'Thika', 'Meru']
from ....security.utils import valid_name, valid_destination, valid_pickup_location
parcels = []


class ParcelModel():
    def __init__(self):
        self.db = parcels

    def create_order(self, sender_name ,sender_email, pickup_location, destination, weight, quantity,
                     order_status='Pending Dispatch'):

        payload = {
            "parcel_id": len(parcels)+1,
            "sender_name": sender_name,
            "pickup_location": pickup_location,
            "destination": destination,
            "weight": weight,
            "quantity": quantity,
            "order_status": order_status,
            "sender_email": sender_email
        }
        if any(input == "" for input in (sender_name, sender_email, pickup_location, destination, weight, quantity)):
            return {"message" : "fields cannot be empty"}
        
        elif destination not in destinations: 
            return "invalid destination"
        
        elif pickup_location not in pickup_locations:
            return "please select one of our locations"
        
        elif weight <= 0:
            return  "invalid weight"

        elif quantity <= 0:
            return "invalid amount"

        if not valid_name(sender_name):
            return make_response(jsonify(
                {
                    "Message": "Invalid sender name"
                }), 200)

        elif not valid_destination(destination):
            return make_response(jsonify({
                "Message": "Invalid destination"
            }), 200)

        elif not valid_pickup_location(pickup_location):
            return make_response(jsonify(
                {
                    'Message': "Invalid pickup location"
                }), 200)

        elif type(quantity) != int:
            return make_response(jsonify(
                {
                    'Message': "Invalid quantity"
                }), 200)

        elif type(weight) != int:
            return make_response(jsonify(
                {
                    'Message': "Invalid weight"
                }), 200)
        
        parcels.append(payload)
        return parcels, 201

    def get_all_orders(self):
        """Return all orders"""
        return self.db, 200

    def get_specific_order(self, parcel_id):
        """Return a specific order"""
        parcel = [parcel for parcel in parcels if parcel["parcel_id"]==parcel_id]
        if parcel:
                return make_response(jsonify({
                        "Status": "OK",
                        "message": "Success", 
                        "Order": parcel 
                       }), 200)

    def get_orders_by_specific_user(self, sender_email):
        """Return all orders by a specific user"""
        my_orders = []
        parcel = [parcel for parcel in parcels if parcel["sender_email"]==sender_email]
        if parcel:
                my_orders.append(parcel)
        if my_orders:
            return make_response(jsonify({
                    "message": "my orders", "User Orders": my_orders
                }), 200)

    def cancel_order(self, parcel_id):
        """Cancel an order"""
        parcel = [parcel for parcel in parcels if parcel["parcel_id"] == parcel_id]
        if parcel:
            parcel[0]["order_status"] = request.json["order_status"]
            if parcel[0]["order_status"] == "Cancelled":
                return "order has been cancelled"
            parcel[0]["order_status"] = "Cancelled"
            return "order has been cancelled"

class Homey():
    def index(self):
        return "welcome home", 200