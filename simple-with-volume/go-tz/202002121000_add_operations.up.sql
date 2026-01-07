CREATE TABLE IF NOT EXISTS operations (
    id varchar(255) PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL
);
