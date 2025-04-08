from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import *


def landing_page(request):
    return render(request, 'landing.html')

def forum_main(request):
    posts = Post.objects.all()

    posts_data = []

    for post in posts:

        post_likes = LikePost.objects.filter(post=post)
        post_dislikes = DislikePost.objects.filter(post=post)
        post_comments = Comment.objects.filter(post=post)

        comment_likes = []
        comment_dislikes = []

        for comment in post_comments:
            comment_likes.append(LikeComment.objects.filter(comment=comment).count())
            comment_dislikes.append(DislikeComment.objects.filter(comment=comment).count())

        posts_data.append({
            'post': post,
            'likes': post_likes.count(),
            'dislikes': post_dislikes.count(),
            'comments': post_comments,
            'comment_likes': comment_likes,
            'comment_dislikes': comment_dislikes
        })

    return render(request, "forum.html", {"posts_data": posts_data})