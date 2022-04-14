from dash import dcc, html


def get_layout():
    return html.Div([
        html.Div([
            html.Div(html.H4('Streaming Analytics of Flights over Europe'), className='five columns'),
            html.Div([
                html.Table(
                    html.Tr([
                        html.Td('Total aircraft'),
                        html.Td(id='total'),
                        html.Td('Flying'),
                        html.Td(id='flying'),
                        html.Td('On ground'),
                        html.Td(id='on_ground'),
                    ])
                ),
                dcc.Interval(
                    id='interval-component',
                    interval=5000,  # in milliseconds
                )
            ], className='seven columns')
        ], className='row'),
        html.Div([
            html.Div(dcc.Graph(id='map'), className='five columns'),
            html.Div([
                html.Table([
                    html.Thead(
                        html.Tr([
                            html.Th(
                                'Callsign',
                                title='Callsign of the vehicle. Can be null if no callsign has been received.'),
                            html.Th('Origin country', title='Country name inferred from the ICAO 24-bit address.'),
                            html.Th(
                                'Last contact',
                                title='Unix timestamp (seconds) for the last update in general. This field is updated '
                                      'for any new, valid message received from the transponder.'),
                            html.Th('Barometric altitude', title='Barometric altitude in meters. Can be null.'),
                            html.Th(
                                'On ground',
                                title='Boolean value which indicates if the position was retrieved from a surface '
                                      'position report.'),
                            html.Th('Velocity', title='Velocity over ground in m/s. Can be null.'),
                            html.Th(
                                'True track',
                                title='True track in decimal degrees clockwise from north (0° is north). Can be null.'),
                            html.Th(
                                'Vertical rate',
                                title='Vertical rate in m/s. A positive value indicates that the airplane is climbing, '
                                      'a negative value indicates that it descends. Can be null.'
                            ),
                            html.Th('Geometric altitude', title='Geometric altitude in meters. Can be null.'),
                        ])
                    ),
                    html.Tbody(id='live-update-text')
                ]),
            ], className='seven columns'),
        ], className='row')
    ])
