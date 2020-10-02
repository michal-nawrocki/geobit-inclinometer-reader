from rest_framework.decorators import api_view
from rest_framework.response import Response


from api.sensor.serializers import SensorSerializer
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
    

    serializer = SensorSerializer(sensor_data, many=True)
    
    return Response(serializer.data)
