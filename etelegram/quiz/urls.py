from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", QuizListView.as_view(), name = "quiz_list"),
    path("<int:pk>/", QuizDetailView.as_view(), name = "quiz_detail"),
    path("create/quiz/", QuizCreateView.as_view(), name = "quiz_create"),
    path("create/<int:pk>/section/", SectionCreateView.as_view(), name = "section_create"),
    path("create/<int:pk>/question/", QuestionCreateView.as_view(), name = "question_create"),
    path("create/<int:pk>/answer", AnswerCreateView.as_view(), name = "answer_create"),

]