from typing import Dict, List
import json
from datetime import datetime 
from kafka import KafkaConsumer
from configs import BOOTSTRAP_SERVERS, KAFKA_TOPIC, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, DOMAIN

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from mongodb import MongoDBClient


def process_batch(df, epoch_id):
    if not df.isEmpty():
    # Convert DataFrame to RDD
        rdd = df.rdd
    if not rdd.isEmpty():
    # Process each message in the RDD
        for row in rdd.collect():
    # Example: assume each Kafka messae is a JSON document
    # Insert the document into MongoDB
            record = row.asDict() 
            print(record)
            subdomain = record['value'].decode('utf-8')
            timestamp = record['timestamp']
            
            #TODO Do scans 
            
            if collection.find({'subdomain': subdomain}).count() > 0:
                continue
            
            client.store_message({'subdomain': subdomain,
                           'domain': DOMAIN,
                           'timestamp': timestamp}, 'subs')

    
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
collection = client['subs']

# Read the Kafka messages as a DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets", "earliest") \
    .option("subscribe", "subs") \
    .load()

# Start the streaming query
query = df.writeStream.foreachBatch(process_batch).start()
# Wait for the streaming to finish
query.awaitTermination()