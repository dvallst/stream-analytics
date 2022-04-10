-- DB creation
CREATE DATABASE stream_analytics
    OWNER = postgres
    ENCODING = 'UTF8';
COMMENT ON DATABASE stream_analytics IS 'DB to store stream data';

\c stream_analytics;

-- Schema creation
CREATE SCHEMA sky AUTHORIZATION postgres;
ALTER DATABASE stream_analytics SET search_path TO sky;
COMMENT ON SCHEMA sky IS 'Schema to store OpenSky data';

\ir tables/create_tables.sql

-- User creation
CREATE USER dvallst WITH ENCRYPTED PASSWORD 'dvallst';
GRANT ALL PRIVILEGES ON DATABASE stream_analytics TO dvallst;
GRANT ALL ON SCHEMA sky TO dvallst;
GRANT ALL ON ALL tables IN SCHEMA sky to dvallst;
