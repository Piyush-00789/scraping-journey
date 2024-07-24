import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException




i = 10
while i <= 10:

	driver = webdriver.Firefox()
	driver.implicitly_wait(50)
	j = str(6)


	details = driver.get('https://2gis.ua/kiev/search/%D0%9F%D0%BE%D0%B5%D1%81%D1%82%D1%8C')


	# driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/div[1]/a[5]')
	#
	# search = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/div[1]/a[2]')
	# search.click()
	# driver.implicitly_wait(50)

	# full_details = driver.find_elements_by_class_name('_1h3cgic')
	#
	# patterns= ['[^!.?]+']
	# count = 0
	# for full_detail in full_details:
	# 	link = full_detail.find_element_by_tag_name('a')
	# 	url = link.get_attribute('href')
	# 	print(url)
	# 	print(full_detail.text)
	search2  = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/div[1]/a[5]')

	search2.click()

	# driver.implicitly_wait(50)
	full_details = driver.find_elements_by_class_name('_1h3cgic')

	patterns= ['[^!.?]+']
	count = 0
	for full_detail in full_details:
		link = full_detail.find_element_by_tag_name('a')
		url = link.get_attribute('href')
		print(url)
		print(full_detail.text)



	# full_details = driver.find_elements_by_class_name('_1h3cgic')
	#
	# patterns= ['[^!.?]+']
	# count = 0
	# for full_detail in full_details:
	# 	link = full_detail.find_element_by_tag_name('a')
	# 	url = link.get_attribute('href')
	# 	print(url)
	# 	print(full_detail.text)
		# with open("2gis.csv", "a", encoding="utf-8") as csvfile:
		# 	writer = csv.writer(csvfile)
		# 	writer.writerow([full_detail.text,url])
		# 	count = count + 1
		# 	print(count)

	i+=1

	# driver.close()
