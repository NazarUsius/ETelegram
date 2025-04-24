from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group

def home_view(request):
    groups = Group.objects.all().prefetch_related('user_set')
    return render(request, 'main.html', {'groups': groups})

