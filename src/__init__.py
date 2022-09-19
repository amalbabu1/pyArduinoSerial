from typing import List
from data_types import convert_to_int_type
from data_transform import tranform_all,multiply_data
from quit_utitlity import quit_handler
from data_stream import DataStream
from write_to_file import file_writer
import signal


def acton_on_index(data_l:List, index):
    data_l[index] = data_l[index] *3
    return data_l

if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_handler) #to quit the application using CTRL-C
    
    try:
        '''
        DataStream(True) -> Process from file
        DataStream(False) -> Process for serial directly from controller
        '''
        ds = DataStream(False)
        if ds.state:
            my_csv_file = file_writer("result/test_data.csv","w",",")
        my_csv_file_p = file_writer("result/test_data_processed.csv","w",",")
        

        for data in ds.getDataStream():
            if ds.state:
                result_l = convert_to_int_type(data)
                result_p=tranform_all(acton_on_index,result_l,0)
                print("data:-> ",*result_l, "proceesed:->",* result_p)
                my_csv_file.write_to_file([*result_l])
                my_csv_file_p.write_to_file([*result_p])
            
            else:
                result_p=tranform_all(multiply_data,data,5)
                print("data:->",*data,"proceesed:->",* result_p)
                my_csv_file_p.write_to_file([*result_p])
    
    except Exception as e:
        print(e)
    finally:
        if ds.state:
            my_csv_file.close_file()
        my_csv_file_p.close_file()