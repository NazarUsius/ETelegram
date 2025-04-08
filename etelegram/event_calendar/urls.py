from django.urls import path

from .import views

urlpatterns = [
    path('create-event/', views.create_event_view, name='create_event'),
    path('list-events/', views.list_events_view, name='list_events'),
]