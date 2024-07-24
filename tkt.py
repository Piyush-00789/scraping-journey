#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:35:22 2021

@author: tony
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
from selenium import webdriver
import urllib.request
import time

driver = webdriver.Firefox()
driver.implicitly_wait(50)
driver.get("https://tkt.ge/restaurants")

restaurant_containers = driver.find_elements_by_class_name('style__EventsCategoryItemsContainer-sc-1lfq6lj-3')

for restaurants_headings in restaurant_containers:
    restnames = restaurants_headings.find_elements_by_class_name('eventItem__EventItemContainer-sc-1xt5420-0')
    rest_addresses = restaurants_headings.find_elements_by_class_name('eventItem__EventItemDescLocation-sc-1xt5420-7')   
    rest_times = restaurants_headings.find_elements_by_class_name('eventItem__EventItemDescTime-sc-1xt5420-8')   
    links = restaurants_headings.find_elements_by_tag_name('a')   
    images_link = restaurants_headings.find_elements_by_tag_name('img')   

    print(len(restnames))
    print(len(restnames))
    print(len(rest_times))
    print(len(links))


    i=0
    for restname,rest_address,rest_time,image_link in zip(restnames,rest_addresses,rest_times,images_link):
        print('Rest_name' + restname.get_attribute('title'))
        print('Restaddress' + rest_address.text)
        print('Resttime' + rest_time.text)
        print('URL' + links[i].get_attribute('href'))
        i = i + 2

        try:
            
           # urllib.request.urlretrieve(image_link.get_attribute('src'), 'tkt/'+restname.get_attribute('title'))

            with open("tktdatageorgiaV3.csv", "a",encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['tkt.ge','sourcing_tkt.ge', restname.get_attribute('title'), 'NA','Georgia','NA','NA',rest_address.text,'NA','NA','NA','NA','NA','NA','https://tkt.ge/',links[i].get_attribute('href'),rest_time.text,'NA','NA'])

        except:
            continue



"""
    i = 1
    count = 0
    for link in links:
        if(i%2==1):
            url = link.get_attribute('href')
            print(url)
            count = count + 1
        i = i + 1
"""   
        
    
    
driver.close()






