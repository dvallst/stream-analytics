import logging.config
import os

from dash import html
from dash.dependencies import Input, Output

from src.messaging.consumer import consume_flights
from src.dashboard.plots import create_geo_map


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "..", "..", "conf", "logging.cfg"))
logger = logging.getLogger(__name__)


def register_callbacks(app):
    @app.callback(
        Output("live-update-map", "figure"),
        Output("live-update-total", "children"),
        Output("live-update-flying", "children"),
        Output("live-update-flying-perc", "children"),
        Output("live-update-on-ground", "children"),
        Output("live-update-on-ground-perc", "children"),
        Output("live-update-country-flying-table", "children"),
        Output("live-update-country-on-ground-table", "children"),
        Output("live-update-flying-table", "children"),
        Output("live-update-on-ground-table", "children"),
        Input("interval-component", "n_intervals"),
    )
    def update_metrics(n_intervals):
        logger.info("Updating dashboard metrics...")

        df = consume_flights()

        df = df.drop(
            columns=[
                "icao24",
                "time_position",
                "last_contact",
                "unknown",
            ]
        )

        on_ground = df[df.on_ground]
        flying = df[df.on_ground == False]

        fig = create_geo_map(
            flying.latitude,
            flying.longitude,
            "Aircraft "
            + flying.callsign.str.strip()
            + " flying from "
            + flying.origin_country.str.strip()
            + " at "
            + flying.baro_altitude.astype(str).str.strip()
            + " meters",
        )

        flying_sample = flying.sample(5).drop(
            columns=[
                "longitude",
                "latitude",
                "on_ground",
                "sensors",
                "geo_altitude",
                "squawk",
                "spi",
                "position_source",
            ]
        )

        on_ground_sample = on_ground.sample(5).drop(
            columns=[
                "longitude",
                "latitude",
                "baro_altitude",
                "on_ground",
                "velocity",
                "true_track",
                "vertical_rate",
                "geo_altitude",
            ]
        )

        top_countries_flying = (
            flying.groupby("origin_country")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
            .head(5)
        )

        top_countries_on_ground = (
            on_ground.groupby("origin_country")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
            .head(5)
        )

        return (
            fig,
            len(df.index),
            len(flying.index),
            f"{round(len(flying.index) / len(df.index) * 100)}%",
            len(on_ground.index),
            f"{round(len(on_ground.index) / len(df.index) * 100)}%",
            [html.Tr([html.Td(col) for col in top_countries_flying.iloc[idx, :]]) for idx in range(4)],
            [html.Tr([html.Td(col) for col in top_countries_on_ground.iloc[idx, :]]) for idx in range(4)],
            [html.Tr([html.Td(col) for col in flying_sample.iloc[idx, :]]) for idx in range(4)],
            [html.Tr([html.Td(col) for col in on_ground_sample.iloc[idx, :]]) for idx in range(4)],
        )

    @app.callback(Output("interval-component", "disabled"), Input("boolean-switch", "on"))
    def disable_update(on):
        if on:
            logger.info("Enabling dashboard update...")
            return False
        if not on:
            logger.info("Disabling dashboard update...")
            return True
