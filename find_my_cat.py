from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import smtplib
from email.message import EmailMessage
import ssl
import yaml

import os
import sys
import re


def send_email(new_cats, url, flat_cat):

    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)

    msg = EmailMessage()
    msg['From'] = config['sender_email']
    msg['To'] = config['receiver_mail']
    if flat_cat:
        msg['Subject'] = 'New FLAT cats!'
    else:
        msg['Subject'] = 'New (non-flat) cats!'
    msg.set_content("""\
    New kities ({}) are waiting to be adopted by YOU!
    Check out the website here:
    {}.
    Be fast!""".format(new_cats, url))

    password = config['password']

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(config['sender_email'], password)
        server.send_message(msg)

    # if flat_cat:
    #     msg['To'] = config['receiver_mail2']
    #     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #         server.login(config['sender_email'], password)
    #         server.send_message(msg)


def save(names, memory_file):
    with open(memory_file, 'w') as f:
        for name in names:
            f.write("%s\n" % name)


def initiate_chrome():
    is_RPi = False

    if "pi" in file_dir:
        is_RPi = True
    else:
        is_RPi = False

    #print(f'Executing on RapsberryPi = {is_RPi}')

    if is_RPi:
        service = Service('/usr/lib/chromium-browser/chromedriver')
    else:
        service = Service(file_dir + '/drivers/chromedriver_mac97')

    options = Options()
    options.headless = True
    return webdriver.Chrome(options=options, service=service)


def read(file):
    if not os.path.isfile(file):
        open(file, 'w')
    with open(file, 'r') as f:
        list_contents = f.read().splitlines()
    return list_contents


def get_cats_on_website(url):

    driver = initiate_chrome()
    driver.get(url)
    cats = driver.find_elements(By.XPATH, '//div[@class="view-content-info"]')

    cat_names = []
    for cat in cats:
        cat_info = cat.get_attribute('innerHTML')
        # gets the content inside quotes
        cat_names.append(re.findall(r'"\/(.*?[^\\])"', cat_info)[0])

    return cat_names


def new_cats_in_shelter(memory_file, url):
    now = set(get_cats_on_website(url))
    before = set(read(memory_file))
    save(now, memory_file)

    new_cats = now - before
    new_cats = [cat.capitalize() for cat in new_cats]
    new_cats = ', '.join(new_cats)

    return new_cats


def check_and_notify_me(memory_file, url, flat_cat=False):
    new_cats = new_cats_in_shelter(memory_file, url)

    if len(new_cats):
        send_email(new_cats, url, flat_cat)
        print(new_cats)


def main():
    url_flat = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=16&field_gender_value=All&field_cat_age_name_tid=All'
    url_all = 'https://kattens-vaern.dk/adoption?field_internat_tid=All&field_race_tid=All&field_environment_tid=17&field_gender_value=All&field_cat_age_name_tid=All'

    global file_dir
    file_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_dir)

    check_and_notify_me('cats_available_all.txt', url_all)

    check_and_notify_me('cats_available_flat.txt', url_flat, flat_cat=True)


if __name__ == "__main__":
    main()
