import logging.config
import os

from dash import html
from dash.dependencies import Input, Output

from src.dashboard.plots import create_geo_map
from src.ingestion.ingest import ingest_flights

logging.config.fileConfig(
    os.path.join(os.path.dirname(__file__), "..", "..", "conf", "logging.cfg")
)
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

        (
            aircraft_tot,
            flying_tot,
            flying_per,
            on_ground_tot,
            on_ground_per,
            flying,
            flying_sample,
            on_ground_from_spain_sample,
            top_countries_flying,
            top_countries_on_ground,
        ) = ingest_flights()

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

        return (
            fig,
            aircraft_tot,
            flying_tot,
            flying_per,
            on_ground_tot,
            on_ground_per,
            [
                html.Tr([html.Td(col) for col in top_countries_flying.iloc[idx, :]])
                for idx in range(len(top_countries_flying))
            ],
            [
                html.Tr([html.Td(col) for col in top_countries_on_ground.iloc[idx, :]])
                for idx in range(len(top_countries_on_ground))
            ],
            [
                html.Tr([html.Td(col) for col in flying_sample.iloc[idx, :]])
                for idx in range(len(flying_sample))
            ],
            [
                html.Tr(
                    [html.Td(col) for col in on_ground_from_spain_sample.iloc[idx, :]]
                )
                for idx in range(len(on_ground_from_spain_sample.index))
            ],
        )

    @app.callback(
        Output("interval-component", "disabled"), Input("boolean-switch", "on")
    )
    def disable_update(on):
        if on:
            logger.info("Enabling dashboard update...")
            return False
        if not on:
            logger.info("Disabling dashboard update...")
            return True
