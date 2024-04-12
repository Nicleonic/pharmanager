from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import UserChangeForm

@login_required
def user_profile(request):
    return render(request, 'registration/profile.html')


def create_account(request):
    # They are logged in, they cannot create an account
    if request.user.is_authenticated:
        return redirect('account:profile')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/create_account.html', { 'form': form })

@login_required
def change_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('account:profile')

    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'registration/change_profile.html', { 'form': form })