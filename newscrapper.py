
from selenium import webdriver
import csv
import re
from selenium.common.exceptions import NoSuchElementException

class Tazztags:

    def getTags(self,count):
        try:
            tags = driver.find_elements_by_class_name('store-description')
            i = 0
            for tag in tags:
                if(i == count):
                    tag_name = tag.text

        except NoSuchElementException:
            return False



driver = webdriver.Firefox()
driver.implicitly_wait(50)


driver.get("https://tazz.ro/roman/restaurante")

details = driver.find_elements_by_class_name('store-card')

multiple_records = driver.find_elements_by_class_name("store-card-info-small")

tags = driver.find_elements_by_class_name('store-description')

obj = Tazztags()

count = 1
temp = 0
sep = '•'
for single_record,tag in zip(multiple_records,tags):
    title = single_record.find_element_by_class_name("store-name")
    # print(title.text)
    a = single_record.find_element_by_tag_name("a")
    link = a.get_attribute('href')
    # print(link)
    tag_name = tag.text
    stripped_tagname = tag_name.split(sep,1)[0]
    # tag = obj.getTags(temp)
    # print(tag)
    ####Writing the restaurant details in the file
    with open("tazzdatanewjan2.csv", "a",encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([count, title.text, link,stripped_tagname])
    count = count + 1
    temp = temp + 1
    print(temp)

#    print(link)
#    print(single_record.text)
print('Its done')
driver.close()