from ast import arg
from typing import List



def multiply_data(data_list:List, factor):
    return [(data * factor) for data in data_list]
    


def tranform_all(function, *args)->List:
    return list(function(*args))



if __name__ == "__main__":
    data = [100,200]
    a = tranform_all(multiply_data,data,3)
    print(a)