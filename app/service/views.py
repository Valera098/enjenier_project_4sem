from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from service.forms import SignUpForm
from api.models import Resort

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(redirect_field_name='home')
def logout(request):
    LogoutView.as_view()(request)
    return redirect('home')

def login(request):
    if not request.user.is_authenticated:
        return LoginView.as_view()(request, template_name = "login.html", redirect = "home")
    return redirect('home')

def home(request):
    return render(request, 'resorts.html', {'resort': Resort.objects.all()})