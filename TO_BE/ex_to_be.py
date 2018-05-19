from function_mapping import *

# Data load
my_data = read_csv('./mydata.csv')
api_data = read_csv('./api_data.csv')

# string query
ex_str1 = "i want change my_data dataset's 0 column type from str to str"
ex_str2 = "i want change api_data dataset's 0 column type from int to str"
ex_str3 = "i want join my_data and api_data table"

# TEST
while True:
    input_str = input('입력 : ')
    if input_str == 'c':
        break
    print('-------------------------------------------------------')
    print(function_mapping(input_str))
    print('-------------------------------------------------------')
    print('이러한 결과를 원하나여? [Y/N]')
    print('...................Done..............')
    print('\n\n')