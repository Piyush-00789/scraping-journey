import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import pandas as pd
from datetime import datetime
import csv

rest_details = pd.read_excel('bucuresti_restaurants.xlsx', 'tazzdata')
# print(df)
# tazzdata = pd.read_excel('tazzread.xlsx', 'Sheet1')

total_rows = len(rest_details.index)
# tazz_rows = len(tazzdata.index)
temp1 = 0

while temp1 < total_rows:
    rest_url = rest_details['URL'][temp1]
    driver = webdriver.Firefox()
    driver.implicitly_wait(50)
    # url = 'https://2gis.ua/kiev/firm/70000001020866204'
    driver.get(rest_url)
    try:
        rating =driver.find_element_by_class_name('_1n8h0vx')
        rest_name_and_tags = driver.find_elements_by_class_name('_oqoid')
        # print(rating.text)
        res_tag_count = 0
        rest_name = ''
        tags = ''
        for res_and_tag in rest_name_and_tags:
            if res_tag_count == 0 :
                rest_name = res_and_tag.text
            elif res_tag_count == 1:
                tags = res_and_tag.text
            res_tag_count = res_tag_count + 1


        discount_details = driver.find_element_by_class_name('_mr0ehty')
        advertising = driver.find_element_by_class_name('_1q1z1sxo')
        advertising = advertising.get_attribute('title')
        # print(advertising)
        # print(discount_details.text)
        rest_description = driver.find_element_by_class_name('_cp8dm8')
        # print(rest_description.text)
        # contact_details = driver.find_elements_by_class_name('_15t9xwf')

        # contact_details_count = 0
        # for add in contact_details:
        #     print('')
        #     # print(add.text.replace("\n","").strip())


        timings = driver.find_elements_by_class_name('_49kxlr')
        emails_and_sites_count = 0
        website = ''
        email_id = ''
        for t in timings:
            if emails_and_sites_count == 4:
                website = t.text.replace("\n","").strip()
            elif emails_and_sites_count ==5:
                email = t.text.replace("\n","").strip()

            emails_and_sites_count = emails_and_sites_count + 1

        facebook_link = driver.find_element_by_css_selector('a._vhuumw[aria-label="Facebook"]')
        facebook_link = facebook_link.get_attribute('href')
        instagram_link = driver.find_element_by_css_selector('a._vhuumw[aria-label="Instagram"]')
        instagram_link = instagram_link.get_attribute('href')
        find_phone_number = driver.find_element_by_class_name('_b0ke8')

        phone_number = find_phone_number.find_element_by_tag_name('a')
        phone_number = phone_number.get_attribute('href')
        phone_number = phone_number.replace("tel:","").strip()


        address = driver.find_elements_by_class_name('_er2xx9')
        final_address = ''
        add_count = 0
        for ad in address:
            if add_count == 0:
                final_address = ad.text + ' '
            elif add_count == 1 :
                final_address = final_address + ad.text
                break
            add_count = add_count + 1
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        with open("tazzfinaldata.csv", "a", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['2gis.ua',rest_name,tags,rating.text,rest_description.text,advertising,discount_details.text,website,email,facebook_link,instagram_link,phone_number,final_address,dt_string,dt_string])
        print(temp1)
        temp1 = temp1 + 1
    except Exception as e:
        temp1 = temp1 + 1
        continue


    driver.close()



