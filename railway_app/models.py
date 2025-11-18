from django.db import models

from config import settings


class Station(models.Model):
    name = models.CharField(max_length=63)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Route(models.Model):
    source = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="departures"
    )
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="arrivals"
    )
    distance = models.PositiveIntegerField()


class TrainType(models.Model):
    name = models.CharField(max_length=63)


class Train(models.Model):
    name = models.CharField(max_length=63)
    cargo_num = models.PositiveIntegerField()
    places_in_cargo = models.PositiveIntegerField()
    train_type = models.ForeignKey(
        TrainType, on_delete=models.CASCADE, related_name="trains_type"
    )


class Crew(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)


class Journey(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="journeys")
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name="journeys")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(Crew, related_name="journeys")


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )


class Ticket(models.Model):
    cargo = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    journey = models.ForeignKey(
        Journey, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")
