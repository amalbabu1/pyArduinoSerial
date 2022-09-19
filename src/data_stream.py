

from serial_utility import get_data
from read_from_file import file_reader




class DataStream():
    def __init__(self, state:bool) -> None:
        self.state = state
        if self.state:
            self.dataStream = get_data
        else:
            fl = file_reader("/home/amal/Python/pyArduinoSerial/result/test_data.csv","r", ',')
            self.dataStream = fl.read_from_file

    def getDataStream(self):
        return self.dataStream()