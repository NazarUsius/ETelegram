from django.shortcuts import render
from .models import Announcement

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcements/list.html', {'announcements': announcements})
