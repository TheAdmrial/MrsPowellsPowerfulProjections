#%%
import pandas as pd
import numpy as np
import plotnine as pn
import os

#%%
os.getcwd()
#%%
# reading in data
dat = pd.read_csv('../data/clover_transactions_test.csv')

dat.info()

#%%
# listing the columns that I want to keep
list_keep_cols = ['Order Date'
,'Order ID'
, 'Tax Amount'
, 'Tip'
, 'Discount'
, 'Order Total'
, 'Payments Total'
, 'Tender']

dat1 = dat.filter(items = list_keep_cols, axis = 1)

dat1.info()

dat1.head(6)

#%%
## cleaning up the order date column
# remove the time at the end
# for i in range(len(dat1['Order Date'])):
#     dat1['Order Date'].str.split(pat = ' ', n = 1)[i].pop(0)

# cut off the AM MDT at the end of the string
# dat1['Order Date'].str.replace(pat = ' \D+', repl = '', regex=True)

# convert into date data type
# for i in range(len(dat['Order Date'])):
dat1['Order Date'] =pd.to_datetime(dat1['Order Date'], format = '%d-%b-%Y', exact = False)

dat1.head(15)
#%%
dat1.shape
#looking at the dataset
dat1.head(15)

#%%
# aggregate the total revenue per day
dat2 = dat1.groupby(['Order Date']).agg(
    count = ('Order ID', 'size'), # aggregate the total number of sales per day
    total_sales = ('Payments Total', np.sum), # aggregate the total revenue per day
    total_taxes = ('Tax Amount', np.sum),
    total_tips = ('Tip', np.sum)
).reset_index()

dat2