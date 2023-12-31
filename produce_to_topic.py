import csv
import json
import time
from typing import List, Dict, Generator
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from sub_finder.core import get_subs
from configs import BOOTSTRAP_SERVERS, KAFKA_TOPIC, TARGETS

class JsonProducer(KafkaProducer):
    def __init__(self, props: Dict):
        self.producer = KafkaProducer(**props)
        
    def publish_stat(self,subs: Generator[str, None, None], topic: str, target: str):
            try:
                for sub in subs:  
                    record = self.producer.send(topic=topic,  value=(sub, target))
                    print('Record {} successfully produced at offset {}'.format(sub, record.get().offset))
            except KafkaTimeoutError as e:
                print(e.__str__())
            time.sleep(2)       
            
def run_producer(target: str):
    config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'value_serializer': lambda x: json.dumps(x).encode('utf-8')
    }
    producer = JsonProducer(props=config)
    producer.publish_stat(topic=KAFKA_TOPIC, subs=get_subs(target), target=target)   
    
if __name__ == '__main__':

    for target in TARGETS:
        run_producer(target)
            
