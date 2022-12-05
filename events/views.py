from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .forms import VenueForm, EventForm, UserForm, EventFormAdmin
from django.http import HttpResponseRedirect
from .models import Venue, MyClubUser, Event


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    year = int(year)
    month = str(month).capitalize()
    # convert month from string to number
    month_number = int(list(calendar.month_name).index(month))
    # create calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get current year
    now = datetime.now()
    now = now.year
    current_time = datetime.now()
    current_time = current_time.strftime('%I:%M:%p')
    return render(request, 'events/home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'now': now,
        'current_time': current_time, })


def all_events(request):
    event = 'EVENTS'
    event_list = Event.objects.all().order_by('name')
    return render(request, 'events/event_list.html', {'event': event,
                                                      'event_list': event_list, })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            # form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form,
                                                     'submitted': submitted, })


# add event to database using form in template
def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            event = EventFormAdmin(request.POST)
        else:
            event = EventForm(request.POST)
        if event.is_valid():
            event.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        # Just visiting the site, not submitting form
        if request.user.is_superuser:
            event = EventFormAdmin(request.POST)
        else:
            event = EventForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'event': event,
                                                     'submitted': submitted, })


# add user to database using form in template
def add_user(request):
    submitted = False
    if request.method == "POST":
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect('/add_user?submitted=True')
    else:
        user = UserForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'events/add_user.html', {'user': user,
                                                    'submitted': submitted, })


# List all venues in database on a page
def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {
        'venue_list': venue_list, })


# selecting each venue with their unique id
def show_venue(request, venue_id):
    get_venue = Venue.objects.get(pk=venue_id)
    event = Event.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'get_venue': get_venue,
                                                      'event': event, })


# Search for venues in database
def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venue.html', {})


# Updating venues in database
def venue_update(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html', {'venue': venue,
                                                        'form': form, })


# update event
def event_update(request, event_id):
    singe_event = Event.objects.get(pk=event_id)
    event_form = EventForm(request.POST or None, instance=singe_event)
    if event_form.is_valid():
        event_form.save()
        return redirect('list-events')
    return render(request, 'events/update_events.html', {'singe_event': singe_event,
                                                         'event_form': event_form, })


# delete event from database
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return redirect('list_events')


# Add clubuser on website
def view_clubuser(request):
    users = MyClubUser.objects.all()
    return render(request, 'events/clubuser.html', {'users': users})


# Update user info
def update_userinfos(request, event_id):
    person = MyClubUser.objects.get(pk=event_id)
    person_form = UserForm(request.POST or None, instance=person)
    if person_form.is_valid():
        person_form.save()
        return redirect('list-clubuser')
    return render(request, 'events/userinfos_update.html', {'person': person,
                                                            'person_form': person_form, })


# select each user with their unique id nad view details
def show_user(request, venue_id):
    show_info = MyClubUser.objects.get(pk=venue_id)
    show_all = MyClubUser.objects.all()
    return render(request, 'events/show_user.html', {'show_info': show_info,
                                                     'show_all': show_all, })


# delete user from database
def delete_user(request, event_id):
    return redirect('list-clubuser',)
