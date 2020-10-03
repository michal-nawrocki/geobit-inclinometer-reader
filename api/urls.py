from rest_framework import routers
from django.urls import path, include

from api.sensor import views


urlpatterns = [
    path("sensor/", views.get_sensor_data, name="get-sensor-data"),
    path("set-absolute-mode/", views.set_absolute_reader_mode, name="set-absolute-reader-mode"),
    path("set-relative-mode/", views.set_relative_reader_mode, name="set-relative-reader-mode"),
    path("save/", views.save_settings, name="save-settings")
]
