import os

def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        schema = f.read()
    return schema

def run():
    schema = load_schema()
    db.engine.execute(schema)

if __name__ == '__main__':
    run()