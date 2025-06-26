from django.shortcuts import render
from .models import Project

def main_page(request):
    projects = Project.objects.all()
    return render(request, 'about_me/main.html', {'projects':projects})