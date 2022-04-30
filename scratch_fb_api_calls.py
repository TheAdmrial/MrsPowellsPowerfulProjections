# loading in libraries
#%%
from os import access
import requests
from datetime import datetime, timedelta
import facebook
import json
import pandas as pd

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
# app_id = '5044226898989028'
# secret_app_id = '4628fe4fbeb89a91f81b622b760d5e49'
# st_token = 'EABHrsph7DZBQBAOXC6TObaAui8xEVcZASpfEUXqeTP4ZA964cvTZCzMjU5vxTAJdTVkGHYFjBfGd8plkXBNjFPgZAeGvvZAv9yZClIAS5fvHdfgx2JZA1lbcMtkTy97FKtt4NEcXt0IRlZCtLIE8ZAWEETfo3FGkG46ZAbgqXQvR6KA467ZAaiAwfvZAXZBIR6edv3OVLk8s8FgUqxSQFYI44C0VH158vXGpJlOMgZD'



# response=requests.get('https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=' + app_id + '&client_secret=' + secret_app_id + '&fb_exchange_token=' + st_token)

# print(response.text)
#%%
# requesting access to Mrs. Powell's Ammon's page. 
lt_token = 'EABHrsph7DZBQBAKxgKEgLMws8H1EvexlzomYObz7xWn8sPt8DbxdMyuZAMTgMLBeFkQ6zbYItzFHzmm0FFOIaXsGUi7P0hydufvCa56y4IgxgC18eiGMiY1Qr13VZAmuTbzdZC4shUPeHaeCoAZCcgSj9owCs4kBTWHslMBpk4ooDcZBh2OSWz'
mrspowellsIF = 'mrspowells'

IFresponce = requests.get('https://graph.facebook.com/' + mrspowellsIF + '?fields=access_token&access_token=' + lt_token)

print(IFresponce.text)
#%%
mrspowellsREX = 'mrspowellsrexburg'

REXresponce = requests.get('https://graph.facebook.com/' + mrspowellsREX + '?fields=access_token&access_token=' + lt_token)

print(REXresponce.text)

#%%
mrspowellsRIG = 'mrspowellsrigby'

RIGresponce = requests.get('https://graph.facebook.com/' + mrspowellsRIG + '?fields=access_token&access_token=' + lt_token)

print(RIGresponce.text)
# %%
IFapikey = "EABHrsph7DZBQBAIGZBwsdIkpp9mcEd7aOtXEnNMd8McoBaALAFcXl89OPaPoSWgZAAZBRs4RORMXOqHzKKw2BxXja70vQWmCrKVoC49b2ujOVsmxC4KxHoPZBiMzJKLa5mZCEut9jhNEyaFa3EK2zjlE3cSyAoLbvH4kWaaZBocG3CNSNEFEwal1dmi1PMrSDEZD"
REXapikey = "EABHrsph7DZBQBAG0RsoAkGEIxbe9ZANs1OkYKY9hD0ZA8GjEudr6508dAXRDJbJHjPyt9NPjV03CoCnbdVOqG6REctiFhNF185UxVV7GnD8ZAcqzcivaZCjCXbkiIOgiG2lrJ68481oWkyh8ql1G7rUAuaJhXuKpGIZCAx9RNZC8yN34SZCln9iZAC9T58ubD66AZD"
RIGapikey = "EABHrsph7DZBQBANNuElLPE4rcrWGIxR05ojek1Eh5BnsB7GcgRZCb8ToK5OGsh2U9HQBoChX5l6qF03FMZCMvTlZCgHZB29W2vSoXRBktghRHwGzSskephkhNpJSTTvrQzEZAGQ1xiEsJJEuYPYAsEVMiPqa3BAAy3KrIozxgKG1fSK4TxB5yQAhYWVDPoXDkZD"

#%%
# trying to use the facebook sdk for python package to get post data from Mrs Powells
graph = facebook.GraphAPI(access_token = IFapikey)
page_name = "mrspowells"
fields = ['id','name', 'likes', 'posts']
fields = ','.join(fields)

page = graph.get_object(mrspowellsIF, fields = fields)
print(json.dumps(page, indent = 4))


# %%
if_post_dat = pd.DataFrame(page)
# %%
if_posts = if_post_dat.posts
# %%
