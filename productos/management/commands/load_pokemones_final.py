"""
Management command: carga 20 Pokémon Top con URLs de imágenes públicas.
Las imágenes se cargan directamente desde URLs en los templates.

Ejecutar: python manage.py load_pokemones_final
"""

from django.core.management.base import BaseCommand
from productos.models import Categoria, Producto
from decimal import Decimal

# Pokémon populares con URLs de imágenes públicas que funcionan
POKEMONES = [
    ("Pikachu", "electric", 70, "Gruñido", "Durante turno siguiente hace 20 menos", 20, "Rayo Pika", 30, "fighting", 1, "062/193", "rara", "Cuando se enfada descarga energía.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"),
    ("Charizard", "fire", 180, "Garra Dragón", "+30 por energía de Fuego", 80, "Llamarada", 150, "water", 3, "004/165", "ultra", "Escupe fuego que funde rocas.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"),
    ("Blastoise", "water", 160, "Aqua Jet", "Chorro a presión", 50, "Hidrobomba", 120, "electric", 3, "009/165", "rara", "Chorros atraviesan acero.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png"),
    ("Venusaur", "grass", 150, "Absorber", "Recupera 10 HP", 20, "Venenopolvo", 60, "fire", 2, "003/165", "rara", "Absorbe energía del sol.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png"),
    ("Dragonite", "dragon", 210, "Garra Dragón", "Devastador", 80, "Hiperrayo", 160, "ice", 2, "149/165", "ultra", "Rey de los dragones.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png"),
    ("Mewtwo", "psychic", 190, "Confusión", "Confunde defensor", 30, "Onda Mental", 140, "psychic", 2, "150/165", "ultra", "Creado por ingeniería genética.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"),
    ("Lapras", "water", 210, "Giro Hidro", "Acuático poderoso", 60, "Rayo Gélido", 100, "electric", 3, "131/165", "rara", "Viaja por océano.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/131.png"),
    ("Gyarados", "water", 230, "Ataque Hidrante", "Agua devastadora", 70, "Rayo Hidrante", 140, "electric", 3, "130/165", "rara", "Destructivo y violento.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png"),
    ("Alakazam", "psychic", 200, "Confusión", "Psíquico puro", 20, "Onda Mental", 150, "psychic", 1, "065/165", "ultra", "Inteligencia sobrehumana.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png"),
    ("Machamp", "fighting", 220, "Puño Dinámico", "Cuatro brazos", 100, "Giga Impacto", 160, "psychic", 3, "068/165", "rara", "Cuatro brazos para atacar.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png"),
    ("Arcanine", "fire", 200, "Fogonada", "Fuego ardiente", 60, "Infierno", 150, "water", 2, "078/165", "rara", "Corre increíblemente rápido.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/78.png"),
    ("Gengar", "ghost", 130, "Lengüetazo", "Paraliza", 20, "Bola Sombra", 90, "psychic", 0, "094/165", "rara", "Se esconde en sombras.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"),
    ("Rhydon", "ground", 220, "Cuerno de Poder", "Coraza resistente", 90, "Terremoto", 140, "water", 3, "112/165", "rara", "Inmune a ataques.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/112.png"),
    ("Marowak", "ground", 160, "Ataque Osudo", "Cola arma", 50, "Bola de Roca", 110, "water", 2, "105/165", "rara", "Llora bajo máscara.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/105.png"),
    ("Kingler", "water", 190, "Corte de Pinza", "Pinzas afiladas", 70, "Pulverizador", 120, "grass", 2, "099/165", "rara", "Pinzas aplastantes.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/99.png"),
    ("Hypno", "psychic", 170, "Péndulo Hipnótico", "Hipnotiza", 50, "Rayo Psíquico", 110, "psychic", 1, "097/165", "rara", "Controla mente.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/97.png"),
    ("Victreebel", "grass", 160, "Trampa de Vina", "Atrapa presas", 60, "Solarbeam", 120, "fire", 2, "071/165", "rara", "Trampa mortal.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/71.png"),
    ("Starmie", "water", 170, "Rayo de Joya", "Brillo acuático", 50, "Hidrobomba", 130, "grass", 1, "121/165", "rara", "Joya viviente.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/121.png"),
    ("Slowbro", "water", 180, "Cuerpo Pegajoso", "Shellder pegado", 60, "Rayo Psíquico", 120, "grass", 2, "080/165", "rara", "Shellder adherida.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/80.png"),
    ("Jynx", "psychic", 150, "Beso Helado", "Beso dañino", 40, "Rayo Psíquico", 120, "psychic", 1, "124/165", "rara", "Movimientos hipnóticos.", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/124.png"),
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
    help = "Carga Top 20 Pokémon con URLs de imágenes públicas de PokeAPI"

    def handle(self, *args, **options):
        # Crear categorías
        categorias = {}
        for tipo_slug, tipo_nombre in TIPOS.items():
            cat, _ = Categoria.objects.get_or_create(
                nombre=tipo_nombre,
                defaults={"descripcion": f"Pokémon de tipo {tipo_nombre}"}
            )
            categorias[tipo_slug] = cat

        self.stdout.write("Cargando Top 20 Pokémon con imágenes...\n")

        # Cargar Pokémon
        contador = 0
        for nombre, tipo_slug, hp, ataque, ataque_desc, ataque_dmg, ataque2, ataque2_dmg, debilidad, retirada, numero, rareza, flavor, img_url in POKEMONES:
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
                    "imagen_url": img_url,  # URL pública
                }
            )

            if created:
                contador += 1
                print(f"  [OK] {nombre}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\n[SUCCESS] {contador} Pokémon cargados.\n"
                f"Total en BD: {Producto.objects.count()}\n"
                f"Las imágenes se cargan desde URLs públicas de PokeAPI."
            )
        )
