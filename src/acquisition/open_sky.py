import json
import logging
import requests


def get_flights():
    logger = logging.getLogger(__name__)
    flight_states = []

    try:
        response = requests.get(url='https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
        if response.ok:
            flight_states = json.loads(response.text)['states']
            logger.info('Flights gotten from OpenSky')
    except Exception as ex:
        logger.warning('Exception getting flights: ' + str(ex))

    return flight_states
