import sqlite3
import os

def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        schema = f.read()
    
    # Connect to the SQLite database (this creates the database if it doesn't exist)
    conn = sqlite3.connect('db.sqlite3')
    try:
        # Execute the SQL commands from schema.sql
        conn.executescript(schema)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Close the database connection
        conn.close()
    
    return True

# Call the function
load_schema()
