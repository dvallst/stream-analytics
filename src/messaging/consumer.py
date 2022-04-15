import json
import logging

from kafka import KafkaConsumer

from src.messaging.config import Config
from src.database.postgres import save_flights


def consume_flights():
    consumer = KafkaConsumer(
        Config.TOPIC,
        bootstrap_servers=f"{Config.HOST}:{Config.PORT}",
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    flight_states = []
    for message in consumer:
        flight_states = message.value
        break

    consumer.close()

    logger = logging.getLogger(__name__)
    logger.info('Flights consumed from Kafka')

    return save_flights(flight_states)
