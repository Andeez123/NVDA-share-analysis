
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
# options.add_argument("--headless=new")

#web driver setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get('https://finance.yahoo.com/quote/NVDA/history/?period1=917015400&period2=1741322781')

body = driver.find_element(By.TAG_NAME, 'tbody')
dates = []
open_prices = []
high_prices = []
low_prices = []
close_prices = []
adj_closes = []
volumes = []

elements = body.find_elements(By.TAG_NAME, "tr")
for elem in elements:
    try:
        date = elem.find_element(By.XPATH, "./td[1]").text
        open_price = elem.find_element(By.XPATH, "./td[2]").text
        high_price = elem.find_element(By.XPATH, "./td[3]").text
        low_price = elem.find_element(By.XPATH, "./td[4]").text
        close_price = elem.find_element(By.XPATH, "./td[5]").text
        adj_close = elem.find_element(By.XPATH, "./td[6]").text
        volume = elem.find_element(By.XPATH, "./td[7]").text

        dates.append(date)
        open_prices.append(open_price)
        high_prices.append(high_price)
        low_prices.append(low_price)
        close_prices.append(close_price)
        adj_closes.append(adj_close)
        volumes.append(volume)
    except:
        pass
       

df = pd.DataFrame({
    'Date': dates,
    'Open': open_prices,
    'High': high_prices,
    'Low': low_prices,
    'Close': close_prices,
    'Adj Close': adj_closes,
    'Volume': volumes
})
df.to_csv('NVDA 3 months.csv', index=False)

driver.quit()