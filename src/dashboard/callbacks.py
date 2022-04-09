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
            'ftime',
            'icao24',
            'callsign',
            'origin_country',
            'time_position',
            'last_contact',
            'longitude',
            'latitude',
            'geometric_altitude',
            'on_ground',
            'velocity',
            'heading',
            'vertical_rate',
            'sensors',
            'barometric_altitude',
            'squawk',
            'spi',
            'position_source',
        ]
        df\
            .rename(columns=dict(zip(df.columns, cols)))\
            .to_sql(con=engine, schema='stream', name='flight_state', if_exists='append', index=False)
        # print(time.strftime('%H:%M:%S', time.localtime(data.get('time'))))
        return [
            html.Tr([html.Td(c) for c in flights[0]]),
            html.Tr([html.Td(c) for c in flights[1]]),
            html.Tr([html.Td(c) for c in flights[3]]),
            html.Tr([html.Td(c) for c in flights[4]]),
            html.Tr([html.Td(c) for c in flights[5]]),
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
