from django.db import models
from django.db.models.constraints import UniqueConstraint

from config import settings


class Station(models.Model):
    name = models.CharField(max_length=63, unique=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Station name: {self.name}"


class Route(models.Model):
    source = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="departures"
    )
    destination = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="arrivals"
    )
    distance = models.PositiveIntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=["source", "destination"], name="unique_route")
        ]


class TrainType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return f"Train type: {self.name}"


class Train(models.Model):
    name = models.CharField(max_length=63)
    cargo_num = models.PositiveIntegerField()
    places_in_cargo = models.PositiveIntegerField()
    train_type = models.ForeignKey(
        TrainType, on_delete=models.CASCADE, related_name="trains"
    )


class Crew(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["first_name", "last_name"], name="unique_crew_member"
            )
        ]


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
    price_snapshot = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["cargo", "seat", "journey"], name="unique_seat_on_journey"
            )
        ]


class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="payment"
    )
    stripe_payment_intent = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=32, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
