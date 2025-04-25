from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Media

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
    media = Media.objects.all()

    return render(request, 'galary/media_list.html', {'media_list': media})

            
