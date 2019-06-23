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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Blog.objects.get(pk=blog_id)
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm()
    return render(request, 'blog_form.html', {'form': form,})