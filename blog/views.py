from django.shortcuts import render
from .models import Post

def hello(request):
    return render(request, "blog/index.html")

def posts(request):
    post_list = Post.objects.all()
    context = {
        "Info":post_list
    }
    return render(request,'blog/posts.html',context=context)

def post_detail(request,id):
    post = Post.objects.get(id=id)
    context = {
        "post":post
    }
    return render(request,'blog/aaa.html',context=context)