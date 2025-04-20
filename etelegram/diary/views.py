from django.shortcuts import render

from django.shortcuts import render

from .forms import GradeForm
from .models import Grade

def grades_list(request):
    grades = Grade.objects.select_related('user', 'subject').order_by( 'subject__name', 'date')
    return render(request, 'diary/grades_list.html', {'grades': grades})

def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data['user']
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            evaluation_type = form.cleaned_data['evaluation_type']
            grade = form.cleaned_data['grade']


    else:
        form = GradeForm()
    return render(request, 'diary/grade_create.html', {'form': form})
