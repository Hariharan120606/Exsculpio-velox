-- ScyllaDB schema for storing scraped airline data

CREATE KEYSPACE IF NOT EXISTS flight_scraper
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'};

USE flight_scraper;

-- Table to store metadata of each scrape
CREATE TABLE IF NOT EXISTS airline_data (
    airline text,
    url text,
    fetch_timestamp timestamp,
    title text,
    status text,
    response_time_ms int,
    PRIMARY KEY ((airline), fetch_timestamp, url)
) WITH CLUSTERING ORDER BY (fetch_timestamp DESC);

-- Example insert:
-- INSERT INTO airline_data (airline, url, fetch_timestamp, title, status, response_time_ms)
-- VALUES ('Singapore Airlines', 'https://www.singaporeair.com', toTimestamp(now()), 'Website Title', 'OK', 320);
