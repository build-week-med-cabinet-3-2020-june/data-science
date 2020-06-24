import pandas as pd
import os
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cursor = connection.cursor(cursor_factory=DictCursor)

df = pd.read_csv('merged.csv')

effects = df.to_dict("records")

list_of_types = [(c["Effects"], c["Type"]) for c in effects]
print(list_of_types)
insert_query = "INSERT INTO Medcab (Effects, Types) VALUES %s"
execute_values(cursor, insert_query, list_of_types)
connection.commit()
cursor.close()
connection.close()