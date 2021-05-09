from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    contenido = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.usuario.username}: {self.contenido}'