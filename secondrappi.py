from selenium import webdriver
import csv
import re
import time
import pandas as pd
from datetime import datetime

class Rappi:

    def closeButton(self):
        try:
            driver.execute_script("document.getElementsByClassName('iconf-modal-close')[0].click()")
        except Exception as e:
            print(e)

    def findTags(self):
        try:
            tags_array = []
            content = driver.find_element_by_class_name('content-container')
            tags = content.find_elements_by_tag_name('li')
            for tag in tags:
                tags_array.append(tag.text)

        except Exception as e:
            print(e)
            return 'no tags'

        return tags_array

    def eta(self):
        try:
            content = driver.find_element_by_class_name('eta-container')
            estimation = content.find_element_by_tag_name('span')
        except Exception as e:
            print(e)
            return 'no eta'

        return estimation.text

    def delivery(self):
        try:
            price = driver.find_element_by_class_name('delivery_price')
        except Exception as e:
            print(e)
            return 0
        return price.text

    def findRating(self):
        try:
            rating_content = driver.find_element_by_class_name('rating-container')
            ratings = rating_content.find_element_by_tag_name('span')
        except Exception as e:
            print(e)
            return 'no rating'

        return ratings.text




##Reading the data from the excel sheet
rest_details = pd.read_excel('bucuresti_restaurants.xlsx', 'tazzdata')

obj  = Rappi()
total_rows = len(rest_details.index)
temp1 = 520

while temp1 < total_rows:
    rest_url = rest_details['URL'][temp1]
    driver = webdriver.Firefox()
    driver.implicitly_wait(50)
    driver.get(rest_url)
    obj.closeButton()


    tags = obj.findTags()
    estimation_time = obj.eta()
    price = obj.delivery()
    rating = obj.findRating()
    length = len(tags)
    if(temp1 < 41):
        city = 'Tucumán'
        city_code = 'TUC'
        country = 'Argentina'
        country_code = 'AR'
        competitor = 'Rappi'
    if temp1 >=41 and temp1 < 481:
        city = 'Lima'
        city_code = 'LIM'
        country = 'Peru'
        country_code = 'PE'
        competitor = 'Rappi'

    if temp1 >= 481 and temp1 < 521:
        city = 'Cusco'
        city_code = 'CUZ'
        country = 'Peru'
        country_code = 'PE'
        competitor = 'Rappi'

    if temp1 >= 521 and temp1 < 629:
        city = 'Trujillo'
        city_code = 'TRU'
        country = 'Peru'
        country_code = 'PE'
        competitor = 'Rappi'

    if temp1 >= 629 and temp1 < 709:
        city = 'Piura'
        city_code = 'PIU'
        country = 'Peru'
        country_code = 'PE'
        competitor = 'Rappi'

    if temp1 >= 709 and temp1 < 720:
        city = 'Punta Hermosa'
        city_code = 'LMS'
        country = 'Peru'
        country_code = 'PE'
        competitor = 'Rappi'





    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)


    with open("rappiwritenew.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if(length == 1):
            writer.writerow([rest_details['Restaurant Name'][temp1], tags[0],'null','null', price, estimation_time, rating, city, city_code,
                         country,country_code,competitor, dt_string, dt_string])
        if(length == 2):
            writer.writerow(
                [rest_details['Restaurant Name'][temp1], tags[0], tags[1], 'null', price, estimation_time, rating, city,
                 city_code,
                 country, country_code, competitor, dt_string, dt_string])
        if (length == 3):
            writer.writerow(
                [rest_details['Restaurant Name'][temp1], tags[0], tags[1], tags[2], price, estimation_time, rating, city,
                 city_code,
                 country, country_code, competitor, dt_string, dt_string])

    print(temp1)
    temp1 = temp1 + 1

    driver.close()
# time.sleep(10)



