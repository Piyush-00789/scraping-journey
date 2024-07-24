#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:49:04 2021

@author: tony
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
from selenium import webdriver




    
    
    
    


response = requests.get('https://glovoapp.com/en/bcn/store/super-glovo/')
soup = BeautifulSoup(response.content, 'html.parser')

allcategories = soup.find('section',class_='collection')
categoriesArray = allcategories.find_all('section')

count = 0
for category in categoriesArray:
    link_without_domain = category.find('a')['href']
    mainlink = 'https://glovoapp.com' + link_without_domain
    category_name = category.text.replace("\n", "").strip()
    secondLevelSoupResponse = requests.get(mainlink)
    secondLevelSoup = BeautifulSoup(secondLevelSoupResponse.content, 'html.parser')
    allCategoriesInCategory = secondLevelSoup.find('section',class_='collection')
    specificCategory = allCategoriesInCategory.find_all('a')
    try:
        
        for link in specificCategory:
            productLink = 'https://glovoapp.com'+link['href']
            #productDataResponse = requests.get(productLink)
            
            with open("glovowebsiteV2.csv", "a",encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([category_name, mainlink, productLink])
                count = count + 1
                print(count)
    except Exception:
        continue
        
       # productDataSoup = BeautifulSoup(productDataResponse.content, 'html.parser')
       # productsCollection = productDataSoup.find("section", class_="store-collection")
       # productsData = productsCollection.find_all('div',attrs={'data-test-id':'collection-sections'})
       # for prodData in productsData:
       #     subcategory = obj.getProductCategory(prodData)
       #     obj.getProductNamesAndPrice(prodData)
       #     print(subcategory)

    
    




#driver.close()