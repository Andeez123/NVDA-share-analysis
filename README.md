# NVDA Stock analysis
ML-Project is a project in which I scraped data from yahoo finance and loaded the data into a local MySQL database on my machine. Connection between my python program and the database is done using SQLalchemy. The data is then used to plot a 5-year time series visualization and is also used to conduct volatility analysis of the NVDA share price. 

Current Tech Stack:
- Python, Selenium, Pandas for data extraction and manipulation
- Matplotlib is used for visualizations 
- MySQL and MySQL workbench serves as the database and database query tool
- SQLalchemy connects the python program to the local MySQL database

## Using this project:
Run scraper.py, this file uses selenium to scrape the Nvidia stock data, from a set time period. 

Extracted data includes: 
date, opening and closing prices, high and low prices, adjusted closing prices and volume. 

After scraping your desired data, the data can be written to a locally hosted mysql database using connect_db.py

Reading the data is done similarly using the reading.py file

## Future Plans:
Performing futher stock price analysis on the dataset that I have scraped. This project serves as a base for me to explore other quantitative finance related projects, such as a real-time trading bot, algorithmic trading. 

The process of writing data to the database is to be improved as well, the current solution of reading from a csv file of extracted data and writing to the database is inefficient. The desired workflow would be to write the data directly to a database after the data has been extracted. 
