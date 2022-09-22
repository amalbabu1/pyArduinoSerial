
import csv
from typing import Any
import signal

class file_writer:
    open_file =[]
    def __init__(self, file_name:str, mode:str, delimiter:str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.delimiter = delimiter
        self.file = open(self.file_name,self.mode)
        self.open_file.append(self.file)
    
    def __del__(self):
       self.close_file()
        
    def write_to_file(self, contents:list):
        writer = csv.writer(self.file, delimiter=self.delimiter)
        writer.writerow(contents)
    
    @classmethod
    def close_file(cls):
        for f in cls.open_file:
            f.close()
    



if __name__ == "__main__":
    f = file_writer("a.csv","w", ',')
    f.write_to_file(["amal", "babu"])
    file_writer.close_file()
