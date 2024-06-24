from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateForm,CustomUserCreationForm
from .models import Post, Demo
# Create your views here.


def demohome(request):
    return render(request, 'demo.html')


def demo(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        demo = Demo(title=title, content=content, image=image)
        demo.save()
        success = 'New blog' + title+'created successfully'
        return HttpResponse(success)
    return render(request, 'demo.html')

def register(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')
   
    return render(request, 'register.html', {'form': form})


@login_required
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})


@login_required
def post(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = CreateForm()
    return render(request, 'post.html', {'form': form})


def post_description(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_description.html', {'post': post})


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')


def edit_post(request, id):
    post = Post.objects.get(id=id)
    form = CreateForm(instance=post)
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_description', id=id)
        else:
            form = CreateForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'instance': post})
