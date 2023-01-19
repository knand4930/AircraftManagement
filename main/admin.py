from django.contrib import admin
from .models import *


# Register your models here.

class AircarftAdmin(admin.ModelAdmin):
    list_display = ('serial', 'manufacture', 'aircraft_name')
    list_filter = ('aircraft_name', 'serial')


admin.site.register(Aircraft, AircarftAdmin)


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'icao_code')
    list_filter = ('icao_code',)


admin.site.register(Airport, AirportAdmin)


class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    list_filter = ('name', 'create_at', 'update_at')


admin.site.register(Flight, FlightAdmin)


class ManagementAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'arrival_airport', 'departure_airport')
    list_filter = ('aircraft', 'arrival_airport', 'departure_airport')


admin.site.register(Management, ManagementAdmin)
