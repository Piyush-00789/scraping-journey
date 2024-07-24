import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import csv

count = 0
with open('newrestiwthopenhour.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = row[0]
        timings = row[2]
 #working#####

        try:
            url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+'restaurants'+"%20singapore&inputtype=textquery&fields=formatted_address,name,rating,opening_hours,geometry,user_ratings_total,place_id,type&key=AIzaSyB2Di7mgE-_rAwSfD__V6I98rLGuVyP6y0"
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')


            res = json.loads(str(soup))

            print(res)
            address = res['candidates'][0]['formatted_address']
            res_name = name
            google_id = res['candidates'][0]['place_id']
            google_reviews = res['candidates'][0]['rating']
            google_grade = res['candidates'][0]['user_ratings_total']

            lat = res['candidates'][0]['geometry']['location']['lat']
            lng = res['candidates'][0]['geometry']['location']['lng']


            remaining_tags = ''
            tags_limit = len(res['candidates'][0]['types'])

            for i in range(tags_limit):
                if(i==0):
                    business_unit = res['candidates'][0]['types'][i]
                else:
                    remaining_tags = remaining_tags + res['candidates'][0]['types'][i]
                if(i>=1) and (i<tags_limit-1):
                    remaining_tags = remaining_tags + ','

            ##########


            url_after_place_id = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='+google_id+'&fields=&key=AIzaSyB2Di7mgE-_rAwSfD__V6I98rLGuVyP6y0'
            response_content = requests.get(url_after_place_id)
            last_details = BeautifulSoup(response_content.content,'html.parser')
            remaining_details = json.loads(str(last_details))
            phone = remaining_details['result']['international_phone_number']
            google_maps_url = remaining_details['result']['url']

            city_name = 'București'
            country = 'Romania'
            last_element = len(remaining_details['result']['address_components'])
            last_element = last_element - 1
            city_code = 'BUC'
            competitor = 'Tazz'
            # datetime object containing current date and time
            now = datetime.now()
            # dd/mm/YY H:M:S
            created_at = now.strftime("%d/%m/%Y %H:%M:%S")

            with open("googleresults.csv", "a", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([res_name, business_unit,remaining_tags,competitor,timings,city_code,city_name,address,country,lat,lng,google_id,google_reviews,google_grade,google_maps_url,phone,created_at,created_at])
                count = count + 1
                print(count)

        except Exception as e:
            print(e)
        continue
