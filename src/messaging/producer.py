import json
import logging.config
import os
import time

from kafka import KafkaProducer

from src.acquisition.open_sky import get_flights
from src.messaging.constants import Const


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '..', '..', 'conf', 'logging.cfg'))
logger = logging.getLogger(__name__)

# Create Kafka client to publish messages to Kafka cluster
producer = KafkaProducer(
    bootstrap_servers=f"{Const.HOST}:{Const.PORT}",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Kafka server must be up & running
if __name__ == '__main__':
    while True:
        flights = get_flights()
        if flights:
            producer.send(topic=Const.TOPIC, value=flights)
            producer.flush()
            logger.info('Flights published to Kafka')

        time.sleep(5)
