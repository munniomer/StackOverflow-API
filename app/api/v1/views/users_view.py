"""User views contains Signup Resources"""

from app.api.v1.models.users_model import UserModel  # imports the user model
from flask import Flask, request, jsonify, json
from flask_restful import Resource
from werkzeug.security import generate_password_hash

db = UserModel()


class SignupResource(Resource):
    """Resource for user registration."""

    def post(self):
        """Method for posting user data"""
        data = request.get_json()
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirmPassword = data["confirmPassword"]

        hashpassword = generate_password_hash(password)

        data = db.add_user(username, email, hashpassword)

        return {"All users": data,
                "message": "User successfully created", }, 201
