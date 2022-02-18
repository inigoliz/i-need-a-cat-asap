from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import re

file_dir = os.path.dirname(os.path.abspath(__file__))

service = Service(file_dir + '/chromedriver')
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, service=service)

#url = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=16&field_gender_value=All&field_cat_age_name_tid=All'
url = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=17&field_gender_value=All&field_cat_age_name_tid=All'
driver.get(url)

print(driver.find_element(By.XPATH, '//div[@class="view-footer"]').text)
cats = driver.find_elements(By.XPATH, '//div[@class="view-content-info"]')

for cat in cats:
    cat_info = cat.get_attribute('innerHTML')
    print(re.findall(r'"(.*?[^\\])"', cat_info))  # gets the content inside quotes
