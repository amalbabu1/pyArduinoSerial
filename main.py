import time
from src.data.data_types import conert_to_int_type
from src.communication.serial_utility import get_data
from src.utils.datatransform.data_transform import tranform_all,multiply_data
from src.utils.quit_utitlity import quit_handler
from src.file.write_to_file import file_writer
import signal


if __name__ == "__main__":
    signal.signal(signal.SIGINT, quit_handler) #to quit the application using CTRL-C
    
    try:
        my_csv_file = file_writer("result/test_data.csv","w",",")
        my_csv_file_p = file_writer("result/test_data_processed.csv","w",",")
        for data in get_data():
            result_l = conert_to_int_type(data)
            result_p=tranform_all(multiply_data,result_l)
            print("data:-> ",*result_l, " processed:-> ", *result_p)
            my_csv_file.write_to_file([time.time(),*result_l])
            my_csv_file_p.write_to_file([time.time(),*result_p])
    except Exception as e:
        print(e)
    finally:
        my_csv_file.close_file()