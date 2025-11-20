from django.shortcuts import render
from rest_framework import viewsets

from railway_app.models import Station, Route, TrainType
from railway_app.serializers import (
    StationSerializer,
    StationListSerializer,
    RouterListSerializer,
    RouteSerializer,
    TrainTypeSerializer,
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


class RouteViewSet(BaseViewSetMethodMixin, viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    action_serializers = {
        "list": RouterListSerializer,
        "retrieve": RouterListSerializer,
    }


class TrainTypeViewSet(BaseViewSetMethodMixin, viewsets.ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
