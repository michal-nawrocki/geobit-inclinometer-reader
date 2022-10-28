from datetime import datetime

from usb_io import (
    SerialError,
    SerialService,
)


def initialize_devices():
    """Based on the /dev/ttyUSB* strings, initialize the SerialService"""
    devices = []

    for device in SerialService.DEVICES:
        try:
            initialized_device = SerialService(device)
        except SerialError:
            continue

        devices.append(initialized_device)

    return devices


def read_all_sensors(devices):
    """Read the devices and print readings"""
    current_time = datetime.now().isoformat(sep=" ", timespec="seconds")
    output_string = f"Reading at {current_time}\n"

    for index, device in enumerate(devices, start=1):
        reading_x = device.get_x_axis_reading()
        reading_y = device.get_y_axis_reading()
        reading_string = (
            f"  Sensor {index}:\n"
            f"    X:{reading_x}\n"
            f"    Y:{reading_y}\n"
        )
        output_string += reading_string

    return output_string

def reset_devices(devices):
    for index, device in enumerate(devices, start=1):
        try:
            device.set_relative_reader_mode()
            device.save_settings()
            print(f"Device {index} set to relative mode")
        except SerialError:
            print(f"ERROR: Device {index} could not be set to relative mode!")
