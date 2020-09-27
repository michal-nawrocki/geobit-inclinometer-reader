from unittest.mock import (
    Mock,
    patch,
)
import unittest
from serial import SerialException

from inclino_reader.hex_values import READ_X_AXIS
from inclino_reader.usb_io import (
    USB_1,
    USB_2,
    SerialService,
)

class TestSerialService(unittest.TestCase):

    @patch("inclino_reader.usb_io.serial.Serial")
    def test_serial_service_init(self, mock_serial):
        mock_serial.return_value.isOpen.return_value = True

        serial_service = SerialService(USB_1)

        assert mock_serial.call_count == 1
        mock_serial.assert_called_once_with(
            baudrate=9600,
            bytesize=8,
            parity='N',
            port='/dev/ttyUSB0',
            stopbits=1
        )

    @patch("inclino_reader.usb_io.serial.Serial")
    def test_serial_service_raises_when_not_open(self, mock_serial):
        mock_serial.return_value.isOpen.return_value = False

        with self.assertRaises(ValueError):
            serial_service = SerialService(USB_2)
        
        assert mock_serial.call_count == 1
        mock_serial.assert_called_once_with(
            baudrate=9600,
            bytesize=8,
            parity='N',
            port='/dev/ttyUSB1',
            stopbits=1
        )

    @patch("inclino_reader.usb_io.serial.Serial")
    def test_serial_service_raises_serial_exception(self, mock_serial):
        mock_serial.side_effect = SerialException

        with self.assertRaises(ValueError):
            serial_service = SerialService(USB_2)

        assert mock_serial.call_count == 1
        mock_serial.assert_called_once_with(
            baudrate=9600,
            bytesize=8,
            parity='N',
            port='/dev/ttyUSB1',
            stopbits=1
        )

    @unittest.skip("Work in Progress")
    @patch("inclino_reader.usb_io.serial.Serial.read.hex")
    @patch("inclino_reader.usb_io.serial.Serial.write")
    @patch("inclino_reader.usb_io.serial.Serial.read")
    @patch("inclino_reader.usb_io.serial.Serial")
    def test_serial_service__do_serial_call(
        self,
        mock_serial,
        mock_read,
        mock_write,
        mock_hex
    ):
        mock_serial.return_value.isOpen.return_value = True
        mock_read.return_value = b"\x77\x09\x00\x00\x82\x10\x00\x14\x10\xbf"
        mock_write.return_value = "I've wrote to the sensor"
        mock_hex.return_value = "770900008210001410bf"


        serial_service = SerialService(USB_2)
        response = serial_service._do_serial_call(READ_X_AXIS)
        self.assertEqual(response, "770900008210001410bf")
        