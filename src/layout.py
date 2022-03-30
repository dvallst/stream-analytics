from dash import dcc, html


def get_layout():
    return html.Div([
        html.H6('TERRA Satellite Live Feed'),
        html.Div(id='total'),
        html.Table([
            html.Thead(
                html.Tr([
                    html.Th('ICAO24', title='ICAO24 address of the transmitter in hex string representation'),
                    html.Th('Callsign', title='Callsign of the vehicle. Can be None if no callsign has been received.'),
                    html.Th('Origin country', title='Inferred through the ICAO24 address'),
                    html.Th(
                        'Time position',
                        title='Seconds since epoch of last position report. Can be None if there was no position '
                              'report received by OpenSky within 15s before.'
                    ),
                    html.Th('Last contact', title='Seconds since epoch of last received message from this transponder'),
                    html.Th('Longitude', title='In ellipsoidal coordinates (WGS-84) and degrees. Can be None.'),
                    html.Th('Latitude', title='In ellipsoidal coordinates (WGS-84) and degrees. Can be None.'),
                    html.Th('Geometric altitude', title='Geometric altitude in meters. Can be None.'),
                    html.Th('On ground', title='True if aircraft is on ground (sends ADS-B surface position reports)'),
                    html.Th('Velocity', title='Over ground in m/s. Can be None if information not present.'),
                    html.Th(
                        'Heading',
                        title='In decimal degrees (0 is north). Can be None if information not present.'
                    ),
                    html.Th(
                        'Vertical rate',
                        title='In m/s, incline is positive, decline negative. Can be None if information not present.'),
                    html.Th(
                        'Sensors',
                        title='Serial numbers of sensors which received messages from the vehicle within the validity '
                              'period of this state vector. Can be None if no filtering for sensor has been '
                              'requested).'
                    ),
                    html.Th('Barometric altitude', title='Barometric altitude in meters. Can be None.'),
                    html.Th('Squawk', title='Transponder code aka Squawk. Can be None.'),
                    html.Th('SPI', title='Special purpose indicator'),
                    html.Th(
                        'Position source',
                        title='Origin of this state’s position: 0 = ADS-B, 1 = ASTERIX, 2 = MLAT, 3 = FLARM'
                    ),
                ])
            ),
            html.Tbody(id='live-update-text')
        ]),
        dcc.Graph(id='map'),
        dcc.Interval(
            id='interval-component',
            interval=3000,  # in milliseconds
        )
    ])
