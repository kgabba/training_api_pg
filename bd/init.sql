CREATE TABLE IF NOT EXISTS otzyvy (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    mail TEXT NOT NULL,
    phone BIGINT, 
    mood TEXT NOT NULL
);