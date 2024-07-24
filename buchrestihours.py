import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pandas as pd
rows = 0
with open('newrestt.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        url = row[2]
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'html.parser')

        opening_time = soup.find('div',class_= 'r_info_pill').text.replace("\n","").strip()
        o_time = opening_time.replace('Program: ','')

        with open("newrestiwthopenhour.csv", "a", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([row[1],row[2],o_time])
        rows = rows + 1
        print(rows)

