from django.urls import path
from . import views

urlpatterns = [
    path('', views.grades_list, name='grades_list'),
    path('create/', views.grade_create, name='grade_create'),
    path('edit/<int:id>', views.grade_edit, name='grade_edit'),
    path('delete/<int:id>', views.grade_delete, name='grade_delete'),
]