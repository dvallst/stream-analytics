from src.messaging.consumer import consume_flights


def ingest_flights():
    aircraft_df = consume_flights()

    aircraft_df = aircraft_df.drop(
        columns=[
            "icao24",
            "time_position",
            "last_contact",
            "unknown",
        ]
    )

    aircraft_on_ground = aircraft_df[aircraft_df.on_ground]
    aircraft_flying = aircraft_df[aircraft_df.on_ground == False]

    aircraft_flying_sample = aircraft_flying.sample(5).drop(
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

    aircraft_on_ground_sample = aircraft_on_ground.sample(5).drop(
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

    # The 5 countries with the most aircraft flying
    top_countries_flying = (
        aircraft_flying.groupby("origin_country")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .head(5)
    )

    # The 5 countries with the most aircraft on ground
    top_countries_on_ground = (
        aircraft_on_ground.groupby("origin_country")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .head(5)
    )

    return (
        len(aircraft_df.index),  # Total aircraft in Europe
        len(aircraft_flying.index),  # Number of aircraft that are flying
        # Percentage of aircraft that are flying
        f"{round(len(aircraft_flying.index) / len(aircraft_df.index) * 100)}%",
        len(aircraft_on_ground.index),  # Number of aircraft that are on ground
        # Percentage of aircraft that are on ground
        f"{round(len(aircraft_on_ground.index) / len(aircraft_df.index) * 100)}%",
        aircraft_flying,
        aircraft_flying_sample,
        aircraft_on_ground_sample,
        top_countries_flying,
        top_countries_on_ground,
    )
