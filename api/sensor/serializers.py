from rest_framework import serializers

class SensorSerializer(serializers.Serializer):
    x_angle = serializers.CharField(max_length=100)
    y_angle = serializers.CharField(max_length=100)
