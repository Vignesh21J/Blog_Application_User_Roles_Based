from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from django.views.decorators.http import require_POST
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Disable user by default
            user.save()

            messages.success(request, "Your account has been created. Please wait for admin approval.")
            return redirect('login')
        
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {'form': form})

    form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})



@require_POST
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')