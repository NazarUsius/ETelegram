from django.urls import path
from . import views

urlpatterns = [
    path('', views.grades_list, name='grades_list'),
    path('create/', views.grade_create, name='grade_create'),
]