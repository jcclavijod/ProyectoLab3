from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.vistaPaginaInicio, name='paginaInicio'),
    path('perfil/',views.vistaPerfil, name='perfil'),
    path('seguidos/',views.vistaSeguidos, name='seguidos'),
    path('seguidores/',views.vistaSeguidores, name='seguidores'),
    path('perfil/<str:username>/', views.vistaPerfil, name='perfil'),
    path('registro/',views.registro, name='registro'),
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('post/', views.post, name='post'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)