from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

#connect to database
engine = create_engine(connection_string)

with open("test.sql", "r") as file:
    sql_query = file.read()

# Execute the query
with engine.connect() as connection:
    result = connection.execute(text(sql_query))

    # Fetch all rows
    rows = result.fetchall()

print('Data fetched succesfully')

# date: trading date, open: opening price of stock for the day
# high: highest price point of the stock, low: lowest price point for the day
#close: closing price of the stock, adj close: adjusted closing price, factoring in corporate actions
#volume: total trading volume of the stock
df = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], index=None)
df.to_csv('NVDA_data.csv')

print('Data has been saved locally')



