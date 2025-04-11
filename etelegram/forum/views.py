from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


def landing_page(request):
    return render(request, 'landing.html')

def get_post_data(post):
    post_likes = LikePost.objects.filter(post=post)
    post_dislikes = DislikePost.objects.filter(post=post)
    post_comments = Comment.objects.filter(post=post)

    comments_data = []

    for comment in post_comments:
        comment_likes = LikeComment.objects.filter(comment=comment).count()
        comment_dislikes = DislikeComment.objects.filter(comment=comment).count()

        comments_data.append({
            'comment': comment,
            'like_count': comment_likes,
            'dislike_count': comment_dislikes
        })

    return {
        'post': post,
        'likes': post_likes.count(),
        'dislikes': post_dislikes.count(),
        'comments': comments_data
    }

class PostListView(ListView):
    model = Post
    template_name = "forum.html"
    context_object_name = "posts_data"

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()

        # Using get_post_data to clean up code repetition
        posts_data = [get_post_data(post) for post in posts]

        return {"posts_data": posts_data}


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        post = self.get_object()

        return {'data': get_post_data(post)}