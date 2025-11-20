from rest_framework import serializers
from railway_app.models import (
    Station,
    TrainType,
    Route,
    Train,
    Crew,
    Journey,
    Order,
    Ticket,
    Payment,
)


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = "__all__"


class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ("id", "name")


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = "__all__"


class RouterListSerializer(serializers.ModelSerializer):
    source = serializers.SlugRelatedField(slug_field="name", read_only=True)
    destination = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Route
        fields = ("id", "source", "destination")


class TrainTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainType
        fields = "__all__"


class TrainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = "__all__"


class TrainListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Train
        fields = ("id", "name")


class TrainRetrieveSerializer(serializers.ModelSerializer):
    train_type = serializers.StringRelatedField()

    class Meta:
        model = Train
        fields = ("id", "name", "cargo_num", "places_in_cargo", "train_type")


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = "__all__"


class JourneyTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = "__all__"


class OrderTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class TicketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"


class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
