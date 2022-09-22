
import csv
from typing import Any, List

class file_reader:
    open_file =[]
    def __init__(self, file_name:str, mode:str, delimiter:str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.delimiter = delimiter
        self.file = open(self.file_name,self.mode)
        self.open_file.append(self.file)
    
    def __del__(self):
       self.close_file()
        

    def read_from_file(self)->List:
        reader = csv.reader(self.file)
        for row in reader:
            # yield row
            yield  list(map(int,row))
    
    @classmethod
    def close_file(cls):
        for f in cls.open_file:
            f.close()
    



if __name__ == "__main__":
    f = file_reader("/home/amal/Python/pyArduinoSerial/result/test_data.csv","r", ',')
    for row in f.read_from_file():
        print(row)