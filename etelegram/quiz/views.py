from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse

def get_quiz_data(quiz):
    return {
        "quiz": quiz
    }

class QuizListView(ListView):
    model = Quiz
    template_name = "quiz.html"
    context_object_name = "quiz_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quizzes = Quiz.objects.all()
        quiz_data = [{"quiz": q} for q in quizzes]
        context["quiz_data"] = quiz_data
        return context


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz_detail.html"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()
        data = get_quiz_data(quiz)
        context["quiz"] = quiz
        context["data"] = data
        return context

class QuizCreateView(CreateView):
    model = Quiz
    template_name = "quiz_create.html"
    form_class = QuizForm
    success_url = '/quiz/'

    def get_success_url(self):
        return reverse("quiz_list")

class SectionCreateView(CreateView):
    model = Section
    template_name = "section_create.html"
    form_class = SectionForm
    success_url = '/quiz/'

    def form_valid(self, form):
        quiz = Quiz.objects.get(pk=self.kwargs['pk'])
        form.instance.quiz = quiz
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_list")


class QuestionCreateView(CreateView):
    model = Question
    template_name = "question_create.html"
    form_class = QuestionForm
    success_url = '/quiz/'

    def form_valid(self, form):
        section = Section.objects.get(pk=self.kwargs['pk'])
        form.instance.section = section
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_list")

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "answer_create.html"
    form_class = AnswerForm
    success_url = '/quiz/'

    def form_valid(self, form):
        question = Question.objects.get(pk=self.kwargs['pk'])
        form.instance.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_list")




