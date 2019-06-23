from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from .forms import CommentForm
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_object})

def comment_new(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    comment = Comment()
    comment.post = post
    comment.author = request.POST['author']
    comment.text = request.POST['body']
    comment.save()
    return render(request, 'detail.html', {'blog': post})