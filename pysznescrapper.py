import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

from selenium import webdriver

# driver = webdriver.Firefox()
# driver.implicitly_wait(50)
#
# driver.get("https://tazz.ro/bucuresti/categorie/toate/")



url = 'https://www.pyszne.pl/restauracja-tychy-tychy-43-110'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rest_names = soup.findAll('a',class_= 'restaurantname')
tags = soup.findAll('div',class_='kitchens')
all_res_ratings_total = soup.findAll('span',class_='rating-total')

delivery_time = soup.findAll('div',class_='avgdeliverytime avgdeliverytimefull open')
delivery_cost = soup.findAll('div',class_='delivery-cost js-delivery-cost notranslate')
min_order = soup.findAll('div',class_='min-order notranslate')
rest_links = soup.findAll('a',{'class':'restaurantname notranslate'})


# try:
#     for rest_link in rest_links:
#         print('https://www.pyszne.pl'+rest_link['href'])
#
#
# except Exception as IndexError:
#         rest_link = 'no link'


# for rest_link in rest_links:




# for rest_name,tag in zip(rest_names,tags):
#     print(rest_name.text.replace("\n","").strip())
#     print(tag.text.replace("\n","").strip())


# for tag in tags:
#     print(tag.text.replace("\n","").strip())

# for ratings in all_res_ratings_total:
#     rating_with_brackets = ratings.text.replace("\n","").strip()
#     ratings_last = rating_with_brackets.replace('(','')
#     rating = ratings_last.replace(')','')
#     print(rating)

#
# try:
#     for d_time in delivery_time:
#         print(d_time.text.replace("\n","").strip())
#
# except Exception as IndexError:
#     print('d_time=None')
#
# try:
#     for d_cost in delivery_cost:
#         print(d_cost.text.replace("\n","").strip())
#
# except Exception as IndexError:
#     print('d_cost=None')
#
# try:
#     for m_order in min_order:
#         print(m_order.text.replace("\n","").strip())
#
# except Exception as IndexError:
#     print('m_order=None')



count=0
for rest_link,rest_name,tag,ratings,d_time,d_cost,m_order in zip(rest_links,rest_names,tags,all_res_ratings_total,delivery_time,delivery_cost,min_order):
    rest_link = 'https://www.pyszne.pl'+rest_link['href']
    rest_name = rest_name.text.replace("\n","").strip()
    tag = tag.text.replace("\n", "").strip()
    try:
        rating_with_brackets = ratings.text.replace("\n","").strip()
        ratings_last = rating_with_brackets.replace('(','')
        rating = ratings_last.replace(')','')
    except Exception as IndexError:
        rating = 'None'
        continue

    try:
        d_time = d_time.text.replace("\n","").strip()
    except Exception as IndexError:
        d_time = 'None'
        continue

    try:
        d_cost = d_cost.text.replace("\n","").strip()
    except Exception as IndexError:
        d_cost = 'None'
        continue

    try:
        m_order = m_order.text.replace("\n","").strip()
    except Exception as IndexError:
        m_order = 'None'
        continue

    now = datetime.now()
    # dd/mm/YY H:M:S
    created_at = now.strftime("%d/%m/%Y %H:%M:%S")


    with open("pysznes.csv", "a", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([rest_name,rest_link,tag,rating,d_time,d_cost,m_order,created_at,created_at])
                count = count + 1
                print(count)








