"""Initialize all USB inclinometers and print their readings"""
from helpers import (
    initialize_devices,
    reset_devices
)

if __name__ == "__main__":
    devices = initialize_devices()
    reset_devices(devices)
