from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    Posts=Post.objects.all()
    return render(request,'index.html',{'Posts':Posts})

def poster(request,pk):
    post=Post.objects.get(id=pk)
    return render(request,'poster.html',{'post':post})