from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    # Mostramos el nombre de la categoría en lugar del ID numérico en el JSON para facilitarle la vida al Frontend
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 
            'categoria', 
            'categoria_nombre', 
            'nombre', 
            'descripcion', 
            'precio', 
            'stock', 
            'imagen', 
            'fecha_creacion'
        ]