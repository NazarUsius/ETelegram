from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group

@login_required
def home_view(request):
    groups = Group.objects.all().prefetch_related('user_set')
    return render(request, 'main.html', {'groups': groups})

def landing_page(request):
    return render(request, 'landing.html')
