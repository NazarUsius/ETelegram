from django.urls import path
from .views import AddListView, AddCreateView, ApproveListView, ApproveUpdateView

urlpatterns = [
    path('', AddListView.as_view(), name='add_list'),
    path('create/', AddCreateView.as_view(), name='add_create'),
    path('approve/', ApproveListView.as_view(), name='approve_list'),
    path('approve/<int:pk>/', ApproveUpdateView.as_view(), name='approve_update'),
]
