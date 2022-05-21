import logging
import pandas as pd

from src.database.config import Config


def save_flights(flights):
    """
    Save flight states to database

    :param flights: List of flight states
    :return: Pandas DataFrame: Flight states
    """
    df = pd.DataFrame(flights)

    cols = [
        "icao24",
        "callsign",
        "origin_country",
        "time_position",
        "last_contact",
        "longitude",
        "latitude",
        "baro_altitude",
        "on_ground",
        "velocity",
        "true_track",
        "vertical_rate",
        "sensors",
        "geo_altitude",
        "squawk",
        "spi",
        "position_source",
        "unknown",
    ]
    df = df.rename(columns=dict(zip(df.columns, cols)))

    logger = logging.getLogger(__name__)

    try:
        df.to_sql(
            name=Config.TABLE,
            con=Config.create_engine(),
            schema=Config.SCHEMA,
            if_exists="append",
            index=False,
        )
    except Exception as ex:
        logger.error(ex)
        raise ex

    logger.info(f"{len(df.index)} flights saved to Postgres")

    return df
