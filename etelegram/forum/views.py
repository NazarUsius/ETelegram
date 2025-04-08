from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


def landing_page(request):
    return render(request, 'landing.html')

class PostListView(ListView):
    model = Post
    template_name = "forum.html"
    context_object_name = "posts_data"

    def get_context_data(self, **kwargs):
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
        return {"posts_data": posts_data}

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "data"

    def get_context_data(self, **kwargs):
        post = self.get_object()

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

        context = {
            "data": {
                'post': post,
                'likes': post_likes.count(),
                'dislikes': post_dislikes.count(),
                'comments': comments_data
            }
        }

        return context
