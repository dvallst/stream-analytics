import json
import logging

from kafka import KafkaConsumer

from src.messaging.config import Config
from src.database.postgres import save_flights


def consume_flights():
    """
    Consume flight states from Kafka broker

    :return: Pandas DataFrame: Flight states
    """
    logger = logging.getLogger(__name__)

    try:
        # Create Kafka client to consume messages from Kafka cluster
        consumer = KafkaConsumer(
            Config.TOPIC,
            bootstrap_servers=Config.get_broker(),
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
    except Exception as ex:
        logger.error(f"Is Kafka broker up & running on {Config.get_broker()}?")
        raise ex

    flight_states = []
    for message in consumer:
        flight_states = message.value
        break

    consumer.close()
    logger.info('Flights consumed from Kafka topic: ' + Config.TOPIC)

    return save_flights(flight_states)
