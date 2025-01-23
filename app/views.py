from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, SignupForm, ChangePasswordForm, UpdateProfileForm


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username_or_email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Invalid username/email or password.")
    return render(request, 'app/login.html', {'form': form})


def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'app/signup.html', {'form': form})


@login_required
def change_password_view(request):
    form = ChangePasswordForm(user=request.user)
    if request.method == "POST":
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successfully!")
            return redirect('dashboard')
    return render(request, 'app/change_password.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'app/dashboard.html', {'username': request.user.username})


@login_required
def profile_view(request):
    form = UpdateProfileForm(instance=request.user)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('dashboard')
    return render(request, 'app/profile.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
