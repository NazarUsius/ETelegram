from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect


def get_quiz_data(quiz):
    return {
        "quiz": quiz
    }

class QuizListView(ListView):
    model = Quiz
    template_name = "quiz/quiz.html"
    context_object_name = "quiz_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quizzes = Quiz.objects.all()
        quiz_data = [{"quiz": q} for q in quizzes]
        context["quiz_data"] = quiz_data
        return context


class QuizDetailView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_detail.html"
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
    template_name = "quiz/quiz_create.html"
    form_class = QuizForm
    success_url = '/quiz/'

    def get_success_url(self):
        return reverse("quiz_setting", kwargs={"pk": self.object.pk})

class SectionCreateView(CreateView):
    model = Section
    template_name = "quiz/section_create.html"
    form_class = SectionForm
    success_url = '/quiz/'

    def form_valid(self, form):
        quiz = Quiz.objects.get(pk=self.kwargs['quiz_pk'])
        form.instance.quiz = quiz
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_setting", kwargs={'pk': self.kwargs['quiz_pk']})


class QuestionCreateView(CreateView):
    model = Question
    template_name = "quiz/question_create.html"
    form_class = QuestionForm
    success_url = '/quiz/'

    def form_valid(self, form):
        section = Section.objects.get(pk=self.kwargs['section_pk'])
        form.instance.section = section
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_setting", kwargs={'pk': self.kwargs['quiz_pk']})

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "quiz/answer_create.html"
    form_class = AnswerForm
    success_url = '/quiz/'

    def form_valid(self, form):
        question = Question.objects.get(pk=self.kwargs['question_pk'])
        form.instance.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("quiz_setting", kwargs={'pk': self.kwargs['quiz_pk']})


class QuizSettingView(DetailView):
    model = Quiz
    template_name = "quiz/quiz_setting.html"
    context_object_name = "quiz"

#answering the test

def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    session = Session.objects.create(user = request.user, quiz = quiz)
    first_section = quiz.section_set.first()
    return redirect('section_view', session_id=session.id, section_id=first_section.id)


KINDS_OF_ANSWER = {"c": "Correct", "i": "Incorrect"}


def section_view(request, session_id, section_id):
    session = get_object_or_404(Session, id=session_id, user=request.user)
    section = get_object_or_404(Section, id=section_id, quiz=session.quiz)
    questions = section.question_set.prefetch_related('answer_set')
    correct_answers = 0
    incorrect_answers = 0
    total_questions = questions.count()

    if request.method == 'POST':
        for question in questions:
            if question.kind == "c":
                selected_answer_id = request.POST.get(f"question_{question.id}")
                if selected_answer_id:
                    selected_answer = Answer.objects.get(id=selected_answer_id)

                    if selected_answer.correctness == "c":
                        correct_answers += 1
                    else:
                        incorrect_answers += 1

                    UserAnswer.objects.update_or_create(
                        session=session,
                        question=question,
                        defaults={'selected_answer_id': selected_answer.id}
                    )

        next_section = Section.objects.filter(quiz=session.quiz, id__gt=section.id).first()
        if next_section:
            return redirect('section_view', session_id=session.id, section_id=next_section.id)
        else:
            session.finished_at = timezone.now()
            session.save()
            return redirect('quiz_result', session_id=session.id)

    return render(request, 'quiz/section.html', {
        'section': section,
        'questions': questions,
        'session': session
    })


def quiz_result(request, session_id):
    session = get_object_or_404(Session, id = session_id, user = request.user)
    answers = UserAnswer.objects.filter(session = session)
    correct_count = sum(1 for ans in answers if ans.selected_answer and ans.selected_answer.correctness == "c")
    total = answers.count()

    return render(request, 'quiz/test_result.html', {
        'correct': correct_count,
        'total': total,
    })


