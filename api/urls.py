from rest_framework import routers
from django.urls import path, include

from api.sensor import views


router = routers.DefaultRouter()

#router.register(r"api", views)

urlpatterns = [
    path("", include(router.urls))
]
