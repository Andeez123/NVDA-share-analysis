from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt

user = 'root'
password = '1234'
host = '127.0.0.1'
port = 3306
database = 'nvda_stock_db'

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

df = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], index=None)

df['Returns'] = df['Close'].pct_change()

plt.figure(figsize=(16, 10))
plt.hist(df['Returns'], density=True, bins = 200)
plt.show()


