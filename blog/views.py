from django.shortcuts import render, get_object_or_404
from .models import Blog_project

def all_blogs(request):
    blogs = Blog_project.objects.all()
    #для ограничения постов писать order_by('-date')[:5] (сортировка по дате)
    return render(request,'blog/all_blogs.html',{'blogs':blogs})
def detail(request,blog_id):
    blog = get_object_or_404(Blog_project,pk = blog_id)
    return render(request,'blog/detail.html',{'blog':blog})