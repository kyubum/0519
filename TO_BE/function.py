# -*- coding: utf-8 -*-
import pandas
from pandas import read_csv, DataFrame, Series
import time
from datetime import datetime

def type_change_str_to_str(dataset, column_index):
    col_name_list = list(dataset)
    values = dataset.values
    for i in range(len(values)):
        values[i,column_index] = values[i,column_index].replace('-','')

    dataset = pandas.DataFrame(values)
    dataset.columns= col_name_list
    return dataset

def type_change_int_to_str(dataset, column_index):
    col_name_list = list(dataset)
    values = dataset.values
    for i in range(len(dataset)):
        values[i,column_index] = str(values[i,column_index])

    dataset = pandas.DataFrame(values)
    dataset.columns= col_name_list
    return dataset

def type_change_str_to_int(dataset, column_name):
    for i in range(len(dataset)):
        dataset[column_name][i] = int(dataset[column_name][i].replace(',',''))
    return dataset

def drop_column(dataset, drop_col_list):
    for i in drop_col_list:
        dataset = dataset.drop(i, axis = 1)
    return dataset

def join(dataset1, dataset2):
    join_df = pandas.merge(dataset1, dataset2, how = 'outer')
    return join_df