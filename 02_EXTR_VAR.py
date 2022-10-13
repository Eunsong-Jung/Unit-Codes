01_EXTR_VAR.py
import pandas as pd, numpy as np, glob, datetime

import os, math
import pandas as pd, glob, numpy as np
import matplotlib.pyplot as plt

# Preprocessing
from sklearn.preprocessing import MinMaxScaler

# Algorithms
from minisom import MiniSom
from tslearn.barycenters import dtw_barycenter_averaging
from tslearn.clustering import TimeSeriesKMeans
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from tslearn.metrics import dtw
from tslearn.metrics import soft_dtw

data_list = glob.glob('../02_POINT_DATA/*.csv')

ref_data = pd.read_csv(data_list[0], parse_dates=['Date'], index_col=0)
# print(data.columns, len(data.columns))
target_vars = data.columns


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
    plt.savefig('../02_POINT_DATA/%s.png'%site_nm)
    plt.close()


data_list = glob.glob('../02_POINT_DATA/*.csv')

# 동일변수에 대해서 각 관측소별 클러스터링 테스트를 위한 데이터 전처리

for var_ in target_vars:
    var_s_box = []
    
    for path in data_list:
        site_nm = path.split('\\')[-1].split('.')[0]
        data = pd.read_csv(path, parse_dates=['Date'], index_col=0).dropna(axis=0)
        var_s_box.append(pd.Series(data[var_], name='%s_%s'%(var_, site_nm)))
    
    var_s_df = pd.concat(var_s_box, axis=1)
    var_s_df.to_csv('../03_VARS_DATA/%s.csv'%var_)
