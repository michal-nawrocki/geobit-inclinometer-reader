"""
Do read and write calls over the RS485 USB adapter to the inclinometer sensors
"""
import serial

from inclino_reader import hex_values


USB_1 = '/dev/ttyUSB0'
USB_2 = '/dev/ttyUSB1'


class SerialService:
    def __init__(self, usb_dev: hex_values.HexCode):
        try:
            self._connection = serial.Serial(
                port=usb_dev,
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
            )
        except (ValueError, serial.SerialException) as e:
            print(e)
            raise ValueError

        if not self._connection.isOpen():
            print("The USB serial connection is not open. Aborting...")
            raise ValueError

    def _do_serial_call(self, call: hex_values.HexCode) -> bytearray:
        """
        Perform the IO calls using the objects Serial connection

        :param hex_call: The HexCode object for specified operation
        :return: `bytearray` with response from sensor
        """
        self._connection.write(call.hex_code)
        response = self._connection.read(call.read_length)

        return response.hex()


    def _convert_status_response_to_str(self, status: str) -> bool:
        """
        Convert the status hex representation into `bool` one.
        This will be True/False

        :param status: The hex string of a status response
        :return: Bool representation of the status response [True/False]
        """
        output = status[hex_values.DATA_INDEX:hex_values.CHEKSUM_END_SLICE]

        if output == hex_values.SUCCESS_BYTES:
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
        output = angle[hex_values.DATA_INDEX:hex_values.CHEKSUM_END_SLICE]

        if output[0] == "1":
            converted = "+" + output[1:4] + "." + output[4:]
        else:
            converted = "-" + output[1:4] + "." + output[4:]

        return converted

    def get_x_axis_reading(self) -> str:
        """
        Get the X-axis reading from sensor
        
        :return: Read angle as a string (with sign and decimal point)
        """
        response = self._do_serial_call(hex_values.READ_X_AXIS)
        return self._convert_angle_response_to_str(response)

    def get_y_axis_reading(self) -> str:
        """
        Get the Y-axis reading from sensor

        :return: Read angle as a string (with sign and decimal point)
        """
        response = self._do_serial_call(hex_values.READ_Y_AXIS)
        return self._convert_angle_response_to_str(response)


    def set_relative_reader_mode(self) -> bool:
        """
        Set the inclinometer into relative-zero mode
        
        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(hex_values.SET_RELATIVE_ZERO)
        return self._convert_status_response_to_str(response)

    def set_absolute_reader_mode(self) -> bool:
        """
        Set the inclinometer into absolute-zero mode
        
        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(hex_values.SET_ABSOLUTE_ZERO)
        return self._convert_status_response_to_str(response)

    def save_settings(self) -> bool:
        """
        Save the inclinometer settings.
        
        :return: Status if the change was successful or not as bool
        """
        response = self._do_serial_call(hex_values.SAVE_SETTINGS)
        return self._convert_status_response_to_str(response)
