import plotly.graph_objects as go

from dash import html
from dash.dependencies import Input, Output

from src.messaging.consumer import consume_flights


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
        df = consume_flights()

        fig = go.Figure(
            data=go.Scattergeo(
                lon=df[df.on_ground==False].longitude,
                lat=df[df.on_ground==False].latitude,
                mode='markers',
                text='a'
            )
        )
        fig.update_layout(
            title='Real-time aircraft flying over Europe',
            geo_scope='europe',
            height=750,
            margin=dict(r=0, t=25, l=0, b=0),
        )

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
