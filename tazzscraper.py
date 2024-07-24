import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
import http.client
import json
import mimetypes
from codecs import encode


class Tazz:

    def getTime(self):
        try:
            name = soup.find("div", class_="schedule").text.replace("\n", "").replace("Program:", "").strip()
        except AttributeError:
            return False

        return name


    def getRatings(self):
        try:
            rating = soup.find("b", attrs={'itemprop': 'ratingValue'})
            rating = rating.text.replace("\n", "").strip()
        except AttributeError:
            return False

        return rating

    def getReviews(self):
        try:
            review = soup.find("span", attrs={'itemprop': 'reviewCount'})
            review = review.text.replace("\n", "").replace("recenzii",'').replace('(','').replace(")",'').strip()

        except AttributeError:
            return False

        return review

    def getMinimumOrder(self):
        try:
            price = soup.find("span", class_="price").text.replace("\n", "").strip()

        except AttributeError:
            return False

        return price

    def getDeliveryCharges(self):
        try:
            d_price = soup.find("h3", class_="price").text.replace("\n", "").strip()
            delivery_charges_price = re.sub(' +', ' ', d_price)

        except AttributeError:
            return 'Free Delivery'

        return delivery_charges_price




obj = Tazz()

##Reading the data from the excel sheet
# rest_details = pd.read_excel('bucuresti_restaurants.xlsx', 'tazzdata')
# # print(df)
# # tazzdata = pd.read_excel('tazzread.xlsx', 'Sheet1')

# total_rows = len(rest_details.index)
# tazz_rows = len(tazzdata.index)
temp1 = 0
total_rows = 1

while temp1 < total_rows:
    #rest_url = rest_details['URL'][temp1]
    #    print(rest_url)

    # temp2 = 0
   # hex7_tag = '871e50aaeffffff'
    # hex7_lat = tazzdata['hex7_lat'][temp2]
    # hex7_long = tazzdata['hex7_lng'][temp2]
    #

    # hex7_lat = str(44.94256741)
    # hex7_long = str(25.99175184)
    # url = rest_url + "?lat=" + hex7_lat + "&lon=" + hex7_long
    # rest_url = 'https://nasscom.in/members-listing'

    # response = requests.get(rest_url)
    # soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    url = "https://nasscom.in/views/ajax?_wrapper_format=drupal_ajax"

    data={'view_name': 'members_listing',
    'view_display_id': 'page_1',
    'view_path': 'members-listing/w',
    'view_base_path': 'members-listing',
    'view_dom_id': 'e80369798acdf78ad15978259a42e21ef6a498e3c5f3b7ed41e141ce19184592',
    'pager_element': '0',
    'page': '2',
    '_drupal_ajax': '1',
    'view_args': 'w'}
    
    headers = {
    'Content-Type': 'application/json',
    'Origin': 'https://nasscom.in',
    'Referer': 'https://nasscom.in/members-listing',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie': 'sess_map=brafyeeyreuterervdtzyezwawyaweavufezuqsydyvzwtccbqbqvyexsfyarauyxfesresqubfzdfuqceaubbauezwccwyasaydsbaedxcszfcdrxqqxwtvveddaqucutdudrwwswdqwvrvruqcayfv'
    }

    response = requests.post(url,  headers=headers, data=data)

    print(response)

    # rest_time = obj.getTime()
    # ratings = obj.getRatings()
    # reviews = obj.getReviews()
    # minimum_order = obj.getMinimumOrder()
    # delivery_charges = obj.getDeliveryCharges()
    # print(rest_time);
    # print(delivery_charges)

    # competitor = 'Tazz'
    # sourcing_competitor = 'sourcing_tazz'
    # average_basket_value = 'N/A'

    # country = 'Romania'
    # city = 'Roman'
    # city_code = 'RMN'
    # lat = '46.9417641889941'
    # long = '26.8831807676094'

    # address = 'N/A'
    # postal_code = 'N/A'

    # phone_number = 'N/A'
    # website = 'https://www.tazz.ro'
    # opening_hours_with_week = 'N/A'



    # restaurant_name = soup.find("h1", class_="lr_name").text.replace("\n", "").strip()
    # # print(restaurant_name)
    # left = soup.find_all("span", class_="price")
    #
    # min_order = 0
    # delievery_cost = 0
    # i = 0
    try:
    #     for price in left:
    #         #    print(price.text)
    #         if (i == 0):
    #             min_order = price.text.replace("\n", "").strip()
    #             min_order = min_order[:-3] + " 00 " + "Lei"
    #             # print(min_order)
    #
    #         if (i == 1):
    #             delievery_cost = price.text.replace("\n", "").strip()
    #             delievery_cost = delievery_cost[:-3] + " 00"
    #             # print(delievery_cost)
    #
    #         i = i + 1
    #
    #     food_tag1 = soup.find("div", class_="lr_specific").text.replace("\n", "").strip()
    #     # print(food_tag1)
    #
    #     rating = soup.find("b", attrs={'itemprop': 'ratingValue'})
    #     rating = rating.text.replace("\n", "").strip()
    #     # print(rating)
    #
    #     review = soup.find("span", attrs={'itemprop': 'reviewCount'})
    #     review = review.text.replace("\n", "").strip()
    #     # print(review)
    #
    #     address = soup.find("span", attrs={'itemprop': 'address'})
    #     address = address.text.replace("\n", "").strip()
    #     # print(address)
    #
    #     schedule_with_program = soup.find("div", attrs={'class': 'r_info_pill'})
    #     schedule_with_program = schedule_with_program.text.replace("\n", "").strip()
    #     schedule_after_replace = schedule_with_program.replace("Program:", "")
        # print(schedule_after_replace)

        # datetime object containing current date and time
        # now = datetime.now()
        # # dd/mm/YY H:M:S
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # print("date and time =", dt_string)

        # with open("tazzfinaldatajan2.csv", "a",encoding="utf-8") as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow([competitor,sourcing_competitor, rest_details['Restaurant Name'][temp1], rest_details['Tag'][temp1],
        #                      average_basket_value,minimum_order,country,city,city_code,
        #                      address,postal_code,lat,long,phone_number,ratings, reviews,
        #                      website,rest_url,rest_time, delivery_charges,
        #                      dt_string, dt_string])
        # print(temp1)
        print('213123123')
    except Exception as e:
        print(e)
        temp1 = temp1 + 1
        continue

    temp1 = temp1 + 1
    print(temp1)

