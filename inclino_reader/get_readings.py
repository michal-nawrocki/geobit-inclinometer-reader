"""Initialize all USB inclinometers and print their readings"""
from helpers import (
    initialize_devices,
    read_all_sensors
)

if __name__ == "__main__":
    devices = initialize_devices()
    data = read_all_sensors(devices)
    print(data)
