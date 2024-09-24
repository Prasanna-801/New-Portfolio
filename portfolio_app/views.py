from django.shortcuts import render

# Create your views here.
# portfolio_app/views.py
from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})
