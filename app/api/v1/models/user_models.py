from flask import jsonify, make_response

users = []


class UserModel():
    def __init__(self):
        
        self.db = users

    def save(self, user_name, email, password):
        payload = {
            'user_id' : len(users) + 1,
            'user_name' : user_name,
            'email' : email,
            'password' : password
        }

        users.append(payload)
        return users

    def getusers(self):
        return users
        
    def get(self, user_id):
        user = [user for user in users if user["user_id"] == user_id]
        for user in users:
            if user["user_id"] == user_id:
                return user
