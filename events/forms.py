from django import forms
from django.forms import ModelForm
from .models import Venue, Event, MyClubUser


class VenueForm(ModelForm):
    class Meta:
        model = Venue

        fields = ('name', 'address', 'location',
                  'contact', 'web', 'telephone', 'email',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Address'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue location'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Contact'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Web Address'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Venue Email'}),
        }
        labels = {'name': '',
                  'address': '',
                  'location': '',
                  'contact': '',
                  'web': '',
                  'telephone': '',
                  'email': '', }

# Admin Event form


class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue',
                  'manager', 'description', 'attendee')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Event Name'}),
                   'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Event Date'}),
                   'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please Event Name'}),
                   'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Event Manager Name'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
                   'attendee': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Names Of Attendees'}), }

        labels = {'name': '',
                  'event_date': 'YYY-MM-DD HH:MM:SS',
                  'venue': 'Event Venue:',
                  'manager': 'Event Manager:',
                  'description': '',
                  'attendee': '', }


# Other user form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'description', 'attendee')

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Event Name'}),
                   'event_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter Event Date'}),
                   'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please Event Name'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}),
                   'attendee': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Names Of Attendees'}), }

        labels = {'name': '',
                  'event_date': 'YYY-MM-DD HH:MM:SS',
                  'venue': 'Event Venue:',
                  'description': '',
                  'attendee': '', }


class UserForm(ModelForm):
    class Meta:
        model = MyClubUser

        fields = ('first_name', 'last_name', 'phone')

        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Your First Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Your Last Name'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter Your Phone Number'}), }

        labels = {'first_name': '',
                  'last_name': '',
                  'phone': '', }
