from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#These are Python functions that define what happens when a user visits /signup/, /login/, or /logout/.

def landing_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # redirect if already logged in
    return render(request, 'accounts/landing.html')

def signup_view(request):
    '''Saves the user to your DB
    Logs them in immediately
    Redirects to a future dashboard page'''

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    '''On POST → it checks username/password
        If valid → logs the user in
        Redirects to dashboard
        Otherwise → re-renders login form with error messages'''
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    '''Clears the user's session and sends them back to login page'''
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')