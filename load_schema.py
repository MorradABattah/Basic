import sqlite3
import os

def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        schema = f.read()

    # Connect to the SQLite database (this creates the database if it doesn't exist)
    conn = sqlite3.connect('db.sqlite3')
    try:
        # Check if the users table already exists
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        if 'users' in [table[0] for table in tables]:
            # If the table already exists, drop it
            conn.execute("DROP TABLE IF EXISTS users;")

            # Execute the SQL commands from schema.sql
            conn.executescript(schema)

            # Check if the uploads directory already exists
            if 'uploads' not in [table[0] for table in tables]:
                os.makedirs('uploads', exist_ok=True)
        else:
            # If the table doesn't exist, just execute the SQL commands
            conn.executescript(schema)

            # Check if the uploads directory already exists
            if 'uploads' not in [table[0] for table in tables]:
                os.makedirs('uploads', exist_ok=True)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Close the database connection
        conn.close()

    return True

# Call the function
load_schema()
