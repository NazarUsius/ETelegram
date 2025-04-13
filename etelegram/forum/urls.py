from django.urls import path
from . import views
from .views import BranchListView, BranchDetailView, BranchCreateView, BranchUpdateView, BranchDeleteView, CommentCreateView

urlpatterns = [
    path("", BranchListView.as_view(), name = 'branch_list'),
    path("<int:pk>/", BranchDetailView.as_view(), name = "branch_detail"),
    path("create/", BranchCreateView.as_view(), name = "branch_create"),
    path("<int:pk>/update/", BranchUpdateView.as_view(), name = "branch_update"),
    path("<int:pk>/delete", BranchDeleteView.as_view(), name = "branch_delete"),
    #path("<int:pk>/like", LikePostCreateView.as_view(), name = "like_post"),
    path('forum/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]