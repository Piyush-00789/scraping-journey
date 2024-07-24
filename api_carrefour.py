

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
from selenium import webdriver


driver = webdriver.Firefox()

driver.get('https://www.carrefour.es/supermercado/algodon-crf-precortado-200gr-carrefour/R-521001096/p')

prices = driver.find_element_by_class_name('buybox__prices')
print(prices)



exit()
rest_details = pd.read_excel('bucuresti_restaurants - onlytime.xlsx', 'tazzdata')


total_rows = len(rest_details.index)
# tazz_rows = len(tazzdata.index)
temp1 = 0

while temp1 < total_rows:
    rest_url = rest_details['URL'][temp1]






    temp1 = temp1 + 1
