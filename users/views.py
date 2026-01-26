from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from django.views.decorators.http import require_POST
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashboard')
        
        messages.error(
            request,
            "Invalid username or password. Please try again."
        )
        return redirect('login')
        
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@require_POST
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')