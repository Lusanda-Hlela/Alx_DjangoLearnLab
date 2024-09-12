# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, UserProfileForm


def home(request):
  return render(request, "blog/base.html")


def posts(request):
  return render(request, "blog/base.html")


# Registration view
def register(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get("username")
      messages.success(request, f"Account created for {username}!")
      return redirect("login")
  else:
    form = CustomUserCreationForm()
  return render(request, "blog/register.html", {"form": form})


# Login view
def login_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, f"Logged in as {username}")
        return redirect("home")
      else:
        messages.error(request, "Invalid username or password")
    else:
      messages.error(request, "Invalid username or password")
  form = AuthenticationForm()
  return render(request, "blog/login.html", {"form": form})


# Logout view
def logout_view(request):
  logout(request)
  messages.success(request, "Logged out successfully")
  return redirect("home")


# Profile view
@login_required
def profile(request):
  if request.method == "POST":
    form = UserProfileForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, "Your profile has been updated!")
      return redirect("profile")
  else:
    form = UserProfileForm(instance=request.user)
  return render(request, "blog/profile.html", {"form": form})
