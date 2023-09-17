from typing import Dict, List
import json
import time
import ast
from datetime import datetime 
from scans.name_resolution import check_domain_ip
from notification.telegram import new_subdomain
from kafka import KafkaConsumer
from urllib.parse import urlparse
from configs import BOOTSTRAP_SERVERS, KAFKA_TOPIC, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mongodb import MongoDBClient

def wait_for_topic(topic):
    consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
    available_topics = set(consumer.topics())

    while topic not in available_topics:
        time.sleep(1)
        available_topics = set(consumer.topics())

    consumer.close()


def process_batch(df, epoch_id):
    if not df.isEmpty():
    # Convert DataFrame to RDD
        rdd = df.rdd
    if not rdd.isEmpty():
    # Process each message in the RDD
        data = {}
        for row in rdd.collect():
    # Example: assume each Kafka messae is a JSON document
    # Insert the document into MongoDB
            record = row.asDict()
            
            # Decode value field to original format (List):
            value = ast.literal_eval(record['value'].decode('utf-8'))
            
            subdomain = value[0]
            
            if (not subdomain) or (client.check_sub_existence(subdomain, 'subs')):
                continue
            
            # alert for new subdomain
            new_subdomain(subdomain)
            
            domain = value[1]
            
            timestamp = record['timestamp']
            
            data['subdomain'] = subdomain
            data['domain'] = domain
            data['timestamp'] = timestamp
        
            #TODO Do scans 
            
            has_ip, ip_address = check_domain_ip(subdomain)
            
            if ip_address:
                data['ip_address'] = ip_address
                
        
            # if client.check_sub_existence(subdomain, 'subs'):
            #     continue
        
            client.store_message(data, 'subs')

    
# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkMongoDB") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()
    


# Define the schema for the Kafka messages
schema = StructType([
    StructField("key", StringType(), True),
    StructField("value", StringType(), True),
    StructField("timestamp", StringType(), True)
])

# Set up the connection to MongoDB
client = MongoDBClient(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, username='admin', password='password')

# Wait for the 'subs' topic to be available
wait_for_topic(KAFKA_TOPIC)

# Create an index on the 'subdomain' field in the 'subs' collection
client.create_index('subdomain', 'subs')


# Read the Kafka messages as a DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets", "earliest") \
    .option("subscribe", KAFKA_TOPIC) \
    .load()

# Start the streaming query
query = df.writeStream.foreachBatch(process_batch).start()
# Wait for the streaming to finish
query.awaitTermination()