"""Read and store readings in specified text file"""
from helpers import (
    initialize_devices,
    read_all_sensors
)
import argparse


def fetch_path():
    parser = argparse.ArgumentParser(
        description="Read and store inclinometer readings in specified textfile"
    )
    parser.add_argument(
        "path",
        metavar="p",
        type=str,
        nargs="?",
        help="path to textfile where recording will be stored"
    )
    return parser.parse_args().path


def store_data(path: str, data):
    with open(path, "a") as destination_file:
        destination_file.write(data)


if __name__ == "__main__":
    path = fetch_path()
    devices = initialize_devices()
    data = read_all_sensors(devices)
    store_data(path, data)
