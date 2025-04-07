from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum_main, name = 'forum_main')
]