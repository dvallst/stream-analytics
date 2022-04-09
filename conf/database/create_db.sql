-- DB creation
CREATE DATABASE stream_analytics
    OWNER = postgres
    ENCODING = 'UTF8';
COMMENT ON DATABASE stream_analytics IS 'DB to store stream data';

\c stream_analytics;

-- Schema creation
CREATE SCHEMA stream AUTHORIZATION postgres;
ALTER DATABASE stream_analytics SET search_path TO stream;
COMMENT ON SCHEMA stream IS 'Schema to store stream data';

\ir tables/create_tables.sql

-- User creation
CREATE USER dvallst WITH ENCRYPTED PASSWORD 'dvallst';
GRANT ALL PRIVILEGES ON DATABASE stream_analytics TO dvallst;
GRANT ALL ON SCHEMA stream TO dvallst;
GRANT ALL ON ALL tables IN SCHEMA stream to dvallst;
