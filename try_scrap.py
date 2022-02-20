from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import sys
import re

import smtplib, ssl

def send_email(new_cats):
    port = 465  # For SSL
    sender_email = "ineedacatasap@gmail.com"
    with open('password.txt', 'r') as f:
        password = f.read().splitlines()[0]
    smtp_server = "smtp.gmail.com"
    receiver_email = "inigoliz@gmail.com"  # Enter receiver address

    candidates = ', '.join(new_cats)


    email = """\
    Subject: Be fast!

    New kities ({}), are waiting for you!
    Check out the website here: https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=16&field_gender_value=All&field_cat_age_name_tid=All.""".format(candidates)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email)


def save(names):
    with open('cats_available.txt', 'w') as f:
        for name in names:
            f.write("%s\n" % name)

def read():
    with open('cats_available.txt', 'r') as f:
        lines = f.read().splitlines()
    return lines

def new_cats_in_shelter():
    now = set(get_cats_on_website())
    before = set(read())
    #save(now)
    return now - before

def get_cats_on_website():
    service = Service(file_dir + '/chromedriver')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, service=service)

    url = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=16&field_gender_value=All&field_cat_age_name_tid=All'
    #url = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=17&field_gender_value=All&field_cat_age_name_tid=All'
    driver.get(url)

    #print(driver.find_element(By.XPATH, '//div[@class="view-footer"]').text)
    cats = driver.find_elements(By.XPATH, '//div[@class="view-content-info"]')

    cat_names = []
    for cat in cats:
        cat_info = cat.get_attribute('innerHTML')
        cat_names.append(re.findall(r'"\/(.*?[^\\])"', cat_info)[0])  # gets the content inside quotes

    #return cat_names
    return ['jones', 'victoria', 'area']

def main():
    global file_dir
    file_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_dir)

    new_cats = new_cats_in_shelter()

    if len(new_cats):
        send_email(new_cats)
        print(new_cats)
    else:
        sys.exit()

main()
