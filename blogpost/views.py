from django.shortcuts import render, redirect
from .models import Post

def posts(request):
    posts = Post.objects.all().order_by("-created_at")[:10]
    
    context = {
        'posts': posts
    }
    return render(request, 'blogpost/index.html', context)

def details(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blogpost/details.html', context)