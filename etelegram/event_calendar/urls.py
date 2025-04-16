from django.urls import path

from .import views

urlpatterns = [
    path('create/', views.create_event_view, name='create_event'),
    path('list/', views.list_events_view, name='list_events'),
    path('delete/<str:event_id>/', views.delete_event_view, name='delete_event'),
]