

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
from selenium import webdriver

#response = requests.get('https://www.carrefour.es/supermercado/el-mercado/cat20002/c')
#soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)

driver = webdriver.Firefox()

driver.get('https://www.carrefour.es/supermercado/el-mercado/cat20002/c')
products = driver.find_element_by_class_name('product-card-list__item')
prod_name = products.find_elements_by_class_name('product-card__title')

products_cart_price = products.find_elements_by_class_name('product-card__prices')
for pcp,pname in zip(products_cart_price,prod_name):
    with open("carrefour2021v5.0jan.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
                ['el-mercado',pname.text,pcp.text])
driver.close()

exit()


for x in range(792,1008,24):
    v= str(x)
    driver = webdriver.Firefox()

    driver.get('https://www.carrefour.es/supermercado/parafarmacia/cat20008/c?offset='+v)

    products = driver.find_element_by_class_name('product-card-list__list')
    products_links = products.find_elements_by_class_name('product-card__media-link')
    prod_name = products.find_elements_by_class_name('product-card__title')
    per_unit = products.find_elements_by_class_name('product-card__price-per-unit')

    products_cart_price = products.find_elements_by_class_name('product-card__price')
    for pd,pcp,pname,pu in zip(products_links,products_cart_price,prod_name,per_unit):
        with open("carrefour2021v4.0jan.csv", "a", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ['Parafarmacia',pname.text,pcp.text,pu.text,pd.get_attribute('href')])
    print(x)
    driver.close()

print('Its done')
