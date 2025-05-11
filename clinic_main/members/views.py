from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
# Create your views here.
from .forms import PatientSignUpForm

def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.username = user.email
                user.save()
                login(request, user)
                return redirect('profile_redirect')
            except IntegrityError:
                form.add_error('email', 'Этот email уже занят')
    else:
        form = PatientSignUpForm()
    return render(request, 'clients/register.html', {'form': form})
