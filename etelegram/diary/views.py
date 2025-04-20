from django.shortcuts import render

from django.shortcuts import render
from .models import Grade

def grades_list(request):
    grades = Grade.objects.select_related('user', 'subject').order_by( 'subject__name', 'date')
    return render(request, 'diary/grades_list.html', {'grades': grades})

