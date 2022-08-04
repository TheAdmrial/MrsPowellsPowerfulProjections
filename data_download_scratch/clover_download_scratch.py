# import webdriver 
from selenium import webdriver
# import opotions

# create webdriver object
driver = webdriver.Chrome()

# going to clover.com login dashboard
driver.get('https://www.clover.com/dashboard/login')

# looking at the email textbox
