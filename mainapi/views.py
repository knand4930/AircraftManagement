from django.shortcuts import render
from .serializers import *
from main.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .filters import ManagementFilter
from django_filters import rest_framework as filters


# Create your views here.

class AircraftListView(ListCreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AirportListView(ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightListView(ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class ManagementListView(ListCreateAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class AircraftDelete(RetrieveUpdateDestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    lookup_field = 'id'


class AirportDelete(RetrieveUpdateDestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    lookup_field = 'id'


class FlightDelete(RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'id'


class ManagementDelete(RetrieveUpdateDestroyAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    lookup_field = 'id'


class SearchFields(ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ManagementFilter
