from django.urls import path

import views

urlpatterns = [
    path('', views.landing_page, name='index'),
]