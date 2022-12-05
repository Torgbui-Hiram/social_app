from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Venue(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    contact = models.CharField(max_length=20)
    web = models.URLField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField(max_length=50, blank=True)
    event_date = models.DateTimeField(max_length=20, blank=True)
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    attendee = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
