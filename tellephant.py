from selenium import webdriver
import csv
import re
import time
import pandas as pd
from datetime import datetime

rest_url = "https://beta.tellephant.com/login"
driver = webdriver.Firefox()
driver.implicitly_wait(50)
driver.get(rest_url)


driver.close()
