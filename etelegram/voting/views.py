from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect
from .forms import *
from django.conf import settings

class VotingListView(ListView):
    model = Voting
    template_name = "voting/voting_list.html"
    context_object_name = "voting_data"

class VotingCreateView(CreateView):
    model = Voting
    template_name = "voting/voting_create.html"
    form_class = VotingForm
    success_url = '/voting/'

    def get_success_url(self):
        return reverse("voting_settings", kwargs={"pk": self.object.pk})

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "voting/answer_create.html"
    form_class = AnswerForm
    success_url = '/voting/'

    def form_valid(self, form):
        voting = Voting.objects.get(pk=self.kwargs['voting_pk'])
        form.instance.voting = voting
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("voting_settings", kwargs={"pk": self.kwargs['voting_pk']})

class VotingDetailView(DetailView):
    model = Voting
    template_name = "voting/voting_detail.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        context["data"] = data
        return context

class VotingSettingsView(DetailView):
    model = Voting
    template_name = "voting/voting_settings.html"
    context_object_name = "voting"

def start_voting(request, voting_id):
    voting = get_object_or_404(Voting, id = voting_id)
    session = Session.objects.create(user=request.user, voting=voting)
    return redirect("voting", session_id=session.id)

def voting(request, session_id):
    session = get_object_or_404(Session, id=session_id, user=request.user)
    voting = session.voting
    answers = voting.answers.all()

    if request.method == "POST":
        for answer in answers:
            selected_answer = request.POST.get(f"answer_{answer.id}")
            if selected_answer:
                UserAnswer.objects.create(user = request.user, answer = answer)

        return redirect("results", session_id = session.id)

    return render(request, 'voting/voting.html', {
        'session': session,
        'voting': voting,
        'answers': answers,
    })

def results(request, session_id):
    session = get_object_or_404(Session, id=session_id, user=request.user)
    user_answers = UserAnswer.objects.filter(user=request.user, answer__voting=session.voting)


    return render(request, 'voting/results.html', {
        'session': session,
        'user_answers': user_answers,
    })





