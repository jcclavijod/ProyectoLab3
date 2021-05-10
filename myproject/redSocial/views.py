from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def vistaPerfil(request):
    return render(request,'perfil.html')

def vistaPaginaInicio(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'paginaInicio.html',context)

def registro(request):
    if request.method == 'POST':
        form = formRegistro(request.POST)
        if form.is_valid():
            form.save()
            nombreUsuario = form.cleaned_data['username']
            messages.success(request, f'Usuario {nombreUsuario} creado')
            return redirect('paginaInicio')
    else:
        form = formRegistro()

    context = { 'form' : form }
    return render(request, 'registro.html', context)