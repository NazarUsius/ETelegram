from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profile_view, name='profile'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('portfolio/create', views.portfolio_create_view, name='portfolio_create'),
    path('portfolio/hide', views.portfolio_hide_view, name='portfolio_hide'),
]
