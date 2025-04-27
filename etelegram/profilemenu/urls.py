from django.urls import path
from .views import profile_view, edit_profile_view, portfolio_create_view

urlpatterns = [
    path('<int:id>', profile_view, name='profile'),
    path('edit/', edit_profile_view, name='edit_profile'),
    path('portfolio/create', portfolio_create_view, name='portfolio_create'),
]
