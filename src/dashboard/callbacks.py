import logging.config
import os

from dash import html
from dash.dependencies import Input, Output

from src.messaging.consumer import consume_flights
from src.dashboard.plots import create_scatter_geo


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '..', '..', 'conf', 'logging.cfg'))
logger = logging.getLogger(__name__)


def register_callbacks(app):
    @app.callback(
        Output('map', 'figure'),
        Output('total', 'children'),
        Output('flying', 'children'),
        Output('on_ground', 'children'),
        Output('live-update-text', 'children'),
        Input('interval-component', 'n_intervals')
    )
    def update_metrics(n):
        logger.info('Updating metrics...')

        df = consume_flights()

        on_ground = df[df.on_ground]
        flying = df[df.on_ground == False]

        fig = create_scatter_geo(flying.latitude, flying.longitude)

        flying_sample = flying.sample(5)
        flying_sample = flying_sample.drop(columns=[
            'icao24',
            'time_position',
            'last_contact',
            'longitude',
            'latitude',
            'on_ground',
            'sensors',
            'geo_altitude',
            'squawk',
            'unknown',
            'spi',
            'position_source',
        ])

        return \
            fig, \
            len(df.index), \
            len(flying.index), \
            len(on_ground.index), \
            [html.Tr([html.Td(col) for col in flying_sample.iloc[idx, :]]) for idx in range(5)]
