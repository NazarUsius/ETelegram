from django.urls import path
from .views import profile_view, edit_profile_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
]
