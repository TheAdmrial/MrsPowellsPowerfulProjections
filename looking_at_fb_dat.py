#%%
import pandas as pd 
import numpy as np
import plotnine as pn
import os

#%%
path =os.getcwd()
path = path+'/data/fb_data_test.csv'

#%%
dat = pd.read_csv(path, skiprows=0)
#%%
dat.describe()
# %%
dat.info()
#%%
# looking at the posted column
dat.Posted.head(5)