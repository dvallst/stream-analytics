import json
import logging
import requests


def get_flights():
    """
    Get flight states from The OpenSky Network API

    :return: List: Flight states
    """
    logger = logging.getLogger(__name__)
    flight_states = []

    try:
        # Request to OpenSky REST API to get flight states over Europe
        response = requests.get(url='https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
        if response.ok:
            # Deserialize string containing JSON document (response.text) to dictionary, and get list of flight states
            flight_states = json.loads(response.text)['states']
    except Exception as ex:
        logger.warning('Exception getting flights: ' + str(ex))

    logger.info(f"{len(flight_states)} flights gotten from OpenSky")

    return flight_states
