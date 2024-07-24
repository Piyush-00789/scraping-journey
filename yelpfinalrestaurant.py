import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv
import re
import time

class Yelp:

    def getRestName(self):
        try:
            name = soup.find("h1", class_="heading--h1__373c0__dvYgw").text.replace("\n", "").strip()
        except AttributeError:
            return 'NA'

        return name

    def getRatings(self):
        try:
            ratings = soup.find("div", class_="i-stars__373c0__1BRrc")['aria-label']
            if 'star' in ratings and 'rating' in ratings:
                ratings = ratings.replace("star",'').replace('rating','')
        except Exception as e:
            return 'NA'

        return ratings

    def getReviews(self):
        try:
            div_reviews = soup.find("span", class_="text__373c0__2Kxyz text-color--white__373c0__22aE8 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B").text.replace("\n", "").strip()

        except AttributeError as e:
            return 'NA'

        return div_reviews

    def getTags(self):
        try:
            tags_abc = 'NA'
            abc = soup.find_all('span',class_='display--inline__373c0__3JqBP margin-r1__373c0__zyKmV border-color--default__373c0__3-ifU')
            temp = 0
            for a in abc:
                if temp ==2:
                    tags_abc = a.text
                    break
                temp = temp +1

        except AttributeError as e:
            return 'NA'

        if tags_abc == '':
            return 'NA'

        return tags_abc

    def getPhoneNumber(self):
        try:
            phon = 'NA'
            phone = soup.find("div", class_="css-0 padding-t2__373c0__11Iek padding-r2__373c0__28zpp padding-b2__373c0__34gV1 padding-l2__373c0__1Dr82 border--top__373c0__3gXLy border--right__373c0__1n3Iv border--bottom__373c0__3qNtD border--left__373c0__d1B7K border-radius--regular__373c0__3KbYS background-color--white__373c0__2uyKj")
            p = phone.text.replace("\n", "").strip()
            if "Phone number" in p:
                ph= p.split('Phone number', 1)[-1]
                phon = ph
                if "Get Directions" in p:
                    pho = ph.split('Get Directions')[0]
                    phon = pho

        except AttributeError as e:
            return 'NA'

        if phon == '':
            return 'NA'

        return phon

    def getAddress(self):
        try:
            address = 'NA'
            address = soup.find("address").text.replace("\n", "").replace("Spain","").strip()
        except AttributeError as e:
            return 'NA'

        if address == '':
            return 'NA'

        return address

    def getTimings(self):
        try:
            time_interval = None
            time_ = soup.find_all("p",class_='text__373c0__2Kxyz no-wrap__373c0__24-0o text-color--normal__373c0__3xep9 text-align--left__373c0__2XGa- text-weight--semibold__373c0__2l0fe text-size--large__373c0__3t60B')
            days = soup.find_all("th",class_='table-header-cell__373c0___pz7p')

            for tt,dd in zip(time_,days):
                time_of_day = tt.text.replace("(Folgetag)","").strip()
                day_name = dd.text
                time_interval = time_interval + '\n' + day_name + ' ' + time_of_day


        except Exception as e:
            return 'NA'

        if time == '' and  days=='':
            return 'NA'

        return time_interval


    def getTagsSecondVersion(self):
        try:
            tags = 'NA'
            tags_group = soup.find_all("span",class_='display--inline__373c0__3JqBP margin-r1__373c0__zyKmV border-color--default__373c0__3-ifU')
            #all_tags = tags_group.find_all('a')
            for tag in tags_group:
                if tag.text.replace("\n", "").strip() not in 'Nicht übernommen' and tag.text.replace("\n", "").strip() not in '€€':
                    tags = tag.text.replace("\n", "").strip()

        except AttributeError as e:
            return 'NA'

        if tags == '':
            return 'NA'

        return tags

    def getReviewsSecondVersion(self):
        try:
            reviews = 'NA'
            reviews_tags = soup.find("div",class_='arrange-unit__373c0__o3tjT border-color--default__373c0__3-ifU nowrap__373c0__35McF')
            reviews = reviews_tags.find('span').text.replace('Beiträge','')

        except AttributeError as e:
            return 'NA'

        if reviews =='':
            return 'NA'
        return reviews











rest_details = pd.read_excel('bucuresti_restaurants.xlsx', 'tazzdata')
total_rows = len(rest_details.index)
# tazz_rows = len(tazzdata.index)
temp1 = 0
obj = Yelp()
while temp1 < total_rows:


    url = 'https://www.yelp.com'+rest_details['URL'][temp1]
    #url = 'https://www.yelp.at/biz/l-ancora-cambrils'
    time.sleep(8)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    city = rest_details['City'][temp1]
    city_code = rest_details['City_code'][temp1]
    rest_name = obj.getRestName()
    ratings = obj.getRatings()
    #reviews = obj.getReviews()
    #tags = obj.getTags()
    phone = obj.getPhoneNumber()
    address = obj.getAddress()
    #timings = obj.getTimings()
    tags_second = obj.getTagsSecondVersion()
    reviews_second = obj.getReviewsSecondVersion()
    print(reviews_second)
    print(tags_second)
    #print(timings)

    with open("yelpfinaldatav8.csv", "a", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Yelp', 'sourcing_yelp', rest_name, tags_second, 'NA','Portugal',city,city_code,address,'NA','NA','NA',phone,ratings,reviews_second,'https://www.yelp.com',url,'NA','NA','NA'])

    temp1 = temp1 + 1
    print(temp1)
