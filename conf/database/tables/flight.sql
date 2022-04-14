CREATE TABLE sky.flight (
    icao24          VARCHAR(10),
    callsign        VARCHAR(10),
    origin_country  VARCHAR(30),
    time_position   BIGINT,
    last_contact    BIGINT,
    longitude       DECIMAL(6,4),
    latitude        DECIMAL(6,4),
    baro_altitude   DECIMAL(7,2),
    on_ground       BOOLEAN,
    velocity        DECIMAL(6,2),
    true_track      DECIMAL(5,2),
    vertical_rate   DECIMAL(5,2),
    sensors         BIGINT,
    geo_altitude    DECIMAL(7,2),
    squawk          VARCHAR(10),
    unknown         BOOLEAN,
    spi             SMALLINT,
    position_source SMALLINT
);

ALTER TABLE sky.flight OWNER to postgres;

-- https://openskynetwork.github.io/opensky-api/rest.html#all-state-vectors
COMMENT ON COLUMN sky.flight.icao24          IS 'Unique ICAO 24-bit address of the transponder in hex string representation';
COMMENT ON COLUMN sky.flight.callsign        IS 'Callsign of the vehicle (8 chars). Can be null if no callsign has been received.';
COMMENT ON COLUMN sky.flight.origin_country  IS 'Country name inferred from the ICAO 24-bit address';
COMMENT ON COLUMN sky.flight.time_position   IS 'Unix timestamp (seconds) for the last position update. Can be null if no position report was received by OpenSky within the past 15s.';
COMMENT ON COLUMN sky.flight.last_contact    IS 'Unix timestamp (seconds) for the last update in general. This field is updated for any new, valid message received from the transponder.';
COMMENT ON COLUMN sky.flight.longitude       IS 'Longitude in ellipsoidal coordinates (WGS-84) and decimal degrees. Can be null.';
COMMENT ON COLUMN sky.flight.latitude        IS 'Latitude in ellipsoidal coordinates (WGS-84) and decimal degrees. Can be null.';
COMMENT ON COLUMN sky.flight.baro_altitude   IS 'Barometric altitude in meters. Can be null.';
COMMENT ON COLUMN sky.flight.on_ground       IS 'Boolean value which indicates if the position was retrieved from a surface position report.';
COMMENT ON COLUMN sky.flight.velocity        IS 'Velocity over ground in m/s. Can be null.';
COMMENT ON COLUMN sky.flight.true_track      IS 'True track in decimal degrees clockwise from north (0° is north). Can be null.';
COMMENT ON COLUMN sky.flight.vertical_rate   IS 'Vertical rate in m/s. A positive value indicates that the airplane is climbing, a negative value indicates that it descends. Can be null.';
COMMENT ON COLUMN sky.flight.sensors         IS 'Serial numbers of sensors which received messages from the vehicle within the validity period of this state vector. Is null if no filtering for sensor was used in the request.';
COMMENT ON COLUMN sky.flight.geo_altitude    IS 'Geometric altitude in meters. Can be null.';
COMMENT ON COLUMN sky.flight.squawk          IS 'The transponder code aka Squawk. Can be null.';
COMMENT ON COLUMN sky.flight.spi             IS 'Whether flight status indicates special purpose indicator';
COMMENT ON COLUMN sky.flight.position_source IS 'Origin of this state’s position: 0 = ADS-B, 1 = ASTERIX, 2 = MLAT, 3 = FLARM';
