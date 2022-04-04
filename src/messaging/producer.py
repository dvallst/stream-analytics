import json
import time
from kafka import KafkaProducer

from src.acquisition.open_sky import get_flights


# Kafka client to publish records to Kafka cluster
# Kafka server must be up & running on localhost:9092
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

if __name__ == '__main__':
    while True:
        producer.send(topic='flights', value=get_flights())
        producer.flush()
        print('Flights published')

        time.sleep(5)
