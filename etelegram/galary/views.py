from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Media
from django.http import HttpResponseForbidden

from .forms import MediaForm

@login_required
def media_add_view(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.author = request.user
            media.save()
            return redirect('media_list')
    else:
        form = MediaForm()
    return render(request, 'galary/media_add.html', {'form': form})




@login_required
def media_list_view(request):
    media = Media.objects.filter(verified = True)

    return render(request, 'galary/media_list.html', {'media_list': media})



def media_verify_view(request):
    if not request.user.is_staff:
        return render(request, 'base/403.html')
    else:
        media = Media.objects.filter(verified = False)

        return render(request, 'galary/media_verify_list.html', {'media_list': media})
