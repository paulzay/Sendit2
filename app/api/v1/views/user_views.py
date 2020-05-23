from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.user_models import UserModel


users = []
parcels = []


class SignUp(Resource, UserModel):
	def __init__(self):
		self.db = users

	def post(self):
		data = request.get_json()
		user_id = len(users)+1
		name = data["name"]
		email = data["email"]
		password = data["password"]
		payload = {
			"user_id": len(users)+1,
			"name": name,
			"email": email,
			"password": password
		}
		users.append(payload)
		return make_response(jsonify(
			{
				"Message": "user successfully registered",
				"Data": payload
			}), 201)


class GetAllUsers(Resource):
	def get(self):
		return make_response(jsonify(
			{
				'Status': "OK",
				'Message': "Success",
				'Data': users
			}), 200)


class SingleUser(Resource):
    def get(self, user_id):
        user = [user for user in users if user["user_id"] == user_id]
        for user in users:
            if user["user_id"] == user_id:
                return make_response(jsonify(
                    {
                        'Status': "OK",
                        'Message': "Successful",
                        'Data': user
                    }), 201)
