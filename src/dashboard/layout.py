import dash_bootstrap_components as dbc
import dash_daq as daq

from dash import dcc, html


def get_layout():
    """
    Get Dash app layout. It describes what the application looks like.

    :return: A Container component
    """
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H3("Streaming Analytics of Flights over Europe"),
                            html.H5("Source: The OpenSky Network"),
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        dbc.Table(
                            [
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th("Total aircraft"),
                                            html.Th("Flying", colSpan=2),
                                            html.Th("On ground", colSpan=2),
                                        ]
                                    )
                                ),
                                html.Tbody(
                                    html.Tr(
                                        [
                                            html.Td(id="live-update-total"),
                                            html.Td(id="live-update-flying"),
                                            html.Td(id="live-update-flying-perc"),
                                            html.Td(id="live-update-on-ground"),
                                            html.Td(id="live-update-on-ground-perc"),
                                        ]
                                    )
                                ),
                            ],
                            bordered=True,
                            color="info",
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        [
                            daq.BooleanSwitch(id="boolean-switch", on=True, label="Live flights"),
                            dcc.Interval(id="interval-component", interval=15000),  # in milliseconds
                        ]
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(
                            id="live-update-map",
                            config=dict(displaylogo=False, displayModeBar=True),
                        ),
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Table(
                                [
                                    html.Thead(
                                        [
                                            html.Tr(html.Th("Flying aircraft sample", colSpan=8)),
                                            html.Tr(
                                                [
                                                    html.Th(
                                                        "Callsign",
                                                        title="Callsign of the vehicle. Can be null if no callsign has "
                                                        "been received.",
                                                    ),
                                                    html.Th(
                                                        "Origin country",
                                                        title="Country name inferred from the ICAO 24-bit address.",
                                                    ),
                                                    html.Th(
                                                        "Barometric altitude",
                                                        title="Barometric altitude in meters. Can be null.",
                                                    ),
                                                    html.Th(
                                                        "Velocity",
                                                        title="Velocity over ground in m/s. Can be null.",
                                                    ),
                                                    html.Th(
                                                        "True track",
                                                        title="True track in decimal degrees clockwise from north "
                                                        "(0° is north). Can be null.",
                                                    ),
                                                    html.Th(
                                                        "Vertical rate",
                                                        title="Vertical rate in m/s. A positive value indicates that "
                                                        "the airplane is climbing, a negative value indicates "
                                                        "that it descends. Can be null.",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    html.Tbody(id="live-update-flying-table"),
                                ],
                                bordered=True,
                                color="primary",
                                hover=True,
                                striped=True,
                            ),
                            dbc.Table(
                                [
                                    html.Thead(
                                        [
                                            html.Tr(
                                                html.Th(
                                                    "On-ground aircraft sample",
                                                    colSpan=8,
                                                )
                                            ),
                                            html.Tr(
                                                [
                                                    html.Th(
                                                        "Callsign",
                                                        title="Callsign of the vehicle. Can be null if no callsign has "
                                                        "been received.",
                                                    ),
                                                    html.Th(
                                                        "Origin country",
                                                        title="Country name inferred from the ICAO 24-bit address.",
                                                    ),
                                                    html.Th(
                                                        "Sensors",
                                                        title="Serial numbers of sensors which received messages from "
                                                        "the vehicle within the validity period of this state "
                                                        "vector. Is null if no filtering for sensor was used in "
                                                        "the request.",
                                                    ),
                                                    html.Th(
                                                        "Squawk",
                                                        title="The transponder code aka Squawk. Can be null.",
                                                    ),
                                                    html.Th(
                                                        "SPI",
                                                        title="Whether flight status indicates special purpose "
                                                        "indicator.",
                                                    ),
                                                    html.Th(
                                                        "Position source",
                                                        title="Origin of this state’s position: 0 = ADS-B, "
                                                        "1 = ASTERIX, 2 = MLAT, 3 = FLARM.",
                                                    ),
                                                ]
                                            ),
                                        ]
                                    ),
                                    html.Tbody(id="live-update-on-ground-table"),
                                ],
                                bordered=True,
                                color="secondary",
                                hover=True,
                                striped=True,
                            ),
                        ]
                    ),
                ]
            ),
        ],
        fluid=True,
    )
