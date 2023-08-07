-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_joined DATE DEFAULT CURRENT_DATE,
    password_hash TEXT NOT NULL
);

-- Documents Table
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    uploaded_date DATE DEFAULT CURRENT_DATE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

-- Logs or Activity Table
CREATE TABLE user_activity_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    activity TEXT NOT NULL,
    activity_date DATE DEFAULT CURRENT_DATE
);

-- Other SQL statements as needed

-- Create the uploads directory if it doesn't already exist
CREATE TABLE uploads (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    uploaded_date DATE DEFAULT CURRENT_DATE
);
