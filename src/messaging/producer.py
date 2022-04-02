import json
import requests
import time

from kafka import KafkaProducer


# Kafka client to publish records to Kafka cluster
# Kafka server must be up & running on localhost:9092
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    response = requests.get('https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
    flights = json.loads(response.text)['states']

    producer.send(topic='flights', value=flights)
    producer.flush()
    print('Message published')

    time.sleep(5)
