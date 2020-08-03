
from selenium import webdriver
import csv

driver = webdriver.Firefox()
driver.implicitly_wait(50)

driver.get("https://tazz.ro/bucuresti/categorie/toate/")

details = driver.find_element_by_class_name('restoList')

multiple_records = driver.find_elements_by_css_selector("div[itemprop='itemListElement']")

count = 1
for single_record in multiple_records:
    title = single_record.find_element_by_tag_name("h2")
    #    print(title.text)
    a = single_record.find_element_by_tag_name("a")
    link = a.get_attribute('href')
    ####Writing the restaurant details in the file
    with open("tazzdata.csv", "a",encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([count, title.text, link])
    count = count + 1

#    print(link)
#    print(single_record.text)
print('Its done')
driver.close()