CREATE TABLE incomes(
    id VARCHAR(70) UNIQUE,
    user_id VARCHAR(70),
    amount FLOAT,
    created_date TIMESTAMP
);
