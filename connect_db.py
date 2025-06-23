import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

#connect to database
engine = create_engine(connection_string)


df = pd.read_csv('NVDA historical.csv')
print("Writing to MySQL Database")
with engine.connect() as connection:
    df.to_sql('3_mth_data', connection, if_exists='replace', index=False, chunksize=10000)

print('Script executed succesfully')

