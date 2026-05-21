from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Orden(models.Model):
    # Opciones predefinidas para el estado del pedido
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ordenes', verbose_name="Cliente")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Orden")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente', verbose_name="Estado del Pedido")
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Total a Pagar")

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"


class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='detalles')
    # Usamos PROTECT para que no se pueda borrar un Funko si ya está registrado en una compra histórica
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, verbose_name="Funko")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")

    class Meta:
        verbose_name = "Detalle de Orden"
        verbose_name_plural = "Detalles de Orden"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Orden #{self.orden.id})"