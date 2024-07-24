import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(50)

details = driver.get('https://www.menulog.com.au/area/5000-adelaide/?lat=-34.9270286&long=138.5982513')

name = driver.find_elements_by_class_name('listing-item-title')



print(name)

driver.close()
# url = 'https://www.menulog.com.au/area/5000-adelaide/?lat=-34.9270286&long=138.5982513'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)