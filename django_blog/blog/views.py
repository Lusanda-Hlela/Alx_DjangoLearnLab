from django.shortcuts import render

# Create your views here.


def index(request):
  return render(
    request, "blog/index.html"
  )  # Make sure the path matches your template folder
