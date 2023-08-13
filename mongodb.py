from pymongo import MongoClient
from configs import MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from datetime import datetime 

def get_client(host, port, db_name):
    return MongoClient(host, port)[db_name]

def close_client(client):
    client.close()

def store_message(message, session, collection_name):
    session[collection_name].insert_one({'subdomain': message, 'fetched_time': datetime.now()})
    