from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import CustomUserCreationForm
from django.contrib import messages

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.user.is_authenticated:
                messages.success(request, 'Вы успешно зарегистрировались!')
                return redirect('index')
            else:
                messages.error(request, 'Ошибка при авторизации!')
                return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


