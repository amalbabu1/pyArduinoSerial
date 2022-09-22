import argparse
import pathlib
import sys

from . import __version__


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="PyArduino Serial",
        description="python based serial monitor for microcontrollers",
        epilog="Thanks for using PyArduino Serial"
    )
    parser.version = f"PyArduinp v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "--baud",
        action="store",
        help="baudrate for serial communication",
        )
    parser.add_argument(
        "-f",
        "--from-file",
        action="store",
        help="(True) -> Process from file , (False) -> Process for serial directly from controller",
        )

    return parser.parse_args()