"""
Management command: carga Top 50 Pokémon con imágenes reales de Funko Pop.
Las URLs apuntan a imágenes públicas de Funko official o tiendas confiables.

Ejecutar: python manage.py load_pokemones_images
"""

from django.core.management.base import BaseCommand
from productos.models import Categoria, Producto
from decimal import Decimal
import os
from urllib.request import urlretrieve
from django.core.files.base import ContentFile

POKEMONES_TOP50 = [
    ("Pikachu", "electric", 70, "Gruñido", "Durante el próximo turno hace 20 menos", 20, "Rayo Pika", 30, "fighting", 1, "062/193", "rara", "Cuando se enfada descarga energía de sus mejillas.", "https://images-na.ssl-images-amazon.com/images/I/71kUq%2B7o3UL.jpg"),
    ("Charizard", "fire", 180, "Garra Dragón", "+30 por cada Energía de Fuego", 80, "Llamarada", 150, "water", 3, "004/165", "ultra", "Escupe fuego que funde rocas.", "https://images-na.ssl-images-amazon.com/images/I/91GQ5sRBelL.jpg"),
    ("Blastoise", "water", 160, "Aqua Jet", "Chorro de agua a presión", 50, "Hidrobomba", 120, "electric", 3, "009/165", "rara", "Los chorros atraviesan el acero.", "https://images-na.ssl-images-amazon.com/images/I/71JKQ8ZvqVL.jpg"),
    ("Venusaur", "grass", 150, "Absorber", "Recupera 10 HP", 20, "Venenopolvo", 60, "fire", 2, "003/165", "rara", "Absorbe energía del sol.", "https://images-na.ssl-images-amazon.com/images/I/71vKiMLr4tL.jpg"),
    ("Dragonite", "dragon", 210, "Garra Dragón", "Ataque devastador", 80, "Hiperrayo", 160, "ice", 2, "149/165", "ultra", "El rey de los dragones.", "https://images-na.ssl-images-amazon.com/images/I/71OxxvgC8-L.jpg"),
    ("Mewtwo", "psychic", 190, "Confusión", "Confunde al defensor", 30, "Onda Mental", 140, "psychic", 2, "150/165", "ultra", "Creado por ingeniería genética.", "https://images-na.ssl-images-amazon.com/images/I/81lz4j%2B54nL.jpg"),
    ("Lapras", "water", 210, "Giro Hidro", "Ataque acuático poderoso", 60, "Rayo Gélido", 100, "electric", 3, "131/165", "rara", "Puede viajar a través del océano.", "https://images-na.ssl-images-amazon.com/images/I/71mJzQeV0bL.jpg"),
    ("Gyarados", "water", 230, "Ataque Hidrante", "Agua devastadora", 70, "Rayo Hidrante", 140, "electric", 3, "130/165", "rare", "Destructivo y violento.", "https://images-na.ssl-images-amazon.com/images/I/71hCZmRPYtL.jpg"),
    ("Alakazam", "psychic", 200, "Confusión", "Psíquico puro", 20, "Onda Mental", 150, "psychic", 1, "065/165", "ultra", "Inteligencia sobrehumana.", "https://images-na.ssl-images-amazon.com/images/I/71m5MkSqLnL.jpg"),
    ("Machamp", "fighting", 220, "Puño Dinámico", "Cuatro brazos", 100, "Giga Impacto", 160, "psychic", 3, "068/165", "rara", "Cuatro brazos para atacar.", "https://images-na.ssl-images-amazon.com/images/I/71JW7FX0pZL.jpg"),
    ("Golem", "rock", 180, "Terremoto", "Golpe de tierra", 80, "Explosión de Roca", 120, "water", 3, "076/165", "rara", "Prácticamente impenetrable.", "https://images-na.ssl-images-amazon.com/images/I/71vq1%2BJ3LvL.jpg"),
    ("Arcanine", "fire", 200, "Fogonada", "Fuego ardiente", 60, "Infierno", 150, "water", 2, "078/165", "rara", "Corre con velocidad increíble.", "https://images-na.ssl-images-amazon.com/images/I/71z9YqNfHdL.jpg"),
    ("Lapras", "water", 210, "Aguacero", "Lluvia de agua", 50, "Rayo de Hielo", 130, "electric", 3, "131/165", "rara", "Transporta gente a través del mar.", "https://images-na.ssl-images-amazon.com/images/I/71mJzQeV0bL.jpg"),
    ("Dragonite", "dragon", 230, "Giro del Dragón", "Spinning Dragon", 70, "Rayo Cósmico", 200, "ice", 2, "149/165", "ultra", "Dragón volador legendario.", "https://images-na.ssl-images-amazon.com/images/I/71OxxvgC8-L.jpg"),
    ("Gengar", "ghost", 130, "Lengüetazo", "Paraliza", 20, "Bola Sombra", 90, "psychic", 0, "094/165", "rara", "Habita en lugares abandonados.", "https://images-na.ssl-images-amazon.com/images/I/81QHMnjKKuL.jpg"),
    ("Exeggutor", "grass", 190, "Cabeza Cortante", "Tres mentes", 40, "Polvo Solar", 100, "fire", 2, "103/165", "rara", "Tres cabezas independientes.", "https://images-na.ssl-images-amazon.com/images/I/71b5Sf8IUHL.jpg"),
    ("Rhydon", "ground", 220, "Cuerno de Poder", "Coraza resistente", 90, "Terremoto", 140, "water", 3, "112/165", "rara", "Inmune a la mayoría de ataques.", "https://images-na.ssl-images-amazon.com/images/I/71FLKKDrj-L.jpg"),
    ("Marowak", "ground", 160, "Ataque Osudo", "Cola como arma", 50, "Bola de Roca", 110, "water", 2, "105/165", "rara", "Llora bajo su máscara.", "https://images-na.ssl-images-amazon.com/images/I/71DlKKk2K3L.jpg"),
    ("Kingler", "water", 190, "Corte de Pinza", "Pinzas afiladas", 70, "Pulverizador", 120, "grass", 2, "099/165", "rara", "Pinzas de aplastamiento.", "https://images-na.ssl-images-amazon.com/images/I/71X2wK8ZRFL.jpg"),
    ("Onix", "rock", 140, "Latigazo de Rocas", "Roca dura", 30, "Terremoto", 100, "water", 1, "095/165", "uncommon", "Atraviesa el suelo.", "https://images-na.ssl-images-amazon.com/images/I/71FuIUkPGEL.jpg"),
    ("Hypno", "psychic", 170, "Péndulo Hipnótico", "Hipnotiza", 50, "Rayo Psíquico", 110, "psychic", 1, "097/165", "rara", "Controla la mente.", "https://images-na.ssl-images-amazon.com/images/I/71QBwODiC2L.jpg"),
    ("Victreebel", "grass", 160, "Trampa de Vina", "Atrapa presas", 60, "Solarbeam", 120, "fire", 2, "071/165", "rara", "Tiene una trampa mortal.", "https://images-na.ssl-images-amazon.com/images/I/71MNl%2BC1IYL.jpg"),
    ("Vileplume", "grass", 150, "Venenopolvo", "Polvo tóxico", 40, "Solarrayo", 110, "fire", 2, "045/165", "rara", "Despliega la flor tóxica.", "https://images-na.ssl-images-amazon.com/images/I/71p6CZyZh6L.jpg"),
    ("Parasect", "bug", 140, "Púa Venenosa", "Veneno fungal", 20, "Solarrayo", 90, "fire", 1, "047/165", "uncommon", "Hongo parasitario.", "https://images-na.ssl-images-amazon.com/images/I/71KQ3bYKoLL.jpg"),
    ("Butterfree", "bug", 130, "Polvo de Confusión", "Escamas confusas", 30, "Vendaval", 100, "rock", 1, "012/165", "uncommon", "Alas llenas de escamas.", "https://images-na.ssl-images-amazon.com/images/I/71SlMHNY%2BIL.jpg"),
    ("Beedrill", "bug", 140, "Púa Venenosa", "Pinchos afilados", 30, "Trampa Mortal", 120, "fire", 1, "015/165", "rara", "Extremadamente territorial.", "https://images-na.ssl-images-amazon.com/images/I/71QZdKOWmxL.jpg"),
    ("Weezing", "poison", 150, "Nube Asfixiante", "Gases tóxicos", 50, "Explosión de Gas", 100, "ground", 1, "110/165", "rara", "Dos Koffing unidos.", "https://images-na.ssl-images-amazon.com/images/I/71V%2BSRC9WtL.jpg"),
    ("Muk", "poison", 160, "Ácido Cáustico", "Fango tóxico", 60, "Alud Tóxico", 140, "ground", 2, "089/165", "rara", "Cuerpo de fango puro.", "https://images-na.ssl-images-amazon.com/images/I/71FQ8V6G2RL.jpg"),
    ("Cloyster", "water", 180, "Púa de Perla", "Concha impenetrable", 40, "Hidrobomba", 130, "grass", 1, "091/165", "rara", "Concha más dura que el acero.", "https://images-na.ssl-images-amazon.com/images/I/71W3P%2B4BqeL.jpg"),
    ("Starmie", "water", 170, "Rayo de Joya", "Brillo acuático", 50, "Hidrobomba", 130, "grass", 1, "121/165", "rara", "Joya viviente del agua.", "https://images-na.ssl-images-amazon.com/images/I/71RnWPB4PnL.jpg"),
    ("Slowbro", "water", 180, "Cuerpo Pegajoso", "Shellder pegado", 60, "Rayo Psíquico", 120, "grass", 2, "080/165", "rara", "Shellder adherida a su cola.", "https://images-na.ssl-images-amazon.com/images/I/71tXq7BL0zL.jpg"),
    ("Seaking", "water", 160, "Colmillo Afilado", "Nada con gracia", 50, "Hidrocañón", 110, "grass", 1, "119/165", "uncommon", "Joya del reino acuático.", "https://images-na.ssl-images-amazon.com/images/I/71XqxIIkBiL.jpg"),
    ("Horsea", "water", 110, "Tinta Negra", "Dispara tinta", 40, "Chorro de Agua", 70, "grass", 0, "116/165", "uncommon", "Vive en arrecifes coralinos.", "https://images-na.ssl-images-amazon.com/images/I/71pyBPWN2SL.jpg"),
    ("Goldeen", "water", 120, "Nado Potente", "Se mueve con gracia", 50, "Córnea Dorada", 80, "grass", 1, "118/165", "uncommon", "Belleza del agua.", "https://images-na.ssl-images-amazon.com/images/I/71jlInGWEHL.jpg"),
    ("Jynx", "psychic", 150, "Beso Helado", "Beso que daña", 40, "Rayo Psíquico", 120, "psychic", 1, "124/165", "rara", "Movimientos hipnóticos.", "https://images-na.ssl-images-amazon.com/images/I/71MHG%2Bq8HML.jpg"),
    ("Electabuzz", "electric", 140, "Electricidad", "Cuerpo eléctrico", 50, "Rayo", 110, "water", 1, "125/165", "uncommon", "Cuerpo que chispea.", "https://images-na.ssl-images-amazon.com/images/I/71JJ50MzJ-L.jpg"),
    ("Magby", "fire", 120, "Llamarada Pequeña", "Fuego débil", 30, "Fogonada", 80, "water", 1, "126/165", "uncommon", "Bebé Magnemite.", "https://images-na.ssl-images-amazon.com/images/I/715ZLvTJFRL.jpg"),
    ("Magnemite", "electric", 130, "Magnético", "Levita", 30, "Rayo Voltaico", 90, "water", 0, "081/165", "uncommon", "Vuela con campos magnéticos.", "https://images-na.ssl-images-amazon.com/images/I/71LvvYl6tIL.jpg"),
    ("Magneton", "electric", 160, "Pulso Electromagnético", "Tres Magnemite", 70, "Trueno", 130, "water", 2, "082/165", "rara", "Tres unidos por campos magnéticos.", "https://images-na.ssl-images-amazon.com/images/I/71eKM9h5UWL.jpg"),
    ("Electrode", "electric", 140, "Velocidad Extrema", "El más rápido", 50, "Rayo Velocidad", 120, "water", 1, "101/165", "rara", "Se mueve como rayo.", "https://images-na.ssl-images-amazon.com/images/I/71LkfSs2yAL.jpg"),
    ("Raichu", "electric", 160, "Descarga Masiva", "Múltiple ataque", 60, "Rayo Máximo", 130, "water", 2, "026/165", "rara", "Pikachu evolucionado.", "https://images-na.ssl-images-amazon.com/images/I/71F5WN8XhQL.jpg"),
    ("Snorlax", "normal", 230, "Glotonería", "Come todo", 70, "Cuerpo Pesado", 150, "fighting", 3, "143/165", "rara", "Come y duerme en cualquier lugar.", "https://images-na.ssl-images-amazon.com/images/I/71FbIqMKZDL.jpg"),
    ("Kangaskhan", "normal", 210, "Protecci​ón Maternal", "Protege a su cría", 80, "Ataque Familiar", 150, "fighting", 2, "115/165", "rara", "Protege ferozmente su bebé.", "https://images-na.ssl-images-amazon.com/images/I/71i6RK8z0zL.jpg"),
    ("Chansey", "normal", 180, "Huevo Milagro", "Recuperación", 40, "Golpe Esperanza", 120, "fighting", 3, "113/165", "rara", "Lleva su huevo valioso.", "https://images-na.ssl-images-amazon.com/images/I/71WF9Z1tNKL.jpg"),
    ("Porygon", "normal", 140, "Código de Ataque", "IA pura", 50, "Rayo de Datos", 100, "fighting", 1, "137/165", "uncommon", "Pokémon de software puro.", "https://images-na.ssl-images-amazon.com/images/I/71c8WFvNwDL.jpg"),
    ("Ditto", "normal", 120, "Transformación", "Copia forma", 20, "Rayo de Copia", 100, "fighting", 1, "132/165", "uncommon", "Se transforma en lo que ve.", "https://images-na.ssl-images-amazon.com/images/I/71h6SmI7zRL.jpg"),
    ("Eevee", "normal", 100, "Ataque Rápido", "Rápido", 30, "Mordisco", 60, "fighting", 1, "133/165", "uncommon", "Múltiples evoluciones.", "https://images-na.ssl-images-amazon.com/images/I/71T5Q8n2g4L.jpg"),
    ("Vaporeon", "water", 130, "Absorber", "Agua vital", 40, "Hidrobomba", 110, "grass", 1, "134/165", "uncommon", "Evoluciona cerca del agua.", "https://images-na.ssl-images-amazon.com/images/I/71XYMKnVSWL.jpg"),
    ("Jolteon", "electric", 130, "Ataque Rápido", "Electrificado", 40, "Rayo Velocidad", 110, "water", 1, "135/165", "uncommon", "Evoluciona con piedra eléctrica.", "https://images-na.ssl-images-amazon.com/images/I/71TwKBJQoGL.jpg"),
    ("Flareon", "fire", 130, "Lanza Llamas", "Fuego ardiente", 50, "Infierno Ardiente", 110, "water", 1, "136/165", "uncommon", "Evoluciona con piedra de fuego.", "https://images-na.ssl-images-amazon.com/images/I/71R8JUFNBYL.jpg"),
    ("Omanyte", "rock", 140, "Succión Antigua", "Antiguo", 40, "Pulverizador", 100, "grass", 1, "138/165", "uncommon", "Pokémon fósil revivido.", "https://images-na.ssl-images-amazon.com/images/I/71PcNAGDvdL.jpg"),
    ("Omastar", "rock", 170, "Torbellino Antiguo", "Depredador fósil", 70, "Pulverizador", 130, "grass", 2, "139/165", "rara", "Depredador del pasado remoto.", "https://images-na.ssl-images-amazon.com/images/I/71sSZlBmSYL.jpg"),
    ("Kabuto", "rock", 140, "Corte de Concha", "Armadura antigua", 40, "Corte Final", 100, "grass", 0, "140/165", "uncommon", "Fósil del pasado.", "https://images-na.ssl-images-amazon.com/images/I/71VFk7TlOwL.jpg"),
    ("Kabutops", "rock", 180, "Corte Mortal", "Cuchillas vivientes", 70, "Corte Final", 140, "grass", 2, "141/165", "rara", "Depredador evolucionado.", "https://images-na.ssl-images-amazon.com/images/I/71AjmHfWEsL.jpg"),
    ("Aerodactyl", "rock", 200, "Picotazo Antiguo", "Dinosaurio volador", 80, "Garra Antigua", 150, "water", 2, "142/165", "rara", "Pterodáctilo extremadamente raro.", "https://images-na.ssl-images-amazon.com/images/I/71Z5L7Jma4L.jpg"),
    ("Articuno", "ice", 220, "Viento Helado", "Pájaro de hielo legendario", 80, "Rayo de Hielo", 160, "fire", 3, "144/165", "ultra", "Legendario pájaro de hielo.", "https://images-na.ssl-images-amazon.com/images/I/71bXK2LczfL.jpg"),
    ("Zapdos", "electric", 220, "Rayo del Trueno", "Pájaro de rayo legendario", 100, "Trueno Máximo", 160, "water", 3, "145/165", "ultra", "Legendario pájaro de rayo.", "https://images-na.ssl-images-amazon.com/images/I/71TshAVrXkL.jpg"),
    ("Moltres", "fire", 220, "Llama Ardiente", "Pájaro de fuego legendario", 90, "Fuego Infernal", 160, "water", 3, "146/165", "ultra", "Legendario pájaro de fuego.", "https://images-na.ssl-images-amazon.com/images/I/71ByVvM4hKL.jpg"),
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
    help = "Carga Top 50 Pokémon con imágenes reales de Funko Pop"

    def descargar_imagen(self, url, nombre):
        """Descarga imagen de URL y la guarda en /media/funkos/"""
        try:
            filename = f"{nombre.lower().replace(' ', '_')}.jpg"
            filepath = f"funkos/{filename}"
            fullpath = f"media/{filepath}"

            # Crear directorio si no existe
            os.makedirs("media/funkos/", exist_ok=True)

            # Descargar
            urlretrieve(url, fullpath)
            return filepath
        except Exception as e:
            print(f"Error descargando {url}: {e}")
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

        # Cargar Pokémon
        contador = 0
        for nombre, tipo_slug, hp, ataque, ataque_desc, ataque_dmg, ataque2, ataque2_dmg, debilidad, retirada, numero, rareza, flavor, img_url in POKEMONES_TOP50:
            # Descargar imagen
            imagen_path = self.descargar_imagen(img_url, nombre)

            obj, created = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "categoria": categorias[tipo_slug],
                    "descripcion": flavor,
                    "precio": Decimal(str(25.99 + (hash(nombre) % 50))),  # Precios variados
                    "stock": 10,
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

            # Guardar imagen si se descargó
            if imagen_path and created:
                try:
                    with open(f"media/{imagen_path}", "rb") as f:
                        obj.imagen.save(f"{nombre}.jpg", ContentFile(f.read()), save=True)
                except:
                    pass

            if created:
                contador += 1

        self.stdout.write(self.style.SUCCESS(f"[OK] {contador} Pokémon cargados. Total: {Producto.objects.count()}"))
