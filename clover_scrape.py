#%%
# loading in libraries
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

#%%

'''
The  following is an example of a dataframe that I would like to fill with 
scraped data from clover.
'''
data = {
    'Time Stamp':['12-12-2020 12:15:00', '12-12-2020 12:15:00','12-12-2020 12:15:00'],
    'Customer ID':['225874','789065','582140'],
    'Order ID':['BAGT8547L','THER8547U','ZYTR8974N'],
    'Line Item':['Original Cinnamon Roll', 'Mini Cinnamon Roll', 'Caramel Cinnamon Roll'],
    'Line Item Price':[4.99, 3.99,4.50],
    'Store Location':['IF', 'Rexburg', 'Rigby']
}

# creating the dataframe
df_ex = pd.DataFrame(data)

# print the output
print(df_ex)
# %%
'''
This webscraper will be built with:
- selenium to navigate the web, 
- BeautifulSoup to find and pull the information out of the html 
- sleep will be used intermitently so as to not overload clover's servers and be banned from the site
- pandas, to work with the data in a tabular format
'''