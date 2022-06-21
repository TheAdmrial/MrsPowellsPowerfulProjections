#%%
import pandas as pd
#%%
def create_date_table(start='2000-01-01', end='2050-12-31'):
    df = pd.DataFrame({"Date": pd.date_range(start, end)})
    df["Day"] = df.Date.dt.dayofweek
    df["Week"] = df.Date.dt.weekofyear
    df["Quarter"] = df.Date.dt.quarter
    df["Year"] = df.Date.dt.year
    return df
#%%
cal_dat = create_date_table(start = '2020-01-01', end = '2022-03-31')