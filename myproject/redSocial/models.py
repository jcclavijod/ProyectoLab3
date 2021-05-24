from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save


# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='batman.png')

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.usuario)\
                                                        .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.usuario)\
                                                        .values_list('from_user_id', flat=True)
        return User.objects.filter(id_in=user_ids)

class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    contenido = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.usuario.username}: {self.contenido}'

class Relationship(models.Model):
    from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'

    class Meta:
        indexes = [
            models.Index(fields=['from_user', 'to_user',]),
            ]