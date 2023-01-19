from django.urls import path
from .views import *

urlpatterns = [
    # get and post api
    path('aircraft/list/view', AircraftListView.as_view(), name='aircraftlistview'),
    path('airport/list/view', AirportListView.as_view(), name='airportlistview'),
    path('flight/list/view', FlightListView.as_view(), name='flightlistview'),
    path('management/list/view', ManagementListView.as_view(), name='managementlistview'),

    # delete api view
    path('aircraft/delete/view/<int:id>', AircraftDelete.as_view(), name='aircraftdelete'),
    path('airport/delete/view/<int:id>', AirportDelete.as_view(), name='airportdelete'),
    path('flight/delete/view/<int:id>', FlightDelete.as_view(), name='flightdelete'),
    path('management/delete/view/<int:id>', ManagementDelete.as_view(), name='managementdelete'),

    # search or filter data
    path('search/fields',SearchFields.as_view(), name='searchfields')
]
