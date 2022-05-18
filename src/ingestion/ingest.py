from src.messaging.consumer import consume_flights


def ingest_flights():
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
        flying.groupby("origin_country").size().reset_index(name="count").sort_values("count", ascending=False).head(5)
    )

    top_countries_on_ground = (
        on_ground.groupby("origin_country")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .head(5)
    )

    return (
        len(df.index),
        len(flying.index),
        f"{round(len(flying.index) / len(df.index) * 100)}%",
        len(on_ground.index),
        f"{round(len(on_ground.index) / len(df.index) * 100)}%",
        flying,
        flying_sample,
        on_ground_sample,
        top_countries_flying,
        top_countries_on_ground,
    )
