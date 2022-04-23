#starting out learning to scrap with beautiful soup
from bs4 import BeautifulSoup
import requests

'''
The following code is a tutorial from geeksforgeeks.com. 
Link to the article: https://www.geeksforgeeks.org/python-web-scraping-tutorial/
'''

# make a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# chech status code for response received
# success code - 200

print(r)

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# Getting the title tag
print(soup.title)

# Getting the namt of the tag
print(soup.title.name)

# Getting the name of the parent tag
print(soup.title.parent.name)

# use the child attribute to get
# the name of the child tag

s = soup.find('div', class_ = 'entry-content')
content = s.find_all('p')

print(content)