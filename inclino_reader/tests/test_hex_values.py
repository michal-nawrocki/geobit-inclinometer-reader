import unittest

from inclino_reader.hex_values import *

class TestHexValues(unittest.TestCase):
    def test_hex_code(self):
        example = HexCode(bytearray(b"\x12"), 10)

        self.assertEqual(example.hex_code, bytearray(b"\x12"))
        self.assertEqual(example.read_length, 10)

    def test_read_x_axis(self):
        self.assertEqual(READ_X_AXIS.hex_code, bytearray(b"\x77\x05\x00\x00\x01\x06"))
        self.assertEqual(READ_X_AXIS.read_length, 10)
    
    def test_read_y_axis(self):
        self.assertEqual(READ_Y_AXIS.hex_code, bytearray(b"\x77\x05\x00\x00\x02\x07"))
        self.assertEqual(READ_Y_AXIS.read_length, 10)

    def test_set_absolute_zero(self):
        self.assertEqual(SET_ABSOLUTE_ZERO.hex_code, bytearray(b"\x77\x06\x00\x00\x05\x00\x0B"))
        self.assertEqual(SET_ABSOLUTE_ZERO.read_length, 7)

    def test_set_relative_zero(self):
        self.assertEqual(SET_RELATIVE_ZERO.hex_code, bytearray(b"\x77\x06\x00\x00\x05\x01\x0C"))
        self.assertEqual(SET_RELATIVE_ZERO.read_length, 7)

    def test_save_settings(self):
        self.assertEqual(SAVE_SETTINGS.hex_code, bytearray(b"\x77\x05\x00\x00\x0A\x0F"))
        self.assertEqual(SAVE_SETTINGS.read_length, 7)

    def test_constants(self):
        self.assertEqual(DATA_INDEX, 10)
        self.assertEqual(CHEKSUM_END_SLICE, -2)
        self.assertEqual(SUCCESS_BYTES, "00")
        self.assertEqual(FAILURE_BYTES, "FF")
