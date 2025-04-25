from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.media_list_view ,name = 'media_list'),
    path('add/', views.media_add_view ,name = 'media_add'),
    path('verify/', views.media_verify_view ,name = 'media_verify'),
    path('verify/<int:media_id>', views.verify_media ,name = 'verify_media'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)