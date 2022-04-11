import json
import time

from kafka import KafkaProducer

from src.acquisition.open_sky import get_flights
from src.messaging.constants import Const


# Create Kafka client to publish messages to Kafka cluster
producer = KafkaProducer(
    bootstrap_servers=f"{Const.HOST}:{Const.PORT}",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Kafka server must be up & running
if __name__ == '__main__':
    while True:
        producer.send(topic=Const.TOPIC, value=get_flights())
        producer.flush()
        print('Flights published')

        time.sleep(5)
