# -*- coding: utf-8 -*-
import pandas
from pandas import read_csv, DataFrame, Series
import time
from datetime import datetime

# data load
my_data = read_csv('./mydata.csv')
api_data = read_csv('./api_data.csv')

# my_data에서 'date' column에서 '-' 제거(api_data의 'date' column과 동일하게 맞춰서 join 하기 위해)
col_name_list = list(my_data)
values = my_data.values
for i in range(len(values)):
    values[i,0] = values[i,0].replace('-','')

my_data = pandas.DataFrame(values)
my_data.columns= col_name_list

# api_data에서 'date' column에서 int type -> str type (my_data의 'date' column꽈 동일하게 맞춰서 join 하기 위해)
col_name_list = list(api_data)
values = api_data.values
for i in range(len(values)):
    values[i,0] = str(values[i,0])

api_data = pandas.DataFrame(values)
api_data.columns= col_name_list

# JOIN
join_df = pandas.merge(my_data, api_data, how = 'outer')

# '거래 금액' column : str -> int type
for i in range(len(join_df)):
    join_df['거래금액'][i] = int(join_df['거래금액'][i].replace(',',''))

# date, sales, 거래금액 열 제외한 열 drop
join_df = join_df.drop('시군구', axis=1)
join_df = join_df.drop('번지', axis=1)
join_df = join_df.drop('본번', axis=1)
join_df = join_df.drop('부번', axis=1)
join_df = join_df.drop('단지명', axis=1)
join_df = join_df.drop('전용면적', axis=1)
#print(join_df)

# Save dataset
join_df.to_csv('./preprocessing_finish.csv')