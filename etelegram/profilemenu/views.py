from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile/profile.html', {
        'user': user
    })

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'form': form,
        'user': request.user, 
    }
    return render(request, 'profile/edit_profile.html', context)