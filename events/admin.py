from django.contrib import admin
from .models import Event, Venue, MyClubUser


@admin.register(Event)
class EventAadmin(admin.ModelAdmin):
    list_display = ('name', 'event_date', 'venue',
                    'manager', 'description')
    ordering = ('name',)
    search_fields = ('name', 'venue',)
    fields = (('name', 'event_date'), 'venue', 'description', 'manager')
    list_filter = ('event_date', 'name', 'venue',)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'location', 'contact', 'owner')
    ordering = ('name',)
    search_fields = ('name', 'location',)
    fields = (('name', 'location'), 'address', 'contact')
    list_filter = ('name', 'location', 'address',)


@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('first_name', 'last_name',)
