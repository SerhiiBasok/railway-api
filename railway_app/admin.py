from django.contrib import admin

from railway_app.models import (
    Crew,
    Journey,
    Order,
    Payment,
    Route,
    Station,
    Ticket,
    Train,
    TrainType,
)

admin.site.register(Order)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Journey)
admin.site.register(Crew)
admin.site.register(TrainType)
admin.site.register(Route)
admin.site.register(Payment)
