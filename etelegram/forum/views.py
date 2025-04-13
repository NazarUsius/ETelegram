from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

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
    template_name = "forum.html"
    context_object_name = "posts_data"

    def get_context_data(self, **kwargs):
        branch = Branch.objects.all()
        branch_data = [get_post_data(i) for i in branch]
        return {"branch_data": branch_data}


class BranchDetailView(DetailView):
    model = Branch
    template_name = "branch_detail.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        post = self.get_object()
        data = get_post_data(post)
        context = super().get_context_data(**kwargs)
        context['data'] = data
        context['form'] = CommentForm()
        return context

class BranchCreateView(CreateView):
    model = Branch
    template_name = "branch_create.html"
    form_class = BranchForm

    def get_success_url(self):
        return reverse("branch_list")

class BranchUpdateView(UpdateView):
    model = Branch
    template_name = "branch_update.html"
    fields = ["title", "description"]

    def get_success_url(self):
        return reverse('branch_detail', kwargs={'pk': self.object.pk})

class BranchDeleteView(DeleteView):
    model = Branch
    template_name = "branch_detail.html"
    context_object_name = 'data'

    def get_success_url(self):
        return reverse('branch_list')

class CommentCreateView(CreateView):
    model = Comment
    template_name = "branch_detail"
    form_class = CommentForm

    def form_valid(self, form):
        branch = Branch.objects.get(pk=self.kwargs['pk'])
        form.instance.branch = branch
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('branch_detail', kwargs={'pk': self.kwargs['pk']})