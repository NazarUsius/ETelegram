from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm


@login_required
def profile_view(request):
    user = request.user
    profile = user.profile
    return render(request, 'profile/profile.html', {
        'user': user,
        'profile': profile
    })

@login_required
def edit_profile_view(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # замени на имя своего URL
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form})