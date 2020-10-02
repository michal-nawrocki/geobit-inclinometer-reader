from rest_framework import routers
from django.urls import path, include

from api.sensor import views


urlpatterns = [
    path('sensor/', views.get_sensor_data, name='get-sensor-data'),
]
