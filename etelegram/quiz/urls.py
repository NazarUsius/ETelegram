from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", QuizListView.as_view(), name = "quiz_list"),
    path("<int:pk>/", QuizDetailView.as_view(), name = "quiz_detail"),
]