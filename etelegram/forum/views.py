from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def landing_page(request):
    return render(request, 'landing.html')

def get_post_data(branch):
    branch_likes = LikeBranch.objects.filter(branch=branch)
    branch_dislikes = DislikeBranch.objects.filter(branch=branch)
    branch_comments = Comment.objects.filter(branch=branch)

    comments_data = []

    for comment in branch_comments:
        comment_likes = LikeComment.objects.filter(comment=comment).count()
        comment_dislikes = DislikeComment.objects.filter(comment=comment).count()

        comments_data.append({
            'comment': comment,
            'like_count': comment_likes,
            'dislike_count': comment_dislikes
        })
    #form = CommentForm()

    return {
        'branch': branch,
        #'form': form,
        'likes': branch_likes.count(),
        'dislikes': branch_dislikes.count(),
        'comments': comments_data
    }

class BranchListView(ListView):
    model = Branch
    template_name = "forum/forum.html"
    context_object_name = "posts_data"

    def get_context_data(self, **kwargs):
        branch = Branch.objects.all()
        branch_data = [get_post_data(i) for i in branch]
        return {"branch_data": branch_data}


class BranchDetailView(LoginRequiredMixin, DetailView):
    model = Branch
    template_name = "forum/branch_detail.html"
    context_object_name = "data"
    login_url = "/accounts/login/"

    def get_context_data(self, **kwargs):
        post = self.get_object()
        data = get_post_data(post)
        context = super().get_context_data(**kwargs)
        context['data'] = data
        context['form'] = CommentForm()
        context['user'] = self.request.user
        return context

class BranchCreateView(UserPassesTestMixin, CreateView):
    model = Branch
    template_name = "forum/branch_create.html"
    form_class = BranchForm
    login_url = "/accounts/login/"

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse("branch_list")

class BranchUpdateView(UserPassesTestMixin, UpdateView):
    model = Branch
    template_name = "forum/branch_update.html"
    fields = ["title", "description"]
    login_url = "/accounts/login/"

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('branch_detail', kwargs={'pk': self.object.pk})

class BranchDeleteView(UserPassesTestMixin, DeleteView):
    model = Branch
    template_name = "forum/branch_detail.html"
    context_object_name = 'data'
    login_url = "/accounts/login/"

    def get_context_data(self, **kwargs):
        post = self.get_object()
        data = get_post_data(post)
        context = super().get_context_data(**kwargs)
        context['data'] = data
        context['form'] = CommentForm()
        return context

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse('branch_list')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "forum/branch_detail"
    form_class = CommentForm
    login_url = "/accounts/login/"

    def form_valid(self, form):
        branch = Branch.objects.get(pk=self.kwargs['pk'])
        form.instance.branch = branch
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('branch_detail', kwargs={'pk': self.kwargs['pk']})


class LikeBranchCreateView(LoginRequiredMixin, CreateView):
    model = LikeBranch
    form_class = LikeBranchForm
    template_name = "branch_detail.html"
    login_url = "/accounts/login/"

    def form_valid(self, form):
        branch = get_object_or_404(Branch, pk=self.kwargs['pk'])

        if LikeBranch.objects.filter(user=self.request.user, branch=branch).exists():
            return HttpResponseForbidden("You have already liked this branch.")
        form.instance.user = self.request.user
        form.instance.branch = branch

        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('branch_detail', kwargs={'pk': self.kwargs['pk']})