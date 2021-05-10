from django.shortcuts import render, redirect
from .models import Post
from datetime import date
import datetime

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('date_deadline')

    return render(request,'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date_created = request.POST['date_created'],
            date_deadline = request.POST['date_deadline'],
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return  render(request, 'detail.html', {'post':post})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        post = Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date_created = request.POST['date_created'],
            date_deadline = request.POST['date_deadline'],
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', { 'post' : post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')