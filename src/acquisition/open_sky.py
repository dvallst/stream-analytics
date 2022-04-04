import json
import requests


def get_flights():
    flight_states = []

    try:
        response = requests.get(url='https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
        if response.ok:
            flight_states = json.loads(response.text)['states']
    except Exception as ex:
        print('Exception while getting flights')
        print(str(ex))

    return flight_states
