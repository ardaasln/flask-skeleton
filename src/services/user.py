from app import mongo
from flask import current_app


class UserService:
    def __init__(self):
        pass

    @staticmethod
    def add_user(user_to_be_added: dict):
        collection = mongo.db.users
        collection.insert_one(user_to_be_added)
        current_app.logger.debug('User with email {} added'.format(user_to_be_added['email']))

    @staticmethod
    def get_user(email: str):
        collection = mongo.db.users
        collection.find_one({'email': email})

