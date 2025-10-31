from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from db_utils import *  # replace with your actual models module

DB_PATH = "sqlite:///database.db"  # adjust path if needed

# Set up engine and session
engine = create_engine(DB_PATH, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Use inspector to get table info
inspector = inspect(engine)
tables = inspector.get_table_names()

tables = ['fon']

print("=== Database Tables ===")
for table in tables:
    print(f"\n--- {table} ---")

    # Print column info
    columns = inspector.get_columns(table)
    for col in columns:
        print(f"{col['name']} ({col['type']})", end=" | ")
    print("\n")

    # Query a sample of rows
    try:
        with engine.connect() as conn:
            rows = conn.execute(text(f"SELECT * FROM {table}")).fetchall()
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Error querying table {table}: {e}")



'''
change hamu5 to ham=5
5-06/5-06-09.mp3

'''