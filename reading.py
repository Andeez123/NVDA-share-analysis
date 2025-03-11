from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('seaborn')
mpl.rc('axes', titlesize=14, titleweight='semibold')

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

# date: trading date, open: opening price of stock for the day
# high: highest price point of the stock, low: lowest price point for the day
#close: closing price of the stock, adj close: adjusted closing price, factoring in corporate actions
#volume: total trading volume of the stock
df = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], index=None)

df['Returns'] = df['Close'].pct_change() #calculate returns based on percentage change from the previous day
df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y') #convert date column to datetime format
df.set_index('Date', inplace=True)
# Specific goals on this dataset:
# Trend Analysis: Identifying long-term trends in stock prices and market movements.
# Volatility Assessment: Evaluating the stability and risk associated with different stocks based on their price fluctuations.
# Correlation Study: Investigating how different stocks correlate with each other, understanding market segments and diversification opportunities.
# Risk-Return Trade-off Analysis: Analyzing the balance between the potential risks and rewards of different stocks, aiding in portfolio management.

#Time series of 5 years of closing prices:
#obtaining 5 year data
# df_split = df[df['Date'].between('2020-01-01', '2025-03-06')].iloc[::-1]
# trading_days = df_split['Date']

# fig, ax = plt.subplots(figsize=(16,10))
# ax.plot(trading_days, df_split['Close'],label="Closing Price", color="#3498db")
# ax.set_title("Nvidia Stock Prices with Indicators", fontsize="14", fontweight="semibold")
# ax.set_xlim([trading_days.min(), trading_days.max()])

# ax.plot(trading_days, df_split['Open'], label = 'Returns')

# #format the plots as yearly data
# ax = plt.gca()  # Get current axis
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format as year
# ax.xaxis.set_major_locator(mdates.YearLocator(base = 1))

# plt.tight_layout()
# plt.show()

#Volatility analysis:
df = df.iloc[::-1]
df['Volatility'] = df['Close'].rolling(window='7D').std()
print(df['Volatility'])




