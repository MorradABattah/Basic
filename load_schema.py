import os
import psycopg2
from psycopg2 import sql

DATABASE_URL = 'postgresql://postgres:password@localhost:5432/mydatabase'

def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        schema = f.read()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    try:
        # Check if the users table already exists
        cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")
        tables = [table[0] for table in cur.fetchall()]

        if 'users' in tables:
            # If the table already exists, drop it
            cur.execute(sql.SQL("DROP TABLE IF EXISTS users CASCADE;"))
            conn.commit()

            # Execute the SQL commands from schema.sql
            cur.execute(schema)
            conn.commit()

        else:
            # If the table doesn't exist, just execute the SQL commands
            cur.execute(schema)
            conn.commit()

        # Check if the documents table already exists
        if 'documents' in tables:
            print('The documents table already exists. Skipping...')
            return True
        else:
            cur.execute(schema)
            conn.commit()

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Close the database connection
        cur.close()
        conn.close()

    # Check if the uploads directory already exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads', exist_ok=True)

    return True

# Call the function
load_schema()
