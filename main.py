import json
import dash
import requests
import time

from dash import dcc, html
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    html.H4('TERRA Satellite Live Feed'),
    html.Div(id='live-update-text'),
    dcc.Interval(
        id='interval-component',
        interval=3000,  # in milliseconds
    )
])


@app.callback(
    Output('live-update-text', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_metrics(n):
    resp = requests.get('https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
    data = json.loads(resp.text)
    print(time.strftime('%H:%M:%S', time.localtime(data.get('time'))))
    return [
        html.Table(
            children=[
                html.Thead(
                    html.Tr([
                        html.Th('ICAO 24'),
                        html.Th('Call sign'),
                        html.Th('Origin country'),
                        html.Th('Last position'),
                        html.Th('Last contact'),
                        html.Th('Longitude'),
                        html.Th('Latitude'),
                        html.Th('Barometric altitude'),
                        html.Th('On ground'),
                        html.Th('Velocity'),
                        html.Th('Heading'),
                        html.Th('Vertical rate'),
                        html.Th('Sensor serials'),
                        html.Th('Geometric altitude'),
                        html.Th('Squawk'),
                        html.Th('Is alert'),
                        html.Th('Is Spi'),
                    ])
                ),
                html.Tbody([
                    html.Tr([html.Td(c) for c in data['states'][0:9][0]]),
                    html.Tr([html.Td(c) for c in data['states'][0:9][1]]),
                    html.Tr([html.Td(c) for c in data['states'][0:9][3]]),
                    html.Tr([html.Td(c) for c in data['states'][0:9][4]]),
                    html.Tr([html.Td(c) for c in data['states'][0:9][5]]),
                ])
            ]
        )
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
