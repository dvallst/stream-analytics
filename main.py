import json
import dash
import plotly.graph_objects as go
import requests
import time

from dash import html
from dash.dependencies import Input, Output

from src.layout import get_layout


app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = get_layout()


@app.callback(
    Output('live-update-text', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_metrics(n):
    resp = requests.get('https://opensky-network.org/api/states/all?lamin=35&lomin=-10&lamax=70&lomax=60')
    data = json.loads(resp.text)
    print(time.strftime('%H:%M:%S', time.localtime(data.get('time'))))
    return [
        html.Tr([html.Td(c) for c in data['states'][0:9][0]]),
        html.Tr([html.Td(c) for c in data['states'][0:9][1]]),
        html.Tr([html.Td(c) for c in data['states'][0:9][3]]),
        html.Tr([html.Td(c) for c in data['states'][0:9][4]]),
        html.Tr([html.Td(c) for c in data['states'][0:9][5]]),
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


if __name__ == '__main__':
    app.run_server(debug=True)
