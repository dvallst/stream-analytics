import json

from kafka import KafkaConsumer

from src.messaging.constants import Const
from src.database.postgres import save_flights


def consume_flights():
    consumer = KafkaConsumer(
        Const.TOPIC,
        bootstrap_servers=f"{Const.HOST}:{Const.PORT}",
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )
    for message in consumer:
        flight_states = message.value
        break
    consumer.close()

    return save_flights(flight_states)
