from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events, name='list-events'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('add_event/', views.add_event, name='add-event'),
    path('add_user/', views.add_user, name='add-user'),
    path('list_venues/', views.list_venues, name='list-venues'),
    path('show/<venue_id>', views.show_venue, name='show-venues'),
    path('search_v/', views.search_venue, name='search-venues'),
    path('update_venue/<venue_id>', views.venue_update, name='venue-update'),
    path('update_event/<event_id>', views.event_update, name='event-update'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('list_clubuser/', views.view_clubuser, name='list-clubuser'),
    path('update_userinfos/<event_id>',
         views.update_userinfos, name='update-userinfos'),
    path('show_user/<venue_id>', views.show_user, name='show-user'),
    path('delete_user/<venue_id>', views.delete_user, name='delete-user'),
]
