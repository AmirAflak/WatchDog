from pymongo import MongoClient
from configs import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from datetime import datetime 

class MongoDBClient:
    def __init__(self, host, port, db_name, username, password):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")[db_name]
    
    def store_message(self, message, collection_name):
        self.client[collection_name].insert_one(message)
    
    def close(self):
        self.client.close()