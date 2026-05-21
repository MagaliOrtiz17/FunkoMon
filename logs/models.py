from django.db import models
from profiles.models import Profile

class Log(models.Model):
    # Guardamos el perfil si se reconoce, si no, queda en null (intento fallido/desconocido)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Perfil Detectado")
    # La captura que envió el frontend en ese instante
    photo = models.ImageField(upload_to='logs/', verbose_name="Captura de Intento")
    is_correct = models.BooleanField(default=False, verbose_name="Acceso Permitido")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log de Autenticación #{self.id} - Autorizado: {self.is_correct}"