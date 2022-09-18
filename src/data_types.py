from cgitb import reset
from typing import List


def convert_to_int_type(data_line)->List:
    result = data_line.decode("utf").strip('\n').split(',')
    l_result =map(int,result)
    return list(l_result)