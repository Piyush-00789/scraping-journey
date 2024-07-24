import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv


from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(50)
url = 'https://wolt.com/en/kaz/almaty/discovery/category-pizza:almaty'
driver.get(url)
full_details = driver.find_element_by_class_name('ListPage__list___24Dl6')

restaurant_names = full_details.find_elements_by_class_name('VenueBanner__title___10bFq')

for rest_name in restaurant_names:
	print(rest_name.text.replace("\n","").strip())


driver.close()