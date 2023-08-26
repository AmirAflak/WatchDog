from typing import Dict, List
import json
from datetime import datetime 
from kafka import KafkaConsumer
from configs import BOOTSTRAP_SERVERS, KAFKA_TOPIC, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
# from mongodb import get_client, store_message


# class JsonConsumer:
#     def __init__(self, props: Dict):
#         self.consumer = KafkaConsumer(**props)

#     def consume_from_kafka(self, topics: List[str]):
#         self.consumer.subscribe(topics)
        
#         print('Consuming from Kafka started')
#         print('Available topics to consume: ', self.consumer.subscription())
        
#         # Connect to mongoDB
#         session = get_client(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, username='admin', password='password')
        
#         while True:
#             try:
#                 # maximum amount of time for new message = 1s
#                 message = self.consumer.poll(1.0)
#                 if message is None or message == {}:
#                     continue
#                 for message_key, message_value in message.items():
#                     for msg_val in message_value:
#                         timestamp = datetime.fromtimestamp(msg_val.timestamp / 1000) 
#                         formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S') 
                        
#                         print(msg_val.value, formatted_timestamp)
#                         store_message(session=session,
#                                     message={'subdomain': msg_val.value,
#                                             'fetched_time': datetime.now()},
#                                     collection_name='subdomains')
#             except KeyboardInterrupt:
#                 break

#         self.consumer.close()


# if __name__ == '__main__':
#     config = {
#         'bootstrap_servers': BOOTSTRAP_SERVERS,
#         'auto_offset_reset': 'latest',
#         'enable_auto_commit': True,
#         'value_deserializer': lambda x: json.loads(x.decode('utf-8')),
#     }

#     json_consumer = JsonConsumer(props=config)
#     json_consumer.consume_from_kafka(topics=[KAFKA_TOPIC])
    
    
    
# from pyspark import SparkContext, SparkConf
# from pyspark.streaming import StreamingContext
# from pyspark.streaming.kafka import KafkaUtils
# from mongodb import MongoDBClient

# # Setup MongoDB connection
# client = MongoDBClient(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, username='admin', password='password')

# # Function to process each RDD (batch)
# def process_rdd(rdd):
#     if not rdd.isEmpty():
#         # Process each message in the RDD
#         for message in rdd.collect():
#             print(message)
#             # Example: assume each Kafka message is a JSON document
#             # Insert the document into MongoDB
#             # collection.insert_one(message)

# # Create SparkConf and StreamingContext
# conf = SparkConf()
# sc = SparkContext(conf=conf)
# ssc = StreamingContext(sc, batchDuration=10)  # Process messages every 10 seconds

# # Create a Kafka stream and consume from the specified topic
# kafka_params = {"bootstrap.servers": "localhost:9092",
#                 "auto.offset.reset": "smallest"}  # Kafka broker address
# topic = "subs"  # Kafka topic to consume
# kafka_stream = KafkaUtils.createDirectStream(ssc, [topic], kafka_params)

# # Process each RDD (batch) in the DStream
# kafka_stream.foreachRDD(process_rdd)

# # Start the streaming context
# ssc.start()
# ssc.awaitTermination()


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
    # Example: assume each Kafka message is a JSON document
    # Insert the document into MongoDB
            print(row.asDict())
    # collection.insert_one(row.asDict())
    
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


# Read the Kafka messages as a DataFrame
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("startingOffsets", "earliest") \
    .option("subscribe", "subs") \
    .load()

# Parse the value column (assuming it contains JSON) and extract required fields
# parsed_df = df \
#     .select(from_json(col("value").cast("string"), schema).alias("data")) \
#     .select("data.*")

# # Define any required processing on the parsed DataFrame
# processed_df = parsed_df \
#     .withColumn("processed_value", <process_function>(col("value")))

# # Define the write stream to MongoDB
# write_stream = processed_df \
#     .writeStream \
#     .foreachBatch(lambda batch_df, batch_id: batch_df.write.format("mongo").mode("append").save())

# Start the streaming query
query = df.writeStream.foreachBatch(process_batch).start()
# Wait for the streaming to finish
query.awaitTermination()