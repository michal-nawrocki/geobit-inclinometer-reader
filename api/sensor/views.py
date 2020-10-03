from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.sensor.serializers import (
    SensorDataSerializer,
    SensorChangeReaderMode,
)
from inclino_reader.usb_io import (
    USB_1,
    USB_2,
    SerialService,
)

@api_view()
def get_sensor_data(request):
    sensor_one = SerialService(USB_1)
    sensor_two = SerialService(USB_2)

    sensor_data = [
        {
            "x_angle": sensor_one.get_x_axis_reading(),
            "y_angle": sensor_one.get_y_axis_reading(),
        },
        {
            "x_angle": sensor_two.get_x_axis_reading(),
            "y_angle": sensor_two.get_y_axis_reading(),
        }
    ]
    

    serializer = SensorDataSerializer(sensor_data, many=True)
    
    return Response(serializer.data)


@api_view()
def set_relative_reader_mode(request):
    sensor_one = SerialService(USB_1)
    sensor_two = SerialService(USB_2)


    sensor_data = {
        "sensor_one_status": sensor_one.set_relative_reader_mode(),
        "sensor_two_status": sensor_two.set_relative_reader_mode()
    }

    serializer = SensorChangeReaderMode(sensor_data)

    return Response(serializer.data)

@api_view()
def set_absolute_reader_mode(request):
    sensor_one = SerialService(USB_1)
    sensor_two = SerialService(USB_2)


    sensor_data = {
        "sensor_one_status": sensor_one.set_absolute_reader_mode(),
        "sensor_two_status": sensor_two.set_absolute_reader_mode()
    }

    serializer = SensorChangeReaderMode(sensor_data)

    return Response(serializer.data)


@api_view()
def save_settings(request):
    sensor_one = SerialService(USB_1)
    sensor_two = SerialService(USB_2)


    sensor_data = {
        "sensor_one_status": sensor_one.save_settings(),
        "sensor_two_status": sensor_two.save_settings()
    }

    serializer = SensorChangeReaderMode(sensor_data)

    return Response(serializer.data)
