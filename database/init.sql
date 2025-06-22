CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(100),
    date DATE
);