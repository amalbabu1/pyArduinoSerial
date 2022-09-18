
import signal
import sys

from write_to_file import file_writer

# from write_to_file import file_writer

file_writer


def quit_handler(signum, frame):
    print(f"Ctrl-c was pressed\n Application turned off")
    file_writer.close_file()
    sys.exit(0)