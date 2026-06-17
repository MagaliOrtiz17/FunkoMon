"""
Management command: carga los 150 Pokémon originales con tipos, precios y descripciones.
Ejecutar: python manage.py load_pokemones
"""

from django.core.management.base import BaseCommand
from productos.models import Categoria, Producto
from decimal import Decimal

POKEMONES = [
    ("Bulbasaur", "grass", 19.99, "Una rara semilla fue plantada en su espalda al nacer."),
    ("Ivysaur", "grass", 24.99, "Cuando se expone a la luz solar, crece y evoluciona."),
    ("Venusaur", "grass", 49.99, "Puede absorber energía del sol para recargar su cuerpo."),
    ("Charmander", "fire", 21.99, "Prefiere lugares calurosos. Se dice que nació en la boca de un volcán."),
    ("Charmeleon", "fire", 27.99, "Es más activo en la noche. Su cola brilla cuando acumula poder."),
    ("Charizard", "fire", 89.99, "Su fuego es lo suficientemente caliente como para derretir cualquier cosa."),
    ("Squirtle", "water", 19.99, "Se retrae dentro de su caparazón para defenderse del frío."),
    ("Wartortle", "water", 26.99, "Posee un caparazón grueso que lo protege en batalla."),
    ("Blastoise", "water", 54.99, "Puede apuntar con precisión a objetivos a 160 pies de distancia."),
    ("Caterpie", "bug", 14.99, "Su cuerpo está cubierto por una capa antitóxica de mucosidad."),
    ("Metapod", "bug", 17.99, "Permanece dentro de su caparazón para protegerse."),
    ("Butterfree", "bug", 34.99, "Sus alas están llenas de escamas de polvo que puede usar en batalla."),
    ("Weedle", "bug", 14.99, "Tiene una vida nocturna, escondiéndose durante el día."),
    ("Kakuna", "bug", 16.99, "Casi no se mueve. Está en proceso de evolucionar."),
    ("Beedrill", "bug", 39.99, "Es extremadamente territorial y atacará a cualquier cosa que se acerque."),
    ("Pidgeot", "normal", 44.99, "Vuela a una velocidad máxima de 2.24 millas por hora."),
    ("Pidgeotto", "normal", 29.99, "Es muy territorial y atacará a otros Pokémon que invadan su espacio."),
    ("Pidgeyn", "normal", 16.99, "Es muy común verlo en campos y bosques."),
    ("Rattata", "normal", 12.99, "Sus dientes nunca dejan de crecer y los afila royendo cosas."),
    ("Raticate", "normal", 22.99, "Es muy hábil trepando por superficies ásperas."),
    ("Spearow", "normal", 17.99, "Su picotazo es muy peligroso. Ataca con el pico y las garras."),
    ("Fearow", "normal", 37.99, "Vuela a una velocidad muy alta, manteniendo un curso estable."),
    ("Ekans", "poison", 18.99, "Vive escondiéndose entre la maleza y los árboles."),
    ("Arbok", "poison", 38.99, "Su patrón puede variar. Vive en áreas tropical."),
    ("Pichu", "electric", 16.99, "Produce electricidad cuando está asustado o excitado."),
    ("Pikachu", "electric", 24.99, "Cuando tiene miedo, almacena electricidad en sus mejillas."),
    ("Raichu", "electric", 44.99, "Produce un rayo capaz de destruir una montaña."),
    ("Magnemite", "electric", 21.99, "Vuela utilizando campos magnéticos generados por su cuerpo."),
    ("Magneton", "electric", 39.99, "Tres Magnemite conectados entre sí por campos magnéticos."),
    ("Voltorb", "electric", 19.99, "Parece ser un Poké Ball, pero en realidad es un Pokémon."),
    ("Electrode", "electric", 36.99, "Se mueve tan rápido que parece que desaparece del lugar."),
    ("Diglett", "ground", 14.99, "Vive bajo tierra. Solo se ve su cabeza."),
    ("Dugtrio", "ground", 28.99, "Tres Diglett unidos bajo tierra. Pueden cavar muy rápido."),
    ("Cubone", "ground", 22.99, "Siempre lleva el cráneo de su madre como casco."),
    ("Marowak", "ground", 37.99, "Usa su cola para cavar y golpear en batalla."),
    ("Rhyhorn", "ground", 34.99, "Tiene una coraza muy dura que puede soportar explosiones."),
    ("Rhydon", "ground", 54.99, "Es prácticamente inmune al daño de la mayoría de ataques."),
    ("Sandshrew", "ground", 19.99, "Se entierra para escapar de enemigos o cuando hace frío."),
    ("Sandslash", "ground", 36.99, "Sus garras pueden cortar a través de casi cualquier cosa."),
    ("Cloyster", "water", 42.99, "Su concha es más dura que el acero."),
    ("Shellder", "water", 24.99, "Tapa su cuerpo con una concha para protegerse."),
    ("Gastly", "ghost", 26.99, "Se dice que habita en hogares abandonados."),
    ("Haunter", "ghost", 35.99, "Baja la temperatura alrededor de los 10 grados Celsius."),
    ("Gengar", "ghost", 44.99, "Se esconde en las sombras y aparece de repente."),
    ("Onix", "rock", 32.99, "Está compuesto por rocas. Puede atravesar el suelo."),
    ("Drowzee", "psychic", 28.99, "Se dice que se alimenta de los sueños de los humanos."),
    ("Hypno", "psychic", 42.99, "Puede hipnotizar a sus enemigos con su péndulo."),
    ("Krabby", "water", 21.99, "Sus pinzas son sus armas principales."),
    ("Kingler", "water", 38.99, "Las pinzas de un Kingler pueden aplastar cualquier cosa."),
    ("Horsea", "water", 22.99, "Vive en los arrecifes de coral. Dispara tinta como defensa."),
    ("Seadra", "water", 41.99, "Sus aletas son tan agudas que puede cortarlo todo."),
    ("Goldeen", "water", 24.99, "Se mueve por el agua con gracia incomparable."),
    ("Seaking", "water", 39.99, "Defiende ferozmente su territorio durante el desove."),
    ("Staryu", "water", 26.99, "Tiene una joya en su centro que brilla con el movimiento."),
    ("Starmie", "water", 45.99, "Puede regenerar sus extremidades si se pierden."),
    ("Mr. Mime", "psychic", 34.99, "Crea una barrera invisible utilizando su poder psíquico."),
    ("Jynx", "psychic", 41.99, "Sus movimientos hipnóticos pueden noquear a cualquiera."),
    ("Smoochum", "psychic", 32.99, "Besa a sus enemigos para hacerlos entrar en pánico."),
    ("Abra", "psychic", 24.99, "Desaparece usando teleportación cuando se asusta."),
    ("Kadabra", "psychic", 34.99, "Su poder psíquico es lo suficientemente fuerte para doblar cucharas."),
    ("Alakazam", "psychic", 54.99, "Su inteligencia es comparable a una supercomputadora."),
    ("Machop", "fighting", 22.99, "Entrena constantemente para desarrollar su musculatura."),
    ("Machoke", "fighting", 32.99, "Puede mover montañas usando su increíble fuerza."),
    ("Machamp", "fighting", 49.99, "Sus cuatro brazos le permiten realizar múltiples ataques."),
    ("Bellsprout", "grass", 18.99, "Ataca enrollándose alrededor de sus enemigos."),
    ("Weepinbell", "grass", 27.99, "Puede digerir casi cualquier cosa con sus ácidos."),
    ("Victreebel", "grass", 44.99, "Tiene una trampa en su boca para atrapar presas."),
    ("Tentacool", "water", 19.99, "Nada en el océano usando sus tentáculos."),
    ("Tentacruel", "water", 38.99, "Sus tentáculos pueden extenderse muy lejos."),
    ("Slowpoke", "water", 23.99, "Piensa muy lentamente en todo lo que hace."),
    ("Slowbro", "water", 36.99, "Un Shellder se adhirió a su cola."),
    ("Seel", "water", 24.99, "Vive en agua fría y se desliza sobre el hielo."),
    ("Dewgong", "water", 42.99, "Nada gracefully through the ocean."),
    ("Grimer", "poison", 21.99, "Está hecho completamente de fango tóxico."),
    ("Muk", "poison", 35.99, "Su cuerpo emite un olor tremendamente fétido."),
    ("Shellder", "water", 24.99, "Cierra su concha cuando se siente amenazado."),
    ("Cloyster", "water", 42.99, "Su concha es prácticamente impenetrable."),
    ("Gastly", "ghost", 26.99, "Se forma a partir de vapores venenosos."),
    ("Haunter", "ghost", 35.99, "Puede atravesar cualquier pared."),
    ("Gengar", "ghost", 44.99, "Desciende la temperatura cuando aparece."),
    ("Onix", "rock", 32.99, "Puede atravesar el terreno como un topo."),
    ("Drowzee", "psychic", 28.99, "Devora los sueños de sus víctimas."),
    ("Hypno", "psychic", 42.99, "Puede controlar la mente con su péndulo."),
    ("Krabby", "water", 21.99, "Sus pinzas son sus mejores armas."),
    ("Kingler", "water", 38.99, "Tiene un caparazón muy resistente."),
    ("Voltorb", "electric", 19.99, "Explota cuando se siente amenazado."),
    ("Electrode", "electric", 36.99, "El Pokémon más rápido jamás registrado."),
    ("Exeggcute", "grass", 19.99, "Seis huevos conectados mentalmente."),
    ("Exeggutor", "grass", 41.99, "Tiene tres cabezas y puede pensar independientemente."),
    ("Cubone", "ground", 22.99, "Llora debajo de su máscara ósea."),
    ("Marowak", "ground", 37.99, "Usa su cola como arma principal."),
    ("Hitmonlee", "fighting", 43.99, "Patadas increíblemente poderosas."),
    ("Hitmonchan", "fighting", 43.99, "Puños igual de devastadores."),
    ("Lickitung", "normal", 25.99, "Su lengua es extremadamente larga y pegajosa."),
    ("Koffing", "poison", 26.99, "Libera gases venenosos como defensa."),
    ("Weezing", "poison", 41.99, "Dos Koffing fusionados juntos."),
    ("Rhyhorn", "ground", 34.99, "Su coraza es casi impenetrable."),
    ("Rhydon", "ground", 54.99, "Extremadamente peligroso en batalla."),
    ("Chansey", "normal", 38.99, "Siempre lleva un huevo con ella."),
    ("Kangaskhan", "normal", 47.99, "Protege ferozmente a su bebé."),
    ("Horsea", "water", 22.99, "Vive en los arrecifes coralinos."),
    ("Seadra", "water", 41.99, "Sus aletas son como espadas afiladas."),
    ("Goldeen", "water", 24.99, "La joya del reino acuático."),
    ("Seaking", "water", 39.99, "Increíblemente territorial durante el desove."),
    ("Staryu", "water", 26.99, "Regenera sus brazos si se pierden."),
    ("Starmie", "water", 45.99, "Brilla como una joya en el agua."),
    ("Magikarp", "water", 12.99, "El Pokémon más débil, pero puede evolucionar."),
    ("Gyarados", "water", 59.99, "Destructivo y de naturaleza violenta."),
    ("Lapras", "water", 64.99, "Puede viajar a través del océano."),
    ("Ditto", "normal", 34.99, "Puede transformarse en cualquier Pokémon."),
    ("Eevee", "normal", 17.99, "Tiene múltiples posibilidades de evolución."),
    ("Vaporeon", "water", 36.99, "Evoluciona cuando está cerca del agua."),
    ("Jolteon", "electric", 36.99, "Evoluciona con una piedra eléctrica."),
    ("Flareon", "fire", 36.99, "Evoluciona con una piedra de fuego."),
    ("Porygon", "normal", 48.99, "Un Pokémon hecho completamente de software."),
    ("Omanyte", "rock", 28.99, "Un Pokémon fósil antiguo revivido."),
    ("Omastar", "rock", 44.99, "Extinto hace millones de años."),
    ("Kabuto", "rock", 28.99, "Otro Pokémon fósil del pasado remoto."),
    ("Kabutops", "rock", 44.99, "Un depredador formidable de la antigüedad."),
    ("Aerodactyl", "rock", 59.99, "Un dinosaurio volador extremadamente raro."),
    ("Snorlax", "normal", 52.99, "Come todo el día y duerme en cualquier lugar."),
    ("Articuno", "ice", 89.99, "El legendario pájaro de hielo."),
    ("Zapdos", "electric", 89.99, "El legendario pájaro de rayo."),
    ("Moltres", "fire", 89.99, "El legendario pájaro de fuego."),
    ("Dratini", "dragon", 32.99, "Una pequeña serpiente dragón."),
    ("Dragonair", "dragon", 49.99, "Sus poderes aumentan enormemente."),
    ("Dragonite", "dragon", 84.99, "El rey de los dragones."),
    ("Mewtwo", "psychic", 99.99, "El Pokémon más fuerte jamás creado."),
    ("Mew", "psychic", 149.99, "El ancestro de todos los Pokémon."),
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
    help = "Carga 150 Pokémon con tipos, precios y descripciones"

    def handle(self, *args, **options):
        # Crear o recuperar categorías
        categorias = {}
        for tipo_slug, tipo_nombre in TIPOS.items():
            cat, created = Categoria.objects.get_or_create(
                nombre=tipo_nombre,
                defaults={"descripcion": f"Pokémon de tipo {tipo_nombre}"}
            )
            categorias[tipo_slug] = cat

        # Cargar Pokémon
        contador = 0
        for nombre, tipo_slug, precio, descripcion in POKEMONES:
            obj, created = Producto.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "categoria": categorias[tipo_slug],
                    "descripcion": descripcion,
                    "precio": Decimal(str(precio)),
                    "stock": 10,  # Stock inicial
                }
            )
            if created:
                contador += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"[OK] {contador} Pokémon cargados exitosamente. "
                f"Total ahora: {Producto.objects.count()}"
            )
        )
