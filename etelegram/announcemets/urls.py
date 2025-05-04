from django.urls import path
from .views import announcement_list

urlpatterns = [
    path('', announcement_list, name='announcement_list'),
]
