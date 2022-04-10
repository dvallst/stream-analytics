import json
import pandas as pd
import plotly.graph_objects as go
import requests
from dash import html
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

from src.messaging.consumer import consume_flights


engine = create_engine("postgresql://postgres:admin@localhost:5432/stream_analytics")


def register_callbacks(app):
    @app.callback(
        Output('live-update-text', 'children'),
        Input('interval-component', 'n_intervals')
    )
    def update_metrics(n):
        flights = consume_flights()
        df = pd.DataFrame(flights)
        cols = [
            'icao24',
            'callsign',
            'origin_country',
            'time_position',
            'last_contact',
            'longitude',
            'latitude',
            'baro_altitude',
            'on_ground',
            'velocity',
            'true_track',
            'vertical_rate',
            'sensors',
            'geo_altitude',
            'squawk',
            'unknown',
            'spi',
            'position_source',
        ]
        df = df.rename(columns=dict(zip(df.columns, cols)))
        df.to_sql(name='flight', con=engine, schema='sky', if_exists='append', index=False)
        df = df.drop(columns=[
            'icao24',
            'time_position',
            'longitude',
            'latitude',
            'sensors',
            'squawk',
            'unknown',
            'spi',
            'position_source'
        ])
        # print(time.strftime('%H:%M:%S', time.localtime(df['last_contact'])))
        return [
            html.Tr([html.Td(c) for c in df.iloc[0, :]]),
            html.Tr([html.Td(c) for c in df.iloc[1, :]]),
            html.Tr([html.Td(c) for c in df.iloc[3, :]]),
            html.Tr([html.Td(c) for c in df.iloc[4, :]]),
            html.Tr([html.Td(c) for c in df.iloc[5, :]]),
        ]

    @app.callback(
        Output('map', 'figure'),
        Input('interval-component', 'n_intervals')
    )
    def update_map(n):
        resp = requests.get('https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
        flights = json.loads(resp.text)['states']
        fig = go.Figure(
            data=go.Scattergeo(
                lon=[flight[5] for flight in flights],
                lat=[flight[6] for flight in flights],
                mode='markers',
                text='a'
            )
        )
        fig.update_layout(
            title='Real-time flights in Europe',
            geo_scope='europe',
            height=750,
            margin=dict(r=0, t=25, l=0, b=0),
        )
        return fig

    @app.callback(
        Output('total', 'children'),
        Input('interval-component', 'n_intervals')
    )
    def update_total(n):
        resp = requests.get('https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
        flights = json.loads(resp.text)['states']
        return len(flights)
