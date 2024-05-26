from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from pharma_app.models import Profile
from pharma_app.forms import ProfileForm
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from .forms import User, UserChangeForm


User = get_user_model()


@login_required
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login")
    
    profile = get_object_or_404(Profile, user=request.user.id)

    return render(request, 'registration/profile.html', {'profile' : profile})

def not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(not_authenticated)
def create_account(request):
    # They are logged in, they cannot create an account
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = User.objects.get(username=user)
            print("USER ++++++++++++++++++++",( user_profile , user_profile.id, user_profile.username))
            p = Profile(user=user_profile,u_name=user_profile.username)
            p.save()
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
            return redirect('accounts:profile')

    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'registration/change_profile.html', { 'form': form })


# from django.contrib.auth import logout
# def logout_view(request):
#     logout(request)
    
#     return redirect('accounts:login')
    # return render(request, 'pharma_app/index.html', {'profile': profile})
# Redirect to a success page.