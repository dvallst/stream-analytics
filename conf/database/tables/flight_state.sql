CREATE TABLE stream.flight_state (
    ftime               VARCHAR(100),
    icao24              VARCHAR(100),
    callsign            VARCHAR(100),
    origin_country      VARCHAR(100),
    time_position       VARCHAR(100),
    last_contact        VARCHAR(100),
    longitude           VARCHAR(100),
    latitude            VARCHAR(100),
    geometric_altitude  VARCHAR(100),
    on_ground           VARCHAR(100),
    velocity            VARCHAR(100),
    heading             VARCHAR(100),
    vertical_rate       VARCHAR(100),
    sensors             VARCHAR(100),
    barometric_altitude VARCHAR(100),
    squawk              VARCHAR(100),
    spi                 VARCHAR(100),
    position_source     VARCHAR(100)
);

ALTER TABLE stream.flight_state OWNER to postgres;
