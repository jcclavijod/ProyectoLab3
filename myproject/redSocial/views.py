from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def vistaPerfil(request, username=None):
    current_usuario = request.user
    if username and username != current_usuario.username:
        usuario = User.objects.get(username=username)
        posts = usuario.posts.all()
    else: 
        posts =current_usuario.posts.all()
        usuario = current_usuario
    return render(request,'perfil.html', {'usuario':usuario, 'posts':posts})


def follow(request, username): 
    current_usuario = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_usuario, to_user=to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('paginaInicio')

def unfollow(request, username):
    current_usuario = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_usuario.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('paginaInicio')


def vistaSeguidos(request):
    seguidos = Relationship.objects.all()
    context = {'seguidos': seguidos}
    return render(request, 'seguidos.html', context)

def vistaPaginaInicio(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request,'paginaInicio.html',context)

@login_required
def post(request):
    current_usuario = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = current_usuario
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('paginaInicio')
    else:
            form=PostForm()
    return render(request,'post.html', {'form': form})

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


