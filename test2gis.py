import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from datetime import datetime
import csv
import re
from selenium.common.exceptions import NoSuchElementException

rest_details = pd.read_excel('bucuresti_restaurants.xlsx', 'tazzdata')
total_rows = len(rest_details.index)

class Twogis:


    def getratings(self,a):
        try:
            rating = driver.find_element_by_class_name('_1n8h0vx')
        except NoSuchElementException:
            return False

        return rating.text

    def rest_name_and_tags(self,a):
        rest_tags = {}
        rest_name = ''
        tags = ''
        try:
            rest_name_and_tags = driver.find_elements_by_class_name('_oqoid')
            # print(rating.text)
            res_tag_count = 0

            for res_and_tag in rest_name_and_tags:
                if res_tag_count == 0:
                    rest_name = res_and_tag.text
                elif res_tag_count == 1:
                    tags = res_and_tag.text
                res_tag_count = res_tag_count + 1

        except NoSuchElementException:
            rest_tags = {'rest_name': rest_name, 'tags': tags}
            return rest_tags

        rest_tags = {'rest_name':rest_name,'tags':tags}

        return rest_tags

    def discount_details(self,a):
        try:
            discount_details = driver.find_element_by_class_name('_mr0ehty')
        except NoSuchElementException:
            return False

        return discount_details.text

    def advertising(self,a):
        try:
            ad = driver.find_element_by_class_name('_1q1z1sxo')
            ad = ad.get_attribute('title')
        except NoSuchElementException:
            return False
        return ad

    def rest_description(self,a):
        try:
            des = driver.find_element_by_class_name('_cp8dm8')
        except NoSuchElementException:
            return False
        return des.text

    def webandemail(self,a):
        website_and_email = {}
        website = ''
        email_id = ''
        try:
            timings = driver.find_elements_by_class_name('_49kxlr')
            emails_and_sites_count = 0
            for t in timings:
                if emails_and_sites_count == 4:
                    website = t.text.replace("\n", "").strip()
                elif emails_and_sites_count == 5:
                    email_id = t.text.replace("\n", "").strip()

                emails_and_sites_count = emails_and_sites_count + 1
        except NoSuchElementException:
            website_and_email = {'website': website, 'email': email_id}
            return website_and_email
        website_and_email = {'website': website, 'email': email_id}
        return website_and_email

    def fb_link(self,a):
        try:
            facebook_link = driver.find_element_by_css_selector('a._vhuumw[aria-label="Facebook"]')
            facebook_link = facebook_link.get_attribute('href')
        except NoSuchElementException:
            return False

        return facebook_link

    def insta_link(self,a):
        try:
            instagram_link = driver.find_element_by_css_selector('a._vhuumw[aria-label="Instagram"]')
            instagram_link = instagram_link.get_attribute('href')

        except NoSuchElementException:
            return False

        return instagram_link

    def phone_no(self,a):
        try:
            find_phone_number = driver.find_element_by_class_name('_b0ke8')
            phone_number = find_phone_number.find_element_by_tag_name('a')
            phone_number = phone_number.get_attribute('href')
            phone_number = phone_number.replace("tel:", "").strip()
        except NoSuchElementException:
            return False

        return phone_number

    def address(self,a):
        final_address = ''
        try:
            address = driver.find_elements_by_class_name('_er2xx9')
            add_count = 0
            for ad in address:
                if add_count == 0:
                    final_address = ad.text + ' '
                elif add_count == 1:
                    final_address = final_address + ad.text
                    break
                add_count = add_count + 1
        except NoSuchElementException:
            return False

        return final_address

    def getmenu(self,a):
        try:
           menu_link =  driver.find_elements_by_class_name('_ke2cp9k')
           res = ''
           for m in menu_link:
               res = m.get_attribute('href')
               menu_link_list = re.search('prices', res)
               if menu_link_list:
                   return res

        except NoSuchElementException:
            return False

        return False


    def getlistofitems(self,a):
        itemslist = []
        try:
            menu = menu_items_driver.find_elements_by_class_name('_1skpdhf')
            for m in menu:
                item = m.text.replace("\n", "-").strip()
                if item != '':
                    itemslist.append(item.split('-'))
        except NoSuchElementException:
            return False

        return itemslist


a = Twogis()
temp1 = 0
while temp1 < total_rows:
    rest_url = rest_details['URL'][temp1]
    driver = webdriver.Firefox()
    driver.implicitly_wait(50)
    driver.get(rest_url)

    rating = a.getratings('_1n8h0vx')
    rest_tag = a.rest_name_and_tags('_oqoid')
    disc_details = a.discount_details('_mr0ehty')
    ad = a.advertising('_1q1z1sxo')
    desc = a.rest_description('_cp8dm8')
    w_and_e = a.webandemail('_49kxlr')
    flink = a.fb_link('a._vhuumw[aria-label="Facebook"]')
    ilink = a.insta_link('a._vhuumw[aria-label="Instagram"]')
    phone = a.phone_no('_b0ke8')
    addre = a.address('_er2xx9')

    menu_link = a.getmenu('_ke2cp9k')

    # print(rest_tag['rest_name'])
    # print(rest_tag['tags'])
    # print(rating)
    # print(disc_details)
    # print(ad)
    # print(desc)
    # print(w_and_e['website'])
    # print(w_and_e['email'])
    # print(flink)
    # print(ilink)
    # print(phone)
    # print(addre)
    # print(menu_link)
    menu_list = ''
    if menu_link != False:
        menu_items_driver = webdriver.Firefox()
        menu_items_driver.implicitly_wait(50)
        menu_items_driver.get(menu_link)
        menu_list = a.getlistofitems('_1skpdhf')
        # print(menu_list[0][0])
        print(menu_list)
        k = 0
        while k < len(menu_list):
            print(menu_list[k][0])
            print(menu_list[k][1])
            with open("twogisfinaldatawithmenu.csv", "a", encoding="utf-8") as csvfile:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                writer = csv.writer(csvfile)
                writer.writerow(
                    [rest_tag['rest_name'],addre,rest_url,
                     menu_list[k][0],menu_list[k][1],k, dt_string, dt_string]
                )
            print('In the menu')
            k+=1

        menu_items_driver.close()



    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    with open("twogisfinaldata.csv", "a", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['2gis.ua', rest_tag['rest_name'], rest_tag['tags'], rating, desc, ad, disc_details,
             w_and_e['website'], w_and_e['email'], flink, ilink, phone, addre, dt_string, dt_string])
    print(temp1)
    temp1 = temp1 + 1

    driver.close()





