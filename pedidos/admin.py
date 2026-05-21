from django.contrib import admin
from .models import Orden, DetalleOrden

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 0  # No muestra filas vacías adicionales por defecto

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_creacion', 'estado', 'total')
    list_filter = ('estado', 'fecha_creacion')
    search_fields = ('usuario__username',)
    inlines = [DetalleOrdenInline] # Integramos los detalles visualmente acá