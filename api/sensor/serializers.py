from rest_framework import serializers

class SensorDataSerializer(serializers.Serializer):
    x_angle = serializers.CharField(max_length=100)
    y_angle = serializers.CharField(max_length=100)


class SensorChangeReaderMode(serializers.Serializer):
    sensor_one_status = serializers.BooleanField()
    sensor_two_status = serializers.BooleanField()
