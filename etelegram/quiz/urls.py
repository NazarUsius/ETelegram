from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", QuizListView.as_view(), name="quiz_list"),
    path("<int:pk>/", QuizDetailView.as_view(), name="quiz_detail"),
    path("create/quiz/", QuizCreateView.as_view(), name="quiz_create"),
    path("create/<int:quiz_pk>/section/", SectionCreateView.as_view(), name="section_create"),
    path("create/<int:quiz_pk>/section/<int:section_pk>/question/", QuestionCreateView.as_view(), name="question_create"),
    path("quiz/create/<int:quiz_pk>/section/<int:section_pk>/question/<int:question_pk>/answer/", AnswerCreateView.as_view(), name="answer_create"),
    path("<int:pk>/setting/", QuizSettingView.as_view(), name="quiz_setting"),
]
