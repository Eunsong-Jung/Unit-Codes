04_CLUSTER.pyimport glob, os, pandas as pd, numpy as np
from tslearn.metrics import soft_dtw, dtw
from tslearn.clustering import TimeSeriesKMeans


data_list = glob.glob('../03_VARS_DATA/*.csv')


def get_dtw(in_data, method, variable_nms):

    rst_dtw = np.zeros((in_data.shape[1], in_data.shape[1]))

    col_nms, var_set, clu_method = [], [], []
    
    for i in range(in_data.shape[1]):
        col_nms.append(in_data.columns[i].split('_')[-1])
        var_set.append(variable_nms)
        clu_method.append(method)
        
        if 'DTW' == method:
            
            for j in range(in_data.shape[1]):
                rst_dtw[i,j] = dtw(in_data.iloc[:,i], in_data.iloc[:,j])
        
        elif 'SOFT_DTW' == method:
            
            for j in range(in_data.shape[1]):
                rst_dtw[i,j] = soft_dtw(in_data.iloc[:,i], in_data.iloc[:,j])

    rst_dtw_df = pd.DataFrame(rst_dtw)
    rst_dtw_df.columns = col_nms
    rst_dtw_df.index   = [var_set, clu_method, col_nms]
    
    return rst_dtw_df


    all_time_kmean_rst = {}

for path in data_list:
    var_nm = path.split('\\')[-1].split('.')[0]
    print('%10s'%var_nm, ' :: ', path)
    data = pd.read_csv(path, parse_dates=['Date'], index_col=0).dropna(axis=0)
    
    dtw_rst  = get_dtw(data, 'DTW', variable_nms=var_nm)
    sdtw_rst = get_dtw(data, 'SOFT_DTW', variable_nms=var_nm)
    
    # dtw_con  = dtw_rst.append([dtw_rst, soft_dtw])

#     t_km_rst = []
#     for i in range(1,9):
#         model = TimeSeriesKMeans(n_clusters=i, metric="dtw", max_iter=10)
#         model.fit(data)
#         print(i, ':: ', f'Inertia: {model.inertia_}')
#         t_km_rst.append(model.inertia_)

#     all_time_kmean_rst[var_nm] = t_km_rst



all_time_kmean_rst = {}

t_km_rst = []
for i in range(1,9):
    model = TimeSeriesKMeans(n_clusters=i, metric="dtw", max_iter=10)
    model.fit(data)
    print(i, ':: ', f'Inertia: {model.inertia_}')
    t_km_rst.append(model.inertia_)

all_time_kmean_rst[var_nm] = t_km_rst
