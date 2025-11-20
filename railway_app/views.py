from django.shortcuts import render
from rest_framework import viewsets

from railway_app.models import Station
from railway_app.serializers import (
    StationSerializer,
    StationListSerializer,
)
from utils.custom_mixin import BaseViewSetMethodMixin


class StationViewSet(BaseViewSetMethodMixin, viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    action_serializers = {
        "list": StationListSerializer,
        "retrieve": StationSerializer,
        "create": StationSerializer,
        "update": StationSerializer,
        "partial_update": StationSerializer,
    }
