from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Post

def landing_page(request):
    return render(request, 'landing.html')

def forum_main(request):
    posts = Post.objects.all()
    return render(request, "forum.html", {"posts": posts})
