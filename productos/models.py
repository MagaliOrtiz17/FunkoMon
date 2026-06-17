from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    RAREZA_CHOICES = [
        ('comun', 'Común ★'),
        ('infrecuente', 'Infrecuente ★★'),
        ('rara', 'Rara ★★★'),
        ('ultra', 'Ultra Rara ★★★★'),
    ]

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos", verbose_name="Categoría")
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Nombre del Funko")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Disponible")
    imagen = models.ImageField(upload_to='funkos/', blank=True, null=True, verbose_name="Imagen del Funko")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    # Campos específicos de Pokémon/TCG
    hp = models.PositiveIntegerField(default=0, verbose_name="HP")
    ataque = models.CharField(max_length=100, blank=True, verbose_name="Nombre del Ataque 1")
    ataque_desc = models.TextField(blank=True, verbose_name="Descripción del Ataque 1")
    ataque_dmg = models.PositiveIntegerField(default=0, verbose_name="Daño Ataque 1")
    ataque2 = models.CharField(max_length=100, blank=True, verbose_name="Nombre del Ataque 2")
    ataque2_dmg = models.PositiveIntegerField(default=0, verbose_name="Daño Ataque 2")
    debilidad = models.CharField(max_length=50, default="-", verbose_name="Debilidad")
    retirada = models.PositiveIntegerField(default=1, verbose_name="Costo de Retirada")
    numero_carta = models.CharField(max_length=20, blank=True, verbose_name="Número de Carta")
    rareza = models.CharField(max_length=20, choices=RAREZA_CHOICES, default='comun', verbose_name="Rareza")
    flavor_text = models.TextField(blank=True, verbose_name="Texto de Sabor")
    imagen_url = models.URLField(max_length=500, blank=True, verbose_name="URL de Imagen (fallback)")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    @property
    def estrellas(self):
        estrellas_map = {'comun': '★', 'infrecuente': '★★', 'rara': '★★★', 'ultra': '★★★★'}
        return estrellas_map.get(self.rareza, '★')

    def get_imagen(self):
        """Retorna emoji del tipo o URL de imagen si existe."""
        ICONOS = {
            "electric": "⚡", "fire": "🔥", "water": "💧", "grass": "🌿",
            "psychic": "🔮", "fighting": "👊", "normal": "⭐", "bug": "🐛",
            "poison": "☠️", "rock": "🪨", "ghost": "👻", "ground": "🏜️",
            "ice": "❄️", "dragon": "🐉",
        }
        tipo_slug = self.categoria.nombre.lower().replace(" ", "")
        return ICONOS.get(tipo_slug, "💧")