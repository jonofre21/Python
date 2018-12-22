#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from .models import Post
from .forms import PostForm

def index(request):
    return HttpResponse("Hello Worldpython")

def preview(request):
        posts = Post.objects.all()
        return render(request, "myapp/blog.html", {'posts':posts})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return HttpResponse("thanks !!!")
    form = PostForm()
    return render(request, "myapp/new.html", {'form':form})
