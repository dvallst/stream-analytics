import json
import logging.config
import os
import time

from kafka import KafkaProducer

from src.acquisition.open_sky import get_flights
from src.messaging.config import Config


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "..", "..", "conf", "logging.cfg"))
logger = logging.getLogger(__name__)

try:
    # Create Kafka client to publish messages to Kafka cluster
    producer = KafkaProducer(
        bootstrap_servers=Config.get_broker(),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
except Exception as ex:
    logger.error(f"Is Kafka broker up & running on {Config.get_broker()}?")
    raise ex

logger.info("Kafka broker: " + producer.config["bootstrap_servers"])
logger.info("Kafka topic: " + Config.TOPIC)

# Kafka server must be up & running
if __name__ == "__main__":
    while True:
        flights = get_flights()
        if flights:
            producer.send(topic=Config.TOPIC, value=flights)
            producer.flush()
            logger.info(f"Kafka message published with {len(flights)} flights")

        # OpenSky anonymous users can only retrieve data with a time resolution of 10 seconds
        time.sleep(10)
