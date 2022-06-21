#%%
# loading in libraries
import requests
from datetime import datetime, timedelta
#%%
'''
The following is an attempt to make an api call to download files from clover. 
'''
#%%
# merchant ids for the api call
rexburg_merchant_id = 'TZBFHX2XKNTB1'
rigby_merchant_id = 'VDWQ3W4K16FP1'
if_merchant_id = 'D4PHF3VM5N26P'
#%%
# asking for the correct data



# the api request
url = "https://api.clover.com/v3/merchants/" + if_merchant_id + "/exports"

start_time = (datetime.utcnow() - timedelta(hours = 16)).strftime("%H:%M:%S")
end_time = datetime.utcnow().strftime("%H:%M:%S")

headers = {
    "type": "PAYMENTS",
    "startTime": start_time,
    "endTime": end_time
}

response = requests.get(url, headers=headers)

print(response.text)

'''
- The message that I got back was a "401 Unauthorized" error. 
- Next, I'll try getting a Auth key and try the same request. 
- Just submitted my application so I can try and get an Auth key. 
- 4/23/2022 - No account verification yet. 


- I will be looking at the webscrape route while I wait...
- I can scrape individual orders and get line items with times and totals. 
    looks like I'll have my work cut out for me to scraping data off of
    clover's website. 
- One thing that I'll have to figure out is how to change the tab and go
    back to the other tab that I was working in. 
'''