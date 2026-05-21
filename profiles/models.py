from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Relación uno a uno con el usuario nativo de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, verbose_name="Biografía")
    # Aquí se subirá la foto selfie de referencia desde el admin
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Foto de Referencia FaceID")
    created = models.DateTimeField(auto_now_add=True)
    biometria_facial = models.TextField(blank=True, null=True, verbose_name="Datos del Rostro (JSON)")


    def __str__(self):
        return f"Perfil de {self.user.username}"