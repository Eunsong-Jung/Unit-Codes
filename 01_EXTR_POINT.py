import pandas as pd, numpy as np

data = pd.read_excel('../01_RAW_DATA/Collected.xlsx', index_col=0)

for site in set(data.Site):
    site_df = data[data.Site == site]
    site_df = site_df.set_index(site_df['Date'])
    
    cols=[]
    for col in site_df.columns:
        if 'Date' not in col and 'Site' not in col:
            cols.append(col)
    site_df = site_df[cols]
    site_df.to_csv('../02_POINT_DATA/%s.csv'%site, index=True)