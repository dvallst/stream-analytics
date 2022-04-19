import logging
import pandas as pd

from src.database.config import Config


def save_flights(flights):
    df = pd.DataFrame(flights)

    cols = [
        'icao24',
        'callsign',
        'origin_country',
        'time_position',
        'last_contact',
        'longitude',
        'latitude',
        'baro_altitude',
        'on_ground',
        'velocity',
        'true_track',
        'vertical_rate',
        'sensors',
        'geo_altitude',
        'squawk',
        'unknown',
        'spi',
        'position_source',
    ]
    df = df.rename(columns=dict(zip(df.columns, cols)))

    df.to_sql(name=Config.TABLE, con=Config.create_engine(), schema=Config.SCHEMA, if_exists='append', index=False)

    logger = logging.getLogger(__name__)
    logger.info(str(len(df.index)) + ' flights saved to Postgres')

    return df
