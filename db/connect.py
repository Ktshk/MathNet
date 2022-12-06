import pymongo
import configparser
import datetime


class MongoService:
    def __init__(self):
        configload = configparser.RawConfigParser()
        configload.read('../server.properties')
        self.client = pymongo.MongoClient(configload.get('db', 'mongourl'))

    def create_user(self, login, name, password):
        db = self.client.math_net
        users_collection = db.users

        now = datetime.datetime.utcnow()

        new_user = {
            "login": login,
            "name": name,
            "created": now,
            "last_login": now,
            "password": password
        }

        result = users_collection.insert_one(new_user)

        document_id = result.inserted_id
        print(f"_id of inserted document: {document_id}")
        return document_id

