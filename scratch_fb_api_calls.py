# loading in libraries
#%%
import requests
from datetime import datetime, timedelta
import facebook
import json
import pandas as pd
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import os
from dotenv import load_dotenv
import time

#%%
'''
So while trying to get access to my mom's facebook posts data, I was blocked from
using Facebook. I applied to have my account reinstated so we'll see if I can even
try this route. 

I'll check back in a couple of days to see if there has been any movement. 
'''

#%%
'''
This code chunk has an api code that has already expired
'''
# making a get request
# app_id = ''
# secret_app_id = ''
# st_token = ''



# response=requests.get('https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=' + app_id + '&client_secret=' + secret_app_id + '&fb_exchange_token=' + st_token)

# print(response.text)
#%%
# getting api keys into the working environment 
load_dotenv()
lt_token = os.getenv('lt_token')

IFapikey = os.environ.get('if_api_key')
REXapikey = os.getenv('rex_api_key')
RIGapikey = os.getenv('rig_api_key')

mrspowellsIF = os.getenv('mrs_powells_if_id')
mrspowellsREX = os.getenv('mrs_powells_rex_id')
mrspowellsRIG = os.getenv('mrs_powells_rig_id')

#%%
base_url = 'https://graph.facebook.com/'

comment_id ='119294611448224_5312435448800755'
fields_url ='?fields=id,created_time,message,comments{comment_count,id,user_likes},likes'

#%%
comment_response = requests.get(base_url + mrspowellsIF + '/' + comment_id + fields_url)

print(comment_response.text)
#%%
IFresponce = requests.get('https://graph.facebook.com/' + mrspowellsIF + '?fields=access_token&access_token=' + lt_token)

print(IFresponce.text)
#%%


REXresponce = requests.get('https://graph.facebook.com/' + mrspowellsREX + '?fields=access_token&access_token=' + lt_token)

print(REXresponce.text)

#%%

RIGresponce = requests.get('https://graph.facebook.com/' + mrspowellsRIG + '?fields=access_token&access_token=' + lt_token)

print(RIGresponce.text)
#%%
'''
This chunk is ment to send a url to make an api call to facebook. 
I will be building a while loop for in the next couple of code chunks 
'''

res = requests.get("https://graph.facebook.com/v13.0/"+ mrspowellsIF +"?fields=engagement%2Cfan_count%2Cfollowers_count%2Cid%2Cposts%7Bid%2Cmessage%2Ccomments%7Bcomment_count%2Cid%2Clikes%7Bid%7D%2Ccreated_time%7D%2Clikes%7Bid%7D%2Ccreated_time%7D&access_token=" + IFapikey)

#%%
res1 = dict(res.json())
print(res1)
#%%
# selecting the post data
res1['posts']['data']

#%%
# pulling out the paging link
page_link = res1['posts']['paging']['next']

#%%
res2=requests.get(page_link)
#%%
res2 = dict(res2.json())
#%%
# this pulls out the next page link
next_page = res2['paging']['next']
#%%
# this uses the next page link in a new get request
res3 = requests.get(next_page)
#%%
res3 = dict(res3.json())
#%%
res3['paging']['next']
#%%
# trying to use the facebook sdk for python package to get post data from Mrs Powells
graph = facebook.GraphAPI(access_token = IFapikey)
fields = ['id','name', 'followers_count', 'posts']
fields = ','.join(fields)

page = graph.get_object(mrspowellsIF, fields = fields)
print(json.dumps(page, indent = 4))
#%%
# finding the post id
page['posts']['data'][0]['id']
# finging the next page
next_page=page['posts']['paging']['next']
#%%
# if_post_dat = pd.read_json(page)
if_dat = pd.json_normalize(page)
post_dat= pd.DataFrame(if_dat['posts.data'][0])
post_dat.head()
#%%
'''
I am able to get all the posts and post id's for the last year for the Mrs.
Powell's. Next I need to make a data set of that info and loop through the id's 
in the facebook api to grab the likes, comments and shares.  
'''
#%%
post_dat.id[0]
#%%
'''
This will be my first attempt at getting the all the posts (for the last year)
for the store in IF. 
1) I will be using a while loop to continue until the 'next' is blank. 
2) for each page, I will be concating together the data that is grabbed 
from the api and adding that to the bottom of the data set
3) I will add sleeps to that there are not too many api calls per second. 
'''
#%%
loops = 0
while next_page != '':
    page1=graph.get_object(mrspowellsIF, page = next_page, fields = fields)
    print('made a call to facebook')
    print()
    next_page=page['posts']['paging']['next']
    if_posts=pd.json_normalize(page1)
    post_dat1=pd.DataFrame(if_posts['posts.data'][0])
    if_post_dat=pd.concat([post_dat, post_dat1])
    loops += 1
    print('just added the new data to the old data')
    print(f'times through: {loops}')
    time.sleep(15)
#%%
if_post_dat.tail()
# %%
