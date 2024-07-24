import json
import requests, sys, webbrowser, bs4
import urllib.request
import json
import csv
from datetime import datetime
import urllib.parse as urlparse
from urllib.parse import parse_qs
import sys
import time

page_no_for_url = 0

x = range(0, 180, 10)
count = 0
for n in x:
    changeIntoString = str(n)
    time.sleep(5)
    rest_response = requests.get(
        'https://www.yelp.com/search?cflt=restaurants&find_loc=Santa Pola%2CSpain&start=' + changeIntoString)
    rest_soup = bs4.BeautifulSoup(rest_response.text, "html.parser")
    rest_container = rest_soup.find('ul')
    rest_lists = rest_container.find_all('li')
    city = 'Santa Pola'
    city_code = 'SNP'
    for rest_list in rest_lists:
        if rest_list.find('a') != None:
            if 'biz' in rest_list.find('a')['href']:
                with open("YelpV1.csv", "a", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([rest_list.find('a')['href'], city, city_code])
                    count = count + 1
                    print(count)
                # print(rest_list.find('a')['href'])
            # if 'yelp' in rest_list.find('a')['href']:
            # print(rest_list.find('a')['href'])

            # print('hey')
            # print(intpage_no)

            # print(page_no_for_url)