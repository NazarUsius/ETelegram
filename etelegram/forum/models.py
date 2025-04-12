from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    media = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post: {self.title} -> {self.description}"


class LikePost(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="liked_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on post: {self.post.title}"


class DislikePost(models.Model):
    post = models.ForeignKey(Post, related_name="dislikes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="disliked_posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dislike by {self.user.username} on post: {self.post.title}"


class Comment(models.Model):
    description = models.TextField(max_length=100)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.title}"


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="liked_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.username} on comment: {self.comment.description}"


class DislikeComment(models.Model):
    comment = models.ForeignKey(Comment, related_name="dislikes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="disliked_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dislike by {self.user.username} on comment: {self.comment.description}"