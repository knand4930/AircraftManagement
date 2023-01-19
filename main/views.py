from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.

def login_attempt(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()

            if user_obj is None:
                msg = "username Not Found"
                return render(request, 'login_pages.html', {'msg': msg})

            user = authenticate(username=username, password=password)
            # pdb.set_trace()
            if user is None:
                msg = "Wrong Password"
                return render(request, 'login_pages.html', {'msg': msg})
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('adminpanel')
                else:
                    msg = "Your Login Details Has Been Not Super User!"
                    return render(request, 'login_pages.html', {'msg': msg})
            else:
                msg = "Invalid Credential!"
                return render(request, 'login_pages.html', {'msg': msg})
    except Exception as e:
        print(e)
        msg = "Something Went Wrong Please Connect With Administrator !"
        return render(request, 'login_pages.html', {'msg': msg})
    return render(request, 'login_pages.html')


def adminpanel(request):
    acraft = Aircraft.objects.all().count()
    aport = Airport.objects.all().count()
    flight = Flight.objects.all().count()
    mment = Management.objects.all().count()
    return render(request, 'adminpanel.html', {'acraft': acraft, 'aport': aport, 'flight': flight, 'mment': mment})


def air_craft(request):
    value = Aircraft.objects.all()
    msg = "Aircraft Data"
    return render(request, 'list/air_craft_list.html', {'value': value, 'msg': msg})


def air_port(request):
    value = Airport.objects.all()
    msg = "Airport Data"
    return render(request, 'list/air_port_list.html', {'value': value, 'msg': msg})


def flight_list(request):
    value = Flight.objects.all()
    msg = "Flight Data"
    return render(request, 'list/flight_list.html', {'value': value, 'msg': msg})


def management_list(request):
    value = Management.objects.all()
    data = Airport.objects.all()
    try:
        if request.method == 'POST':
            departure_flight_time_start = request.POST.get('departure_flight_time_start')
            departure_flight_time_end = request.POST.get('departure_flight_time_end')
            value = Management.objects.filter(
                departure_flight_time__range=[departure_flight_time_start, departure_flight_time_end])
            return render(request, 'valuesearch.html', {'value': value})
    except Exception as e:
        print(e)
        msg = "Please Input Correct Time Range !"
        return render(request, 'list/management_list.html', {'msg': msg})
    msg = "Management Values"
    return render(request, 'list/management_list.html', {'value': value, 'msg': msg, 'data': data})


def management_arrival(request):
    value = Management.objects.all()
    try:
        if request.method == 'POST':
            arrival_airport = request.POST.get('arrival_airport', None)
            value = Management.objects.filter(arrival_airport__name__icontains=arrival_airport)
            return render(request, 'valuesearch.html', {'value': value})
    except Exception as e:
        print(e)
        msg = "Please Input Correct Arrival Airport Value !"
        return render(request, 'list/management_list.html', {'msg': msg})
    msg = "Management Values"
    return render(request, 'list/management_list.html', {'value': value, 'msg': msg})


def management_departure(request):
    value = Management.objects.all()
    try:
        if request.method == 'POST':
            departure_airport = request.POST.get('departure_airport', None)
            value = Management.objects.filter(departure_airport__name__icontains=departure_airport)
            return render(request, 'valuesearch.html', {'value': value})
    except Exception as e:
        print(e)
        msg = "Please Input Correct Departure Airport Value !"
        return render(request, 'list/management_list.html', {'msg': msg})
    msg = "Management Values"
    return render(request, 'list/management_list.html', {'value': value, 'msg': msg})


def add_aircraft(request):
    msg = "Add Aircraft"
    if request.method == 'POST':
        aircraft_name = request.POST.get('aircraft_name')
        manufacture = request.POST.get('manufacture')
        if Aircraft.objects.filter(manufacture=manufacture).exists():
            msg = "Manufacture Value Already Exists"
            return render(request, 'add/add_aircraft.html', {'msg': msg})
        data = Aircraft.objects.create(aircraft_name=aircraft_name, manufacture=manufacture)
        data.save()
        val1 = "Aircraft Name"
        val2 = "Manufacture"
        msg = "you Have Created Successfully New Aircraft"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': aircraft_name, 'var2': manufacture, 'val1': val1, 'val2': val2})
    return render(request, 'add/add_aircraft.html', {'msg': msg})


def add_airport(request):
    msg = "Add Airport"
    if request.method == 'POST':
        name = request.POST.get('name')
        icao_code = request.POST.get('icao_code')
        if Airport.objects.filter(icao_code=icao_code).exists():
            msg = "ICAO CODE Already Exists"
            return render(request, 'add/add_airport.html', {'msg': msg})
        data = Airport.objects.create(name=name, icao_code=icao_code)
        data.save()
        val1 = "Airport Name"
        val2 = "ICAO Code"
        msg = "you Have Created Successfully New Aircraft"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': name, 'var2': icao_code, 'val1': val1, 'val2': val2})

    return render(request, 'add/add_airport.html', {'msg': msg})


def add_flight(request):
    msg = "Add Flight"
    if request.method == 'POST':
        name = request.POST.get('name')
        if Flight.objects.filter(name=name).exists():
            msg = "Flight Name Already Exists!"
            return render(request, 'add/add_flight.html', {'msg': msg})
        data = Flight.objects.create(name=name)
        data.save()
        val1 = "Flight Name"
        msg = "you Have Created Successfully New Flight"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': name, 'val1': val1})

    return render(request, 'add/add_flight.html', {'msg': msg})


def add_management(request):
    msg = "Add Management Value"
    aircraft = Aircraft.objects.all()
    flight = Flight.objects.all()
    airport = Airport.objects.all()
    if request.method == 'POST':
        aircraft_id = request.POST.get('aircraft')
        flight_id = request.POST.get('flight')
        arrival_airport_id = request.POST.get('arrival_airport')
        departure_airport_id = request.POST.get('departure_airport')
        arrival_flight_date = request.POST.get('arrival_flight_date')
        arrival_flight_time = request.POST.get('arrival_flight_time')
        departure_flight_date = request.POST.get('departure_flight_date')
        departure_flight_time = request.POST.get('departure_flight_time')

        aircraft = Aircraft.objects.get(id=aircraft_id)
        flight = Flight.objects.get(id=flight_id)
        arrival_airport = Airport.objects.get(id=arrival_airport_id)
        departure_airport = Airport.objects.get(id=departure_airport_id)
        data = Management.objects.create(aircraft=aircraft, flight=flight, arrival_airport=arrival_airport,
                                         departure_airport=departure_airport,
                                         arrival_flight_date=arrival_flight_date,
                                         arrival_flight_time=arrival_flight_time,
                                         departure_flight_date=departure_flight_date,
                                         departure_flight_time=departure_flight_time)
        data.save()
        val1 = "Arrival Flight Date"
        val2 = "Departure Flight Date"
        msg = "you Have Created Successfully New Management Value"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': arrival_flight_date, 'var2': departure_flight_date, 'val1': val1,
                       'val2': val2})

    return render(request, 'add/add_management.html',
                  {'msg': msg, 'aircraft': aircraft, 'flight': flight, 'airport': airport})


def del_aircraft(request, slug):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    try:
        u = get_object_or_404(Aircraft, slug=slug)
        u.delete()
        msg = "Delete Data Has Been Successfully!"
        return render(request, 'error.html', {'msg': msg, 'u': u})

    except Aircraft.DoesNotExist:
        msg = "Data Not Found !"
        return render(request, 'error.html', {'msg': msg})

    except Exception as e:
        return render(request, 'error.html', {'err': e.message})


def del_airport(request, slug):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    try:
        u = get_object_or_404(Airport, slug=slug)
        u.delete()
        msg = "Delete Data Has Been Successfully!"
        return render(request, 'error.html', {'msg': msg, 'u': u})

    except Airport.DoesNotExist:
        msg = "Data Not Found !"
        return render(request, 'error.html', {'msg': msg})

    except Exception as e:
        return render(request, 'error.html', {'err': e.message})


def del_flight(request, slug):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    try:
        u = get_object_or_404(Flight, slug=slug)
        u.delete()
        msg = "Delete Data Has Been Successfully!"
        return render(request, 'error.html', {'msg': msg, 'u': u})

    except Flight.DoesNotExist:
        msg = "Data Not Found !"
        return render(request, 'error.html', {'msg': msg})

    except Exception as e:
        return render(request, 'error.html', {'err': e.message})


def del_management(request, id):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    try:
        u = get_object_or_404(Management, id=id)
        u.delete()
        msg = "Delete Data Has Been Successfully!"
        return render(request, 'error.html', {'msg': msg, 'u': u})

    except Management.DoesNotExist:
        msg = "Data Not Found !"
        return render(request, 'error.html', {'msg': msg})

    except Exception as e:
        return render(request, 'error.html', {'err': e.message})


def edit_aircraft(request, id):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    var = get_object_or_404(Aircraft, id=id)
    if request.method == 'POST':
        aircraft_name = request.POST.get('aircraft_name')
        manufacture = request.POST.get('manufacture')

        data = Aircraft.objects.get(id=id)
        data.aircraft_name = aircraft_name
        data.manufacture = manufacture

        data.save()
        val1 = "Aircraft Name"
        val2 = "Manufacture"
        msg = "you Have Updated Successfully Aircraft Details"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': aircraft_name, 'var2': manufacture, 'val1': val1, 'val2': val2})

    return render(request, 'edit/edit_aircraft.html', {'var': var})


def edit_airport(request, id):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    var = get_object_or_404(Airport, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        icao_code = request.POST.get('icao_code')

        data = Airport.objects.get(id=id)
        data.icao_code = icao_code
        data.name = name

        data.save()
        val1 = "Airport Name"
        val2 = "ICAO Code"
        msg = "you Have Updated Successfully Aircraft Details"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': name, 'var2': icao_code, 'val1': val1, 'val2': val2})

    return render(request, 'edit/edit_airport.html', {'var': var})


def edit_flight(request, id):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    var = get_object_or_404(Flight, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')

        data = Flight.objects.get(id=id)
        data.name = name

        data.save()
        val1 = "Flight Name"
        msg = "you Have Created Successfully New Flight"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': name, 'val1': val1})

    return render(request, 'edit/edit_flight.html', {'var': var})


def edit_management(request, id):
    # if not request.user.is_superuser:
    #     return redirect('login_attempt')
    var = get_object_or_404(Management, id=id)
    print(var.arrival_flight_date)
    aircraft = Aircraft.objects.all()
    flight = Flight.objects.all()
    airport = Airport.objects.all()
    if request.method == 'POST':
        aircraft_id = request.POST.get('aircraft')
        flight_id = request.POST.get('flight')
        arrival_airport_id = request.POST.get('arrival_airport')
        departure_airport_id = request.POST.get('departure_airport')
        arrival_flight_date = request.POST.get('arrival_flight_date')
        arrival_flight_time = request.POST.get('arrival_flight_time')
        departure_flight_date = request.POST.get('departure_flight_date')
        departure_flight_time = request.POST.get('departure_flight_time')

        aircraft = Aircraft.objects.get(id=aircraft_id)
        flight = Flight.objects.get(id=flight_id)
        arrival_airport = Airport.objects.get(id=arrival_airport_id)
        departure_airport = Airport.objects.get(id=departure_airport_id)

        data = Management.objects.get(id=id)
        data.aircraft = aircraft
        data.flight = flight
        data.arrival_airport = arrival_airport
        data.departure_airport = departure_airport
        data.arrival_flight_date = arrival_flight_date
        data.arrival_flight_time = arrival_flight_time
        data.departure_flight_date = departure_flight_date
        data.departure_flight_time = departure_flight_time

        data.save()
        val1 = "Arrival Flight Date"
        val2 = "Departure Flight Date"
        msg = "you Have Updated Successfully Management Details"
        return render(request, 'success.html',
                      {'msg': msg, 'var1': arrival_flight_date, 'var2': departure_flight_date, 'val1': val1,
                       'val2': val2})

    return render(request, 'edit/edit_management.html',
                  {'var': var, 'aircraft': aircraft, 'flight': flight, 'airport': airport})


