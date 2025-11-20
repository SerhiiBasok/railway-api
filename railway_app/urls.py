from django.urls import path, include
from rest_framework import routers

from railway_app.views import (
    StationViewSet,
    RouteViewSet,
    TrainTypeViewSet,
    TrainViewSet,
)

app_name = "railway"

router = routers.DefaultRouter()
router.register("station", StationViewSet)
router.register("route", RouteViewSet)
router.register("train-type", TrainTypeViewSet)
router.register("train", TrainViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
