"""
Do read and write calls over the RS485 USB adapter to the inclinometer sensors
"""
import logging
from typing import Optional
import serial

from hex_values import *

_logger = logging.getLogger(__name__)


class SerialError(Exception):
    """Exception to handle all serial issues"""


class SerialService:
    USB_1 = '/dev/ttyUSB0'
    USB_2 = '/dev/ttyUSB6'
    DEVICES = [USB_1, USB_2]

    def __init__(self, usb_dev: HexCode):
        try:
            self._connection = serial.Serial(
                port=usb_dev,
                baudrate=9600,
                timeout=1,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
            )
        except (ValueError, serial.SerialException) as e:
            _logger.warning(e)
            raise SerialError()

        if not self._connection.isOpen():
            _logger.warning(
                "The USB serial connection is not open. Aborting...")
            raise SerialError()

    def _do_serial_call(self, call: HexCode) -> bytearray:
        """
        Perform the IO calls using the objects Serial connection

        :param hex_call: The HexCode object for specified operation
        :return: `bytearray` with response from sensor
        """
        self._connection.write(call.hex_code)
        response = self._connection.read(call.read_length)
        
        if not response:
            raise SerialError("No data recieved")

        return response.hex()

    def _convert_status_response_to_str(self, status: str) -> bool:
        """
        Convert the status hex representation into `bool` one.
        This will be True/False

        :param status: The hex string of a status response
        :return: Bool representation of the status response [True/False]
        """
        output = status[DATA_INDEX:CHEKSUM_END_SLICE]

        if output == SUCCESS_BYTES:
            return True
        else:
            return False

    def _convert_angle_response_to_str(self, angle: str) -> str:
        """
        Convert the angle hex representation into str one.
        This includes the +/= bit of the angle and decimal point representation

        :param angle: The hex string of a read angle
        :return: String representation of an angle (with sign and decimal point)
        """
        output = angle[DATA_INDEX:CHEKSUM_END_SLICE]

        if output[0] == "1":
            converted = "+" + output[1:4] + "." + output[4:]
        else:
            converted = "-" + output[1:4] + "." + output[4:]

        return converted

    def get_x_axis_reading(self) -> Optional[str]:
        """
        Get the X-axis reading from sensor

        :return: Read angle as a string (with sign and decimal point)
        """
        try:
            response = self._do_serial_call(READ_X_AXIS)
        except SerialError:
            return None
        return self._convert_angle_response_to_str(response)

    def get_y_axis_reading(self) -> Optional[str]:
        """
        Get the Y-axis reading from sensor

        :return: Read angle as a string (with sign and decimal point)
        """
        try:
            response = self._do_serial_call(READ_Y_AXIS)
        except SerialError:
            return None
        return self._convert_angle_response_to_str(response)

    def set_relative_reader_mode(self) -> bool:
        """
        Set the inclinometer into relative-zero mode

        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(SET_RELATIVE_ZERO)
        return self._convert_status_response_to_str(response)

    def set_absolute_reader_mode(self) -> bool:
        """
        Set the inclinometer into absolute-zero mode

        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(SET_ABSOLUTE_ZERO)
        return self._convert_status_response_to_str(response)

    def save_settings(self) -> bool:
        """
        Save the inclinometer settings.

        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(SAVE_SETTINGS)
        return self._convert_status_response_to_str(response)
