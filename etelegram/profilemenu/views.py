from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm, PortfolioCreateForm
from .models import Portfolio, Portfolio_dislike, Portfolio_like
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404



User = get_user_model()



@login_required
def profile_view(request, id):
    user = get_object_or_404(User, pk=id)
    try:
        portfolio = Portfolio.objects.get(user=user, hided=False)
    except Portfolio.DoesNotExist:
        portfolio = None
    return render(request, 'profile/profile.html', {
        'user': user,
        'portfolio': portfolio,
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



@login_required
def portfolio_create_view(request):
    if request.method == 'POST':
        form = PortfolioCreateForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('profile', id=request.user.id)  

    else:
        form = PortfolioCreateForm()
    return render(request, 'profile/portfolio_create.html', {'form': form})


@login_required
def portfolio_hide_view(request):
        portfolio = get_object_or_404(Portfolio, user=request.user)
        portfolio.hided = True
        portfolio.save()
        return redirect('profile', id=request.user.id)  



@login_required
def portfolio_edit_view(request):
    portfolio = get_object_or_404(Portfolio, user=request.user)
    if request.method == 'POST':
        form = PortfolioCreateForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.save()
            return redirect('profile', id=request.user.id)  

    else:
        form = PortfolioCreateForm(instance=portfolio)
    return render(request, 'profile/portfolio_edit.html', {'form': form})


@login_required
def portfolio_like_view(request, portfolio_id):
        portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
        like, created = Portfolio_like.objects.get_or_create(
            author=request.user, portfolio=portfolio
        )   

        if not created: 
            like.delete()
        else:  
            Portfolio_dislike.objects.filter(
                author=request.user, portfolio=portfolio
            ).delete()

        return redirect("profile", id=request.user.id)


@login_required
def portfolio_dislike_view(request, portfolio_id):
        portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
        like, created = Portfolio_dislike.objects.get_or_create(
            author=request.user, portfolio=portfolio
        )   

        if not created:
            like.delete()
        else:  
            Portfolio_like.objects.filter(
                author=request.user, portfolio=portfolio
            ).delete()

        return redirect("profile", id=request.user.id)

    
    
