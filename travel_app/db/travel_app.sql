DROP TABLE sights;
DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    visited BOOLEAN,
    cities_id INT REFERENCES cities(id) ON DELETE CASCADE
);