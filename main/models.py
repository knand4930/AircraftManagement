from random import randint
from django.db import models
from django.utils.text import slugify
from .utils import *


# Create your models here.
class Aircraft(models.Model):
    serial = models.CharField(max_length=20, blank=True, null=True, unique=True, editable=False,
                              default=generate_serial)
    manufacture = models.CharField(max_length=200, blank=True, null=True, unique=True)
    aircraft_name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if Aircraft.objects.filter(aircraft_name=self.aircraft_name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.aircraft_name) + "-" + extra
        else:
            self.slug = slugify(self.aircraft_name)
        super(Aircraft, self).save(*args, **kwargs)


class Airport(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    icao_code = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if Airport.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(Airport, self).save(*args, **kwargs)


class Flight(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=300, blank=True, null=True, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if Flight.objects.filter(name=self.name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(Flight, self).save(*args, **kwargs)


class Management(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, blank=True, null=True, related_name='aircraft +')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True, related_name='flight +')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='arrival airport +')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, blank=True, null=True,
                                          related_name='departure airport +')
    arrival_flight_date = models.DateField(blank=True, null=True)
    arrival_flight_time = models.TimeField(blank=True, null=True)
    departure_flight_date = models.DateField(blank=True, null=True)
    departure_flight_time = models.TimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

