#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


f = webdriver.Firefox('/home/duckie/Downloads/geckodriver/')
f.get('https://web.whatsapp.com/')
username = 'Papa'
wait = input('Scan the QR code')
f.find_element_by_xpath('//*[@title="{}"]'.format(username)).click()

for i in range(200):
    f.find_element_by_class_name('web').send_keys('Hello' + Keys.ENTER + Keys.ENTER)

