import pandas as pd
from sklearn import preprocessing
import os

#读取数据
file = 'multiple_industry without HSCI.csv'
series = pd.read_csv(file, header = 0, index_col = 0)
# print(series)
# print(series.shape)
series = series.dropna(axis = 0)
name, suf = os.path.splitext(file)
if suf =='.csv':
    nfile = name + '.txt'
    series.to_csv('pre_%s'%nfile, index = False)
