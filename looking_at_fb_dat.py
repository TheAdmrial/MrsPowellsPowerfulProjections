#%%
import pandas as pd 
import numpy as np
import plotnine as pn
import os

#%%
path =os.getcwd()
path = path+'/data/fb_data_test.csv'

#%%
dat = pd.read_csv(path)
#%%
# making a data dictionary for the lifetime data columns
dd_cols = dat.columns

# this grabs the columns and the first row
dd_defs = dat.iloc[0,8:52]

# trying to make a dictionary for the column definitions 
# dd_fb_dat = pd.DataFrame([dd_cols,dd_defs])
# dd_fb_dat = dd_fb_dat.melt(id_vars = [], var_name = "cols", value_name="defs")
# %%
dat.info()
#%%
# looking at the posted column
dat.Posted.head(5)