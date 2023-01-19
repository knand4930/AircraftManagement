from drf_writable_nested import UniqueFieldsMixin
from rest_framework import serializers
from main.models import *


class AircraftSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'manufacture', 'aircraft_name']


class AirportSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'name', 'icao_code']


class FlightSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'name']


class ManagementSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = ['id', 'aircraft', 'flight', 'arrival_airport', 'departure_airport', 'arrival_flight_date',
                  'arrival_flight_time', 'departure_flight_date', 'departure_flight_time']
