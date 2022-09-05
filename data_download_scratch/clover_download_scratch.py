#%%
# import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from dotenv import load_dotenv
import os
from time import sleep
# calling hidden variables
load_dotenv()
email = os.getenv('clover_email')
password = os.getenv('clover_password')
dwnld = os.getenv('path_to_data')
#%%
print(email)

#%%
# create webdriver object
service = Service(executable_path='C:/WebDriver/chromedriver.exe')
driver = webdriver.Chrome(service =service)
#%%
# going to clover.com login dashboard
driver.get('https://www.clover.com/dashboard/login')
sleep(7)
# looking at the email textbox
email_textbox = driver.find_element(by = 'id', value = 'email-input')
# type in email
email_textbox.send_keys(email)
sleep(4)
# find the password textbox
password_textbox = driver.find_element(by = 'id', value = 'password-input')
# type in password
password_textbox.send_keys(password)
sleep(4)
# find the login button
login_button = driver.find_element(by = 'id', value = 'log-in')
# click the login button
login_button.click()
sleep(15)

# %%
# navigating to the financial data

# things to remember:
# 1) there are three stores to pull data from
# 2) pull financial data from January 01, 2020 to March 31, 2022
# 3) test loops a couple of times before just letting it run
# 4) find a way to dynamically change the downloading file path
# 5) Don't forget the sleeps!! 