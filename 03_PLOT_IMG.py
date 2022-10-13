import pandas as pd, numpy as np, glob, datetime

import os, math
import pandas as pd, glob, numpy as np
import matplotlib.pyplot as plt

data_list = glob.glob('../02_POINT_DATA/*.csv')


def plot_ts_all(in_df, site_nm):
  
    fig, axs = plt.subplots(6,5,figsize=(25,30))
    fig.suptitle('Series')
    
    j, k = 0, 0
    for i in range(1, len(in_df.columns)+1):
        axs[k, j].plot(in_df[in_df.columns[i-1]].values)
        axs[k, j].set_title(in_df.columns[i-1])        
        
        j += 1
        if i % 5 == 0:
            j = 0; k += 1
            
    # plt.show()
    plt.savefig('../04_IMG_POINT_VARS/%s.png'%site_nm)
    plt.close()


for path in data_list:
    site_nm = path.split('\\')[-1].split('.')[0]
    data = pd.read_csv(path, parse_dates=['Date'], index_col=0).dropna(axis=0)
    plot_ts_all(data, site_nm=site_nm)    