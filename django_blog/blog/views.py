# blog/views.py

from django.shortcuts import render

def home(request):
  return render(request, 'blog/base.html')

def posts(request):
  return render(request, 'blog/base.html')

def login_view(request):
  return render(request, 'blog/base.html')

def register(request):
  return render(request, 'blog/base.html')

