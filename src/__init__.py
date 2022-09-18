from typing import List
from data_types import convert_to_int_type
from serial_utility import get_data
from data_transform import tranform_all,multiply_data
from quit_utitlity import quit_handler
from write_to_file import file_writer
import signal


def acton_on_index(data_l:List, index):
    data_l[index] = data_l[index] *3
    return data_l

if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_handler) #to quit the application using CTRL-C
    
    try:
        my_csv_file = file_writer("result/test_data.csv","w",",")
        my_csv_file_p = file_writer("result/test_data_processed.csv","w",",")
        for data in get_data():
            result_l = convert_to_int_type(data)
            result_p=tranform_all(acton_on_index,result_l,0)
            print("data:-> ",*result_l, "proceesed:->",* result_p)
            my_csv_file.write_to_file([*result_l])
            my_csv_file_p.write_to_file([*result_p])
    except Exception as e:
        print(e)
    finally:
        my_csv_file.close_file()