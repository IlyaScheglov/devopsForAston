CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    balance NUMERIC(15, 2) NOT NULL
);
