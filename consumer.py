from typing import Dict, List
import json
from datetime import datetime 
from kafka import KafkaConsumer
from configs import BOOTSTRAP_SERVERS, KAFKA_TOPIC, MONGO_HOST, MONGO_PORT, MONGO_DB_NAME
from mongodb import get_client, store_message


class JsonConsumer:
    def __init__(self, props: Dict):
        self.consumer = KafkaConsumer(**props)

    def consume_from_kafka(self, topics: List[str]):
        self.consumer.subscribe(topics)
        
        print('Consuming from Kafka started')
        print('Available topics to consume: ', self.consumer.subscription())
        
        # Connect to mongoDB
        session = get_client(MONGO_HOST, MONGO_PORT, MONGO_DB_NAME, username='admin', password='password')
        
        while True:
            try:
                # maximum amount of time for new message = 1s
                message = self.consumer.poll(1.0)
                if message is None or message == {}:
                    continue
                for message_key, message_value in message.items():
                    for msg_val in message_value:
                        timestamp = datetime.fromtimestamp(msg_val.timestamp / 1000) 
                        formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S') 
                        
                        print(msg_val.value, formatted_timestamp)
                        store_message(session=session,
                                      message={'subdomain': msg_val.value,
                                               'fetched_time': formatted_timestamp},
                                      collection_name='subdomains')
            except KeyboardInterrupt:
                break

        self.consumer.close()


if __name__ == '__main__':
    config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'auto_offset_reset': 'earliest',
        'enable_auto_commit': True,
        'value_deserializer': lambda x: json.loads(x.decode('utf-8')),
    }

    json_consumer = JsonConsumer(props=config)
    json_consumer.consume_from_kafka(topics=[KAFKA_TOPIC])