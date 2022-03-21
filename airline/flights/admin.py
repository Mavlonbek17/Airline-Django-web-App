from csv import list_dialects
from django.contrib import admin
from .models import Airport,Flight,Passenger
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class AirportAdmin(admin.ModelAdmin):
    list_display = ("code","city")

class Passengeradmin(admin.ModelAdmin):
    filter_horizontal = ["passenger_flights"]



admin.site.register(Airport,AirportAdmin)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,Passengeradmin)
