from ast import arg
from typing import List



def multiply_data(data_list:List):
    return [data * 5 for data in data_list]
    


def tranform_all(function, data_list)->List:
    return list(function(data_list))



if __name__ == "__main__":
    data = [100,200]
    a = tranform_all(multiply_data,data)
    print(type(a))