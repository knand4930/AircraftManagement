from django.urls import path
from .views import *

urlpatterns = [
    path('', login_attempt, name='login_attempt'),
    path('adminpanel', adminpanel, name='adminpanel'),
    # show list
    path('aircraft/list', air_craft, name='air_craft'),
    path('airport/list', air_port, name='air_port'),
    path('flight/list', flight_list, name='flight_list'),
    path('management/list', management_list, name='management_list'),
    # filter section
    path('management/filter/arrival', management_arrival, name='management_arrival'),
    path('management/filter/departure', management_departure, name='management_departure'),
    # create details
    path('add/aircraft', add_aircraft, name='add_aircraft'),
    path('add/airport', add_airport, name='add_airport'),
    path('add/flight', add_flight, name='add_flight'),
    path('add/management', add_management, name='add_management'),
    # delete details
    path('delete/aircraft/<slug>', del_aircraft, name='del_aircraft'),
    path('delete/airport/<slug>', del_airport, name='del_airport'),
    path('delete/flight/<slug>', del_flight, name='del_flight'),
    path('delete/management/<id>', del_management, name='del_management'),
    # edit Details
    path('edit/aircraft/<id>', edit_aircraft, name='edit_aircraft'),
    path('edit/airport/<id>', edit_airport, name='edit_airport'),
    path('edit/flight/<id>', edit_flight, name='edit_flight'),
    path('edit/management/<id>', edit_management, name='edit_management'),
]
