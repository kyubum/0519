from function import *

my_dataset = read_csv('./mydata.csv')
api_dataset = read_csv('./api_data.csv')

def function_mapping(str):
    if 'join' in str:
        token = str.split(' ')
        para_index = token.index('and')
        para1 = token[para_index-1]
        if para1 == 'my_data':
            para1 = my_dataset
        elif para1 == 'api_data':
            para1 = api_dataset

        para2 = token[para_index+1]
        if para2 == 'my_data':
            para2 = my_dataset
        elif para2 == 'api_data':
            para2 = api_dataset
        return(join(para1,para2))

    if 'change' in str:
        token = str.split(' ')
        para1_index = token.index("dataset's")
        para1 = token[para1_index-1]
        if para1 == 'my_data':
            para1 = my_dataset
        elif para1 == 'api_data':
            para1 = api_dataset

        para2_index = token.index('column')
        para2 = int(token[para2_index-1])
        
        from_type = token[token.index('from')+1]
        to_type = token[token.index('to')+1]
        
        if from_type == 'str' and to_type == 'str':
            return(type_change_str_to_str(para1, para2))
        
        if from_type == 'int' and to_type == 'str':
            return(type_change_int_to_str(para1, para2))

        if from_type == 'str' and to_type == 'int':
            return(type_change_str_to_int(para1, para2))
        
    if 'drop' in str:
        token = str.split(' ')
        para2_index = token.index('drop')
        para1_index = token.index('dataset')
        para1 = token[para1_index-1]
        para2 = token[para2_index+1].split(',')
        return(drop_column(para1,para2))