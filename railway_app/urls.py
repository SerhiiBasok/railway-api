from django.urls import path, include
from rest_framework import routers
from rest_framework.urls import app_name

from railway_app.views import StationViewSet

app_name = "railway"

router = routers.DefaultRouter()
router.register("station", StationViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
