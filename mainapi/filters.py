import django_filters

from main.models import *
from django_filters import rest_framework as filters, DateFilter, TimeFilter, TimeRangeFilter


class ManagementFilter(filters.FilterSet):
    time_range = TimeRangeFilter(field_name='departure_flight_time')
    arrival_airport__name = django_filters.CharFilter(lookup_expr='icontains')
    departure_airport__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Management
        fields = ['flight']
