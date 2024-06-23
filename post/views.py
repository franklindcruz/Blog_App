from django.shortcuts import render,redirect
from .forms import CreateForm
from .models import Post
# Create your views here.
def index(request):
    post=Post.objects.all()
    return render(request, 'index.html',{'posts':post})


def post(request):
    form=CreateForm()
    if request.method=='POST':
        form=CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=CreateForm()   
    return render(request, 'post.html', {'form':form})

def post_description(request,id):
    post=Post.objects.get(id=id)
    return render(request, 'post_description.html',{'post':post})


def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('home')
