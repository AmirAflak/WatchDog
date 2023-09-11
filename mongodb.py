from pymongo import MongoClient
from configs import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from datetime import datetime 

class MongoDBClient:
    def __init__(self, host, port, db_name, username, password):
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        self.db = self.client[db_name]
    
    def check_sub_existence(self, value, collection_name):
        return self.db.get_collection(collection_name).count_documents({"subdomain": value}) > 0
    
    def store_message(self, message, collection_name):
        self.db.get_collection(collection_name).insert_one(message)
        
    def create_index(self, field_name, collection_name):
        self.db.collection_name.create_index(field_name)
        
    def close(self):
        self.client.close()