#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:19:44 2021

@author: tony
"""




import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
from selenium import webdriver
import io


class Glovowebsite:

    def getProductCategory(self, productsData):
        try:
            subcategory = productsData.find('h3').text.replace("\n", "").strip()

        except AttributeError:
            return False

        return subcategory

    def getProductNamesAndPrice(self, productsData):
        try:
            productnameandprices = productsData.find_all('div', attrs={'data-test-id': 'store-product-desktop'})
            dictionary = {}
            for prodnameandprice in productnameandprices:
                product_name = prodnameandprice.find('h4').text.replace("\n", "").strip()
                product_price = prodnameandprice.find('span', attrs={'data-test-id': 'product-price-effective'}).text.replace("\n", "").strip()
                dictionary[product_name] = product_price



        except AttributeError:
            return False

        return dictionary


rest_details = pd.read_excel('glovowebsiteproductfile.xlsx', 'tazzdata')
total_rows = len(rest_details.index)
temp1 = 0
#print(rest_details)
obj = Glovowebsite()
while temp1 < total_rows:
    rest_url = rest_details['Restaurant URL'][temp1]
    category = rest_details['Restaurant Name'][temp1]
    url = rest_details['URL'][temp1]
    productDataResponse = requests.get(rest_url)
    productDataSoup = BeautifulSoup(productDataResponse.content, 'html.parser')
    productsCollection = productDataSoup.find("section", class_="store-collection")
    productsData = productsCollection.find_all('div',attrs={'data-test-id':'collection-sections'})
    for prodData in productsData:
        subcategory = obj.getProductCategory(prodData)
        nameandprice = obj.getProductNamesAndPrice(prodData)
        print(subcategory)
        print(nameandprice)
        with open("glovowebsitefinalData.csv", "a", encoding="utf-8") as csvfile:
            for productname,price in nameandprice.items():
                writer = csv.writer(csvfile)
                writer.writerow([category,subcategory,productname,price,rest_url])

    temp1 = temp1 + 1
    print(temp1)

