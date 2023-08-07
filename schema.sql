-- Users Table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    date_joined DATE DEFAULT CURRENT_DATE,
    password_hash TEXT NOT NULL
);

-- Documents Table
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    filename TEXT NOT NULL,
    uploaded_date DATE DEFAULT CURRENT_DATE,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Logs or Activity Table
CREATE TABLE user_activity_logs (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    activity TEXT NOT NULL,
    activity_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Other SQL statements as needed
