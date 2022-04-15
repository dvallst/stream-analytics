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

        fig = create_scatter_geo(df[df.on_ground==False].longitude, df[df.on_ground==False].latitude)

        df = df.drop(columns=[
            'icao24',
            'time_position',
            'longitude',
            'latitude',
            'sensors',
            'squawk',
            'unknown',
            'spi',
            'position_source',
        ])

        return \
            fig, \
            len(df.index), \
            len(df[df.on_ground==False].index), \
            len(df[df.on_ground].index), \
            [
                html.Tr([html.Td(c) for c in df.iloc[0, :]]),
                html.Tr([html.Td(c) for c in df.iloc[1, :]]),
                html.Tr([html.Td(c) for c in df.iloc[3, :]]),
                html.Tr([html.Td(c) for c in df.iloc[4, :]]),
                html.Tr([html.Td(c) for c in df.iloc[5, :]]),
            ]
