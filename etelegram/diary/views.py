from django.shortcuts import render, get_object_or_404, redirect

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
            return redirect('grades_list')


    else:
        form = GradeForm()
    return render(request, 'diary/grade_create.html', {'form': form})


def grade_edit(request, id):
    grade = get_object_or_404(Grade , pk=id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            old_grade = form.save()
            user = form.cleaned_data['user']
            subject = form.cleaned_data['subject']
            date = form.cleaned_data['date']
            evaluation_type = form.cleaned_data['evaluation_type']
            grade = form.cleaned_data['grade']
            old_grade.subject = subject
            old_grade.date = date
            old_grade.evaluation_type = evaluation_type
            old_grade.grade = grade
            old_grade.save()
            return redirect('grades_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'diary/grade_change.html', {'form': form, 'grade': grade})


def grade_delete(request, id):
    grade = get_object_or_404(Grade , pk=id)
    grade.delete()
    return redirect('grades_list')

