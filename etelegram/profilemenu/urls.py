from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.profile_view, name='profile'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('portfolio/create', views.portfolio_create_view, name='portfolio_create'),
    path('portfolio/hide', views.portfolio_hide_view, name='portfolio_hide'),
    path('portfolio/edit', views.portfolio_edit_view, name='portfolio_edit'),
    path('portfolio/like/<int:portfolio_id>/', views.portfolio_like_view, name='portfolio_like'),
    path('portfolio/dislike/<int:portfolio_id>/', views.portfolio_dislike_view, name='portfolio_dislike'),
]
