from pymongo import MongoClient
from datetime import datetime
from pprint import pprint


client = MongoClient("mongodb+srv://admin:admin123@clustertest.c9c6nys.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_supplies
users_collection = db.sales

query = {
    'customer': {
        '$or': [
            {'gender': 'M', 'age': {'$gte': 60}},
            {'gender': 'F', 'age': {'$gte': 55}}
        ]
    }
}

cursor = users_collection.find(query)
q = 0
for doc in cursor:
    q += 1
print(q)
