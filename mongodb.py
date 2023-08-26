from pymongo import MongoClient
from configs import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from datetime import datetime 

# def get_client(host, port, db_name, username, password):
#     return MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")[db_name]

# def close_client(client):
#     client.close()

# def store_message(session, message, collection_name):
#     session[collection_name].insert_one(message)

class MongoDBClient:
    def __init__(self, host, port, db_name, username, password):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        self.db = self.client[db_name]
    
    def store_message(self, session, message, collection_name):
        session[collection_name].insert_one(message)
    
    def close(self):
        self.client.close()