from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



banner = '''
  _________                      ._____________ ____ ___ 
 /   _____/__________    _____   |   \\______   \\    |   \\
 \\_____  \\\\____ \\__  \\  /     \\  |   ||     ___/    |   /
 /        \\  |_> > __ \\|  Y Y  \\ |   ||    |   |    |  / 
/_______  /   __(____  /__|_|  / |___||____|   |______/  
        \\/|__|       \\/      \\/                          

'''
print (banner)
print ("by duckie ~ https://github.com/not-duckie/")

email_id = input('Enter your email id>')
print("No password is stored, chill UwU")
password_text = input("Enter your Password> ")

n = int(input('Enter the number of time you want to sent the mail> '))
print ("This script does some shady things to login into gmail ignore that please")


subject_text = 'Regarding Exams During the Corona Pandemic'


body_text = '''Respected Sir/Ma'am

This is test email to show the spam feature of the gmail.
 
'''


f = webdriver.Chrome()

#---------------------- Login  ----------------------------------------------#
f.get('https://app.storychief.io/login/google')

email = f.find_element_by_id('identifierId')
email.send_keys(email_id)

a = f.find_element_by_class_name('CwaK9')
a.click()

time.sleep(2)

password = f.find_element_by_name('password')
password.send_keys(password_text)

a = f.find_element_by_class_name('CwaK9')
a.click()

time.sleep(2)

if 'challenge/ootp' in f.current_url:
    print ("verify the 2 Factor Authentication")
    a = input('Press any key on compeletion >')


f.get('https://mail.google.com/mail/')

time.sleep(4)

for i in range(n):

    compose = f.find_element_by_class_name('z0')
    compose.click()

    time.sleep(4)

    to = f.find_element_by_name('to')
    to.send_keys('sarthakmisraa@gmail.com')

    time.sleep(2)
    
    subject = f.find_element_by_name('subjectbox')
    subject.send_keys(subject_text + Keys.TAB + body_text)
    f.find_element_by_name('subjectbox').send_keys(Keys.CONTROL + Keys.ENTER)



print ("All Done !")
print ("Your Contribution is Appreciated")

