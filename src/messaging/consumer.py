import json

from kafka import KafkaConsumer


def consume_flights():
    consumer = KafkaConsumer('flights', value_deserializer=lambda v: json.loads(v.decode('utf-8')))
    for message in consumer:
        flight_states = message.value
        break
    consumer.close()

    return flight_states
