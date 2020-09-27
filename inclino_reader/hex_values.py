"""
Keep all the HEX codes in here so they can be reused
"""


class HexCode:
    def __init__(self, hex_code: bytearray, read_length: int):
        """
        Keep track of the hex code the sensor expects and what's the
        length of it's output

        :param hex_code: The HEX value for an operation
        :param read_length: The length the sensor's response for given command
        """
        self.hex_code = hex_code
        self.read_length = read_length


