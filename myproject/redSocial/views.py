from django.shortcuts import render

# Create your views here.

def vistaPost(request):
    return render(request,'vistaPost.html')

def perfil(request):
    return render(request,'perfil.html')