from prefect import task, flow
from sub_finder.core import get_subs
from typing import List, Dict, Generator
from producer import JsonProducer
from consumer import JsonConsumer
import datetime
import configs

@task(log_prints=True)
def subdomain_finder() -> Generator[str, None, None]:
    return get_subs()

@task(log_prints=True)
def kafka_producer(subdomains: Generator[str, None, None]) -> None:
    config = {
        'bootstrap_servers': configs.BOOTSTRAP_SERVERS,
        'value_serializer': lambda x: json.dumps(x).encode('utf-8')
    }
    producer = JsonProducer(props=config)
    producer.publish_stat(topic=configs.KAFKA_TOPIC, subs=get_subs())

@task(log_prints=True)
def mongodb_consumer() -> None:
    config = {
        'bootstrap_servers': configs.BOOTSTRAP_SERVERS,
        'auto_offset_reset': 'earliest',
        'enable_auto_commit': True,
        'value_deserializer': lambda x: json.loads(x.decode('utf-8')),
    }

    json_consumer = JsonConsumer(props=config)
    json_consumer.consume_from_kafka(topics=[configs.KAFKA_TOPIC])
    
@flow(name="subdomains finder", log_prints=True)
def main():
    subdomains = subdomain_finder()
    kafka_producer(subdomains)
    mongodb_consumer()

if __name__ == '__main__':
    main()
    
    
    
    
    

