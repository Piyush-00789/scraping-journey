from selenium import webdriver
import csv
import re
import time

class Rappi:

    def closeButton(self):
        try:
            driver.execute_script("document.getElementsByClassName('close-btn')[0].click()")
        except Exception as e:
            print(e)

    def clickSeeMoreButton(self):
        try:
            for x in range(0,200):
                driver.execute_script("document.getElementsByClassName('button-loading-search')[0].click()")
        except Exception as e:
                print('hey')
                print(e)




alllocationlinks = [


#done
# 'https://www.rappi.com.ar/buenos-aires/restaurantes',
# 'https://www.rappi.com.ar/cordoba/restaurantes',
# 'https://www.rappi.com.ar/la-plata/restaurantes',
# 'https://www.rappi.com.ar/rosario/restaurantes',
# 'https://www.rappi.com.pe/chiclayo/restaurantes',
# 'https://www.rappi.com.pe/lima/restaurantes',
# 'https://www.rappi.com.ar/san-miguel-de-tucuman/restaurantes',\
# 'https://www.rappi.com.pe/arequipa/restaurantes',


# 'https://www.rappi.com.pe/cusco/restaurantes',


# 'https://www.rappi.com.pe/trujillo/restaurantes',

# 'https://www.rappi.com.pe/piura/restaurantes',








#not done
# 'https://www.rappi.com.ar/neuquen/restaurantes',
# 'https://www.rappi.com.ar/carilo-pinamar/restaurantes',
# 'https://www.rappi.com.ar/quilmes/restaurantes',
# 'https://www.rappi.com.ar/santafe/restaurantes',
# 'https://www.rappi.com.ar/mendoza/restaurantes',
# 'https://www.rappi.com.pe/asia/restaurantes',


]

count = 0
for link in alllocationlinks:
    obj = Rappi()
    driver = webdriver.Firefox()
    driver.implicitly_wait(50)
    driver.get(link)
    obj.closeButton()
    result = obj.clickSeeMoreButton()




    time.sleep(50)

    try:
        cards_info = driver.find_elements_by_class_name('store-item-box')

        i = 0
        temp = 0
        for card in cards_info:
            i = i + 1
            a = card.find_element_by_tag_name("a")
            link = a.get_attribute('href')
            rest_name = card.find_element_by_class_name('store-name')
            with open("rappihotelinkssalta.csv", "a", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([count, rest_name.text, link])
            temp = temp + 1
            print(temp)
    except Exception as e:
        continue

    count = count + 1
    print(count)
    driver.close()


