def load_schema():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql')) as f:
        schema = f.read()
    return schema

