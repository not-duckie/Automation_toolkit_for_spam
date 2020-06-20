#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = webdriver.Firefox('/home/duckie/Downloads/geckodriver/')
f.get('https://web.whatsapp.com/')
wait = input('Scan the QR Code')
all = f.find_elements_by_xpath("//span[@title]")
tmp = 3
for i in range(2):
    all[tmp].click()
    f.find_element_by_class_name('web').send_keys('This is test message' + Keys.ENTER + 'Do not reply' + Keys.ENTER + Keys.ENTER)
