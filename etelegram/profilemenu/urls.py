from django.urls import path
from .views import profile_view, edit_profile_view

urlpatterns = [
    path('<int:id>', profile_view, name='profile'),
    path('edit/', edit_profile_view, name='edit_profile'),
]
