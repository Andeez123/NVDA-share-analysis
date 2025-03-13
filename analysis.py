import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('seaborn')
mpl.rc('axes', titlesize=14, titleweight='semibold')

df = pd.read_csv('NVDA_data.csv')

df['Ticker'] = 'NVDA'
df['Returns'] = df['Close'].pct_change() #calculate returns based on percentage change from the previous day
df['Date'] = pd.to_datetime(df['Date']) #convert date column to datetime format

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
df_vol = df.iloc[::-1]
pivot_data = df_vol.pivot(index = 'Date', columns='Ticker', values='Close')
volatility = pivot_data.std()
#From the calculations done here: the historical volatility of the closing price NVDA stock is 24.451147, which means that NVDA's closing 
#price varies +-24.45 from its mean price over the dataset