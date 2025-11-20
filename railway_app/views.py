from django.shortcuts import render
from rest_framework import viewsets

from railway_app.models import Station, Route
from railway_app.serializers import (
    StationSerializer,
    StationListSerializer,
    RouterListSerializer,
    RouteSerializer,
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
