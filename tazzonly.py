import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re



class Tazz:

    def getTime(self):
        try:
            name = soup.find("div", class_="schedule").text.replace("\n", "").replace("Program:", "").strip()
        except AttributeError:
            return False

        return name


    def getRatingsandReviews(self):
        rat = 'N/A'
        rev = 'N/A'

        try:
            rating = soup.find("div", attrs={'class': 'rating_box'})
            ratings_tags = str(rating)
            scheduleDetails = BeautifulSoup(ratings_tags, 'html.parser')
            try:
                rating = scheduleDetails.find('b')
                rat = rating.text.replace("\n", "").strip()
            except AttributeError:
                rat = 'N/A'


            try:
                reviews = scheduleDetails.find('span')
                rev = reviews.text.replace("\n", "").replace("(", "").replace(")", "").replace("recenzii", "").strip()
            except AttributeError:
                rev = 'N/A'


        except AttributeError:
            rr = [rat, rev]
            return rr

        rr = [rat , rev]
        return rr

    def getReviews(self):
        try:
            review = soup.find("span", attrs={'itemprop': 'reviewCount'})
            review = review.text.replace("\n", "").replace("recenzii",'').replace('(','').replace(")",'').strip()

        except AttributeError:
            return 'N/A'

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


    def getAddress(self):
        try:
            address = soup.find("div", class_="address").text.replace("\n", "").strip()

        except AttributeError:
            return 'No address'

        return address

    def getSchedule(self):
        all_schedule_in_one = ''
        try:
            allschedule = soup.findAll("div", class_="schedule-row")
            i = 0
            for schedule in allschedule:
                s = str(schedule)
                scheduleDetails = BeautifulSoup(s, 'html.parser')
                try:
                    day_and_time = scheduleDetails.findAll("div", class_="text")
                    z = 0
                    for single in day_and_time:
                        if(z == 0):
                            day = single.text.replace("\n", "").strip()
                        if(z == 1):
                            time = single.text.replace("\n", "").strip()
                            both = day + '  ' + time + "\n"
                            all_schedule_in_one = all_schedule_in_one + both

                        z = z + 1




                except AttributeError:
                    continue
                i = i+1

        except AttributeError:
            return 'No schedule'


        return all_schedule_in_one






obj = Tazz()

##Reading the data from the excel sheet
rest_details = pd.read_excel('bucuresti_restaurants - onlytime.xlsx', 'tazzdata')
# print(df)
# tazzdata = pd.read_excel('tazzread.xlsx', 'Sheet1')

total_rows = len(rest_details.index)
# tazz_rows = len(tazzdata.index)
temp1 = 0

while temp1 < total_rows:
    rest_url = rest_details['URL'][temp1]
    #    print(rest_url)

    # temp2 = 0
    #hex7_tag = '871e50aaeffffff'
    # hex7_lat = tazzdata['hex7_lat'][temp2]
    # hex7_long = tazzdata['hex7_lng'][temp2]
    #

    # hex7_lat = str(44.94256741)
    # hex7_long = str(25.99175184)
    # url = rest_url + "?lat=" + hex7_lat + "&lon=" + hex7_long

    #response = requests.get(rest_url + '/informatii')
    response = requests.get(rest_url)

    soup = BeautifulSoup(response.content, 'html.parser')
   # print(soup)

    rr = obj.getRatingsandReviews()
    print(rr[0])
    print(rr[1])




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
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)

        with open("tazzonlyreviewsandratings22222.csv", "a",encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([rr[0],rr[1]])
        print(temp1)
    except Exception as e:
        print(e)
        continue

    temp1 = temp1 + 1
    print(temp1)

