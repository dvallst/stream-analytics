import logging
import pandas as pd

from sqlalchemy import create_engine

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

    engine = create_engine(f"postgresql://{Config.USER}:{Config.SECRET}@{Config.HOST}:{Config.PORT}/{Config.DB}")
    df.to_sql(name='flight', con=engine, schema='sky', if_exists='append', index=False)

    logger = logging.getLogger(__name__)
    logger.info(str(len(df.index)) + ' flights saved to database')

    return df
