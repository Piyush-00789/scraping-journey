import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv

from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(50)

details = driver.get('https://food.jumia.co.ke/restaurants/city/nairobi')


res_name = driver.find_elements_by_class_name('name')

full_details = driver.find_element_by_class_name('restaurant-list')

links = full_details.find_elements_by_tag_name('a')

info = full_details.find_elements_by_class_name('bottom-info')
ratins = ''
tags = ''

# for i in info:
#     rating_and_tag = i.find_elements_by_tag_name('span')
#     i = 0
#     for r_and_t in rating_and_tag:
#         i = i + 1
#         if(i==1):
#             ratings = r_and_t.text.replace('•','').replace("\n","").strip()
#             print(ratings)
#         else:
#             tags = r_and_t.text.replace('$','').replace('•','').replace("\n","").strip()
#             print(tags)



# print(full_details)

count = 0
for r,link,i in zip(res_name,links,info):
    now = datetime.now()
    created_at_date = now.strftime("%d/%m/%Y")
    created_at_time = now.strftime("%H:%M:%S")
    url = link.get_attribute('href')
    rating_and_tag = i.find_elements_by_tag_name('span')
    p = 0
    for r_and_t in rating_and_tag:
        p = p + 1
        if (p == 1):
            ratings = r_and_t.text.replace('•', '').replace("\n", "").strip()
            print(ratings)
        else:
            tags = r_and_t.text.replace('$', '').replace('•', '').replace("\n", "").strip()
            print(tags)

    with open("jumiarestaurants.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([r.text,url,ratings,tags,created_at_date,created_at_time])
    count = count + 1
    print(count)


print('Its done')
driver.close()