from flask import request
from flask_restful import Resource
from ..models.models import ParcelModel
destinations = ['Nairobi', 'Nakuru', 'Mombasa', 'Kisimu', 'Kisii', 'Thika', 'Meru']
pickup_locations = ['Nairobi', 'Nakuru', 'Mombasa', 'Kisimu', 'Kisii', 'Thika', 'Meru']


class PostParcel(Resource, ParcelModel):
    def __init__(self):
        self.db = ParcelModel()
        
    def post(self):
        data = request.get_json()
        sender_name = data["sender_name"]
        pickup_location = data["pickup_location"]
        quantity = data["quantity"]
        weight = data["weight"]
        destination = data["destination"]
        sender_email = data["sender_email"]
        order_status = data["order_status"]

        parcel = self.db.create_order(sender_name, sender_email, pickup_location, destination, weight, quantity,
                                      order_status)
        return parcel


class GetAll(Resource, ParcelModel):
    def get(self):
        all_parcels = self.get_all_orders()
        return all_parcels


class GetSpecificOrder(Resource, ParcelModel):
    def get(self, parcel_id):
        one_order = self.get_specific_order(parcel_id)
        return one_order


class CancelSpecific(Resource, ParcelModel):
    def put(self, parcel_id):
        cancel_order = self.cancel_order(parcel_id)
        return cancel_order


class GetUserOrders(Resource, ParcelModel):
    def get(self, sender_email):
        user_orders = self.get_orders_by_specific_user(sender_email)
        return user_orders
