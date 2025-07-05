from django.shortcuts import render
from .models import Blog_project

def all_blogs(request):
    blogs = Blog_project.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blogs})