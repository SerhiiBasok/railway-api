from django.contrib import admin

from railway_app.models import (
    Order,
    Station,
    Train,
    Ticket,
    Journey,
    Crew,
    TrainType,
    Route,
)

admin.site.register(Order)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Journey)
admin.site.register(Crew)
admin.site.register(TrainType)
admin.site.register(Route)
