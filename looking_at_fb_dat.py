#%%
import pandas as pd 
import numpy as np
import plotnine as pn
import os

#%%
path =os.getcwd()
path = path+'/data/fb_test_dat.xlsx'

#%%
# dat = pd.read_csv(path)
# reading in the .xls file from facebook
dat = pd.read_excel(path, sheet_name=0, header = 0, skiprows= lambda x:x in[1])
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