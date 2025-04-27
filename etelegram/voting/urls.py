from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", VotingListView.as_view(), name = "voting_list"),
    path("create/", VotingCreateView.as_view(), name = "voting_create"),
    path("<int:voting_pk>/answer/create/", AnswerCreateView.as_view(), name="answer_create"),
    path("<int:pk>/settings/", VotingSettingsView.as_view(), name = "voting_settings"),
    path("<int:pk>/", VotingDetailView.as_view(), name = "voting_detail"),
    path('<int:voting_id>/start/', views.start_voting, name='start_voting'),
    path('session/<int:session_id>/questions/', views.voting, name='voting'),
    path('session/<int:session_id>/results/', views.results, name='results'),
]