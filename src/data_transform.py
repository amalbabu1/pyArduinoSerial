from ast import arg
from typing import List



def multiply_data(data_list:List, factor):
    return [(data * factor) for data in data_list]
    


'''

take a function (function) and its argumets and apply on the data
here below multiply_data fn and args are passed to transform all

this function can be used as an api to apply processing on the data

'''
def tranform_all(function,data_list,*args)->List:
    return list(function(data_list.copy(), *args))



if __name__ == "__main__":
    data = [100,200]
    a = tranform_all(multiply_data,data,3)
    print(a)