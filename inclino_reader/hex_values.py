"""
Keep all the HEX codes in here so they can be reused
"""


class HexCode:
    """
    Keep track of the hex code the sensor expects and how to handle output
    """
    def __init__(
        self,
        hex_code: bytearray,
        read_length: int,
    ):
        """
        Initalize a HexCode object

        :param hex_code: The HEX value for an operation
        :param read_length: The length the sensor's response for given command (in bytes)
        """
        self.hex_code = hex_code
        self.read_length = read_length



READ_X_AXIS =       HexCode(bytearray(b"\x77\x05\x00\x00\x01\x06"), 10)
READ_Y_AXIS =       HexCode(bytearray(b"\x77\x05\x00\x00\x02\x07"), 10)

SET_ABSOLUTE_ZERO = HexCode(bytearray(b"\x77\x06\x00\x00\x05\x00\x0B"), 7)
SET_RELATIVE_ZERO = HexCode(bytearray(b"\x77\x06\x00\x00\x05\x01\x0C"), 7)
SAVE_SETTINGS =     HexCode(bytearray(b"\x77\x05\x00\x00\x0A\x0F"), 7)

# Known constants in the HEX values
DATA_INDEX = 10
CHEKSUM_END_SLICE = -2
SUCCESS_BYTES = "00"
FAILURE_BYTES = "FF"
