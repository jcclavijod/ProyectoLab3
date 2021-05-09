from django.shortcuts import render
from .models import *
# Create your views here.

def vistaPerfil(request):
    return render(request,'perfil.html')

def vistaPost(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'vistaPost.html',context)
