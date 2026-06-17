"""
Management command: carga Pokémon con imágenes reales descargadas de URLs públicas.
Las imágenes se guardan en media/funkos/

Ejecutar: python manage.py load_pokemones_with_images
"""

from django.core.management.base import BaseCommand
from productos.models import Categoria, Producto
from decimal import Decimal
import os
from urllib.request import urlretrieve
from django.core.files.base import ContentFile
import io
from PIL import Image as PILImage

# URLs de imágenes reales (públicas y estables)
POKEMONES_CON_IMAGENES = [
    ("Pikachu", "electric", 70, "Gruñido", "Durante turno siguiente hace 20 menos", 20, "Rayo Pika", 30, "fighting", 1, "062/193", "rara", "Cuando se enfada descarga energía.", "https://images.pokemontcg.io/base1/25_hires.png"),
    ("Charizard", "fire", 180, "Garra Dragón", "+30 por energía de Fuego", 80, "Llamarada", 150, "water", 3, "004/165", "ultra", "Escupe fuego que funde rocas.", "https://images.pokemontcg.io/base2/6_hires.png"),
    ("Blastoise", "water", 160, "Aqua Jet", "Chorro a presión", 50, "Hidrobomba", 120, "electric", 3, "009/165", "rara", "Chorros atraviesan acero.", "https://images.pokemontcg.io/base2/9_hires.png"),
    ("Venusaur", "grass", 150, "Absorber", "Recupera 10 HP", 20, "Venenopolvo", 60, "fire", 2, "003/165", "rara", "Absorbe energía del sol.", "https://images.pokemontcg.io/base2/3_hires.png"),
    ("Dragonite", "dragon", 210, "Garra Dragón", "Devastador", 80, "Hiperrayo", 160, "ice", 2, "149/165", "ultra", "Rey de los dragones.", "https://images.pokemontcg.io/base2/149_hires.png"),
    ("Mewtwo", "psychic", 190, "Confusión", "Confunde defensor", 30, "Onda Mental", 140, "psychic", 2, "150/165", "ultra", "Creado por ingeniería genética.", "https://images.pokemontcg.io/base1/10_hires.png"),
    ("Lapras", "water", 210, "Giro Hidro", "Acuático poderoso", 60, "Rayo Gélido", 100, "electric", 3, "131/165", "rara", "Viaja por océano.", "https://images.pokemontcg.io/base1/25_hires.png"),
    ("Gyarados", "water", 230, "Ataque Hidrante", "Agua devastadora", 70, "Rayo Hidrante", 140, "electric", 3, "130/165", "rara", "Destructivo y violento.", "https://images.pokemontcg.io/base1/34_hires.png"),
    ("Alakazam", "psychic", 200, "Confusión", "Psíquico puro", 20, "Onda Mental", 150, "psychic", 1, "065/165", "ultra", "Inteligencia sobrehumana.", "https://images.pokemontcg.io/base1/1_hires.png"),
    ("Machamp", "fighting", 220, "Puño Dinámico", "Cuatro brazos", 100, "Giga Impacto", 160, "psychic", 3, "068/165", "rara", "Cuatro brazos para atacar.", "https://images.pokemontcg.io/base1/33_hires.png"),
    ("Arcanine", "fire", 200, "Fogonada", "Fuego ardiente", 60, "Infierno", 150, "water", 2, "078/165", "rara", "Corre increíblemente rápido.", "https://images.pokemontcg.io/base1/35_hires.png"),
    ("Gengar", "ghost", 130, "Lengüetazo", "Paraliza", 20, "Bola Sombra", 90, "psychic", 0, "094/165", "rara", "Se esconde en sombras.", "https://images.pokemontcg.io/base1/2_hires.png"),
    ("Rhydon", "ground", 220, "Cuerno de Poder", "Coraza resistente", 90, "Terremoto", 140, "water", 3, "112/165", "rara", "Inmune a ataques.", "https://images.pokemontcg.io/base1/39_hires.png"),
    ("Marowak", "ground", 160, "Ataque Osudo", "Cola arma", 50, "Bola de Roca", 110, "water", 2, "105/165", "rara", "Llora bajo máscara.", "https://images.pokemontcg.io/base1/25_hires.png"),
    ("Kingler", "water", 190, "Corte de Pinza", "Pinzas afiladas", 70, "Pulverizador", 120, "grass", 2, "099/165", "rara", "Pinzas aplastantes.", "https://images.pokemontcg.io/base1/29_hires.png"),
    ("Hypno", "psychic", 170, "Péndulo Hipnótico", "Hipnotiza", 50, "Rayo Psíquico", 110, "psychic", 1, "097/165", "rara", "Controla mente.", "https://images.pokemontcg.io/base1/9_hires.png"),
    ("Victreebel", "grass", 160, "Trampa de Vina", "Atrapa presas", 60, "Solarbeam", 120, "fire", 2, "071/165", "rara", "Trampa mortal.", "https://images.pokemontcg.io/base1/17_hires.png"),
    ("Starmie", "water", 170, "Rayo de Joya", "Brillo acuático", 50, "Hidrobomba", 130, "grass", 1, "121/165", "rara", "Joya viviente.", "https://images.pokemontcg.io/base1/32_hires.png"),
    ("Slowbro", "water", 180, "Cuerpo Pegajoso", "Shellder pegado", 60, "Rayo Psíquico", 120, "grass", 2, "080/165", "rara", "Shellder adherida.", "https://images.pokemontcg.io/base1/7_hires.png"),
    ("Jynx", "psychic", 150, "Beso Helado", "Beso dañino", 40, "Rayo Psíquico", 120, "psychic", 1, "124/165", "rara", "Movimientos hipnóticos.", "https://images.pokemontcg.io/base1/31_hires.png"),
]

TIPOS = {
    "grass": "Planta",
    "fire": "Fuego",
    "water": "Agua",
    "bug": "Bicho",
    "normal": "Normal",
    "poison": "Veneno",
    "electric": "Eléctrico",
    "ground": "Tierra",
    "ghost": "Fantasma",
    "rock": "Roca",
    "psychic": "Psíquico",
    "fighting": "Lucha",
    "ice": "Hielo",
    "dragon": "Dragón",
}


class Command(BaseCommand):
    help = "Carga Pokémon descargando imágenes reales desde URLs públicas"

    def descargar_imagen(self, url, nombre_archivo):
        """Descarga imagen y la convierte a JPG."""
        try:
            os.makedirs("media/funkos/", exist_ok=True)

            # Descargar
            print(f"  Descargando {nombre_archivo}...", end=" ", flush=True)
            urlretrieve(url, f"temp_{nombre_archivo}.png")

            # Convertir a JPG
            img = PILImage.open(f"temp_{nombre_archivo}.png").convert("RGB")
            jpg_path = f"media/funkos/{nombre_archivo}.jpg"
            img.save(jpg_path, "JPEG", quality=90)

            # Limpiar temp
            if os.path.exists(f"temp_{nombre_archivo}.png"):
                os.remove(f"temp_{nombre_archivo}.png")

            print("[OK]")
            return f"funkos/{nombre_archivo}.jpg"
        except Exception as e:
            print(f"[ERROR] {e}")
            return None

    def handle(self, *args, **options):
        # Crear categorías
        categorias = {}
        for tipo_slug, tipo_nombre in TIPOS.items():
            cat, _ = Categoria.objects.get_or_create(
                nombre=tipo_nombre,
                defaults={"descripcion": f"Pokémon de tipo {tipo_nombre}"}
            )
            categorias[tipo_slug] = cat

        self.stdout.write("Descargando imágenes y cargando Pokémon...\n")

        # Cargar Pokémon
        contador = 0
        for nombre, tipo_slug, hp, ataque, ataque_desc, ataque_dmg, ataque2, ataque2_dmg, debilidad, retirada, numero, rareza, flavor, img_url in POKEMONES_CON_IMAGENES:
            # Descargar imagen
            nombre_sanitizado = nombre.lower().replace(" ", "_")
            imagen_path = self.descargar_imagen(img_url, nombre_sanitizado)

            obj, created = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "categoria": categorias[tipo_slug],
                    "descripcion": flavor,
                    "precio": Decimal(str(25.99 + (hash(nombre) % 50))),
                    "stock": 15,
                    "hp": hp,
                    "ataque": ataque,
                    "ataque_desc": ataque_desc,
                    "ataque_dmg": ataque_dmg,
                    "ataque2": ataque2,
                    "ataque2_dmg": ataque2_dmg,
                    "debilidad": debilidad,
                    "retirada": retirada,
                    "numero_carta": numero,
                    "rareza": rareza,
                    "flavor_text": flavor,
                }
            )

            # Guardar imagen si existe
            if imagen_path and created:
                try:
                    obj.imagen = imagen_path
                    obj.save()
                except:
                    pass

            if created:
                contador += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\n[OK] {contador} Pokémon con imágenes cargados exitosamente.\n"
                f"Total en BD: {Producto.objects.count()}\n"
                f"Imágenes guardadas en: media/funkos/"
            )
        )
