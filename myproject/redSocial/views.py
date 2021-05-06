from django.shortcuts import render

# Create your views here.

def vistaPost(request):
    return render(request,'paginas/vistaPost.html')

def perfil(request):
    return render(request,'paginas/perfil.html')