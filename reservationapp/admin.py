from time import time
from django.contrib import admin
from reservationapp.models import Commodity, UserCredientials,Ticket,Time,Train,Route
# Register your models here.
admin.site.register(UserCredientials)
admin.site.register(Train)
admin.site.register(Time)
admin.site.register(Ticket)
admin.site.register(Route)
admin.site.register(Commodity)