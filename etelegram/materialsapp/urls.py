from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('list/', views.material_list ,name = 'material_list'),
    path('delete/<int:pk>', views.material_delete ,name = 'material_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)