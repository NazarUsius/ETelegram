from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render

from .forms import GradeForm, GradeFilterForm
from .models import Grade

def grades_list(request):
    form = GradeFilterForm(request.GET or None)
    sort_by = request.GET.get('sort', 'date')
    grades = Grade.objects.select_related('user', 'subject').only('user', 'subject', 'grade', 'date')
    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        evaluation_type = form.cleaned_data.get('evaluation_type')
        date_from = form.cleaned_data.get('date_from')

        if subject:
            grades = grades.filter(subject=subject)
        if evaluation_type:
            grades = grades.filter(evaluation_type=evaluation_type)
        if date_from:
            grades = grades.filter(date__gte=date_from)
    average = "Can not count"
    if len(grades) != 0:
        sum = 0
        for i in grades:
            sum += i.grade
        average = sum/len(grades)
    return render(request, 'diary/grades_list.html', {'grades': grades, 'average': average, "form": form})
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

