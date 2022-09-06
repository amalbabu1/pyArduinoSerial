
import signal
import sys

from src.file.write_to_file import file_writer

def quit_handler(signum, frame):
    print(f"Ctrl-c was pressed\n Application turned off")
    file_writer.close_file()
    sys.exit(0)