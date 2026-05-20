"use client"

import { PokemonCard } from "@/components/pokemon-card"
import { Button } from "@/components/ui/button"
import { ChevronRight } from "lucide-react"

const products = [
  {
    name: "Pikachu",
    type: "Electric",
    hp: 70,
    attack: "Grunido",
    attackDescription: "Durante el proximo turno de tu rival, los ataques del Pokemon Defensor hacen 20 puntos menos.",
    attackDamage: 20,
    secondAttack: "Rayo Pika",
    secondAttackDamage: 30,
    weakness: "fighting",
    resistance: "-",
    retreatCost: 1,
    price: 24.99,
    image: "⚡",
    rarity: "rare" as const,
    cardNumber: "062/193",
    flavorText: "Cuando se enfada, este Pokemon descarga la energia que almacena en el interior de las bolsas de las mejillas.",
  },
  {
    name: "Charizard",
    type: "Fire",
    hp: 180,
    attack: "Garra Dragon",
    attackDescription: "Este ataque hace 30 puntos de dano adicional por cada carta de Energia de Fuego unida a este Pokemon.",
    attackDamage: 80,
    secondAttack: "Llamarada",
    secondAttackDamage: 150,
    weakness: "water",
    resistance: "-",
    retreatCost: 3,
    price: 89.99,
    image: "🔥",
    rarity: "ultra-rare" as const,
    cardNumber: "004/165",
    flavorText: "Escupe fuego tan caliente que funde las rocas. Causa incendios forestales sin querer.",
  },
  {
    name: "Blastoise",
    type: "Water",
    hp: 160,
    attack: "Aqua Jet",
    attackDescription: "Lanza un potente chorro de agua a presion.",
    attackDamage: 50,
    secondAttack: "Hidrobomba",
    secondAttackDamage: 120,
    weakness: "electric",
    resistance: "-",
    retreatCost: 3,
    price: 54.99,
    image: "💧",
    rarity: "rare" as const,
    cardNumber: "009/165",
    flavorText: "Los chorros de agua que dispara son capaces de atravesar el acero.",
  },
  {
    name: "Bulbasaur",
    type: "Grass",
    hp: 70,
    attack: "Placaje",
    attackDescription: "",
    attackDamage: 10,
    secondAttack: "Latigo Cepa",
    secondAttackDamage: 30,
    weakness: "fire",
    resistance: "-",
    retreatCost: 1,
    price: 19.99,
    image: "🌿",
    rarity: "common" as const,
    cardNumber: "001/165",
    flavorText: "Una rara semilla fue plantada en su espalda al nacer. La planta brota y crece con este Pokemon.",
  },
  {
    name: "Mewtwo",
    type: "Psychic",
    hp: 190,
    attack: "Confusion",
    attackDescription: "Tu oponente voltea una moneda. Si es cruz, el Pokemon Defensor esta confundido.",
    attackDamage: 30,
    secondAttack: "Onda Mental",
    secondAttackDamage: 140,
    weakness: "psychic",
    resistance: "-",
    retreatCost: 2,
    price: 79.99,
    image: "🔮",
    rarity: "ultra-rare" as const,
    cardNumber: "150/165",
    flavorText: "Fue creado por un cientifico tras anos de horribles experimentos de ingenieria genetica.",
  },
  {
    name: "Gengar",
    type: "Psychic",
    hp: 130,
    attack: "Lengüetazo",
    attackDescription: "El Pokemon Defensor ahora esta Paralizado.",
    attackDamage: 20,
    secondAttack: "Bola Sombra",
    secondAttackDamage: 90,
    weakness: "psychic",
    resistance: "-",
    retreatCost: 0,
    price: 44.99,
    image: "👻",
    rarity: "rare" as const,
    cardNumber: "094/165",
    flavorText: "Le encanta esconderse en las sombras y hacer que la gente tiemble de miedo.",
  },
  {
    name: "Eevee",
    type: "Normal",
    hp: 60,
    attack: "Ataque Rapido",
    attackDescription: "Voltea una moneda. Si es cruz, este ataque no hace nada.",
    attackDamage: 30,
    secondAttack: "Mordisco",
    secondAttackDamage: 20,
    weakness: "fighting",
    resistance: "-",
    retreatCost: 1,
    price: 17.99,
    image: "🦊",
    rarity: "uncommon" as const,
    cardNumber: "133/165",
    flavorText: "Su codigo genetico es irregular. Puede evolucionar en varias formas diferentes.",
  },
  {
    name: "Squirtle",
    type: "Water",
    hp: 60,
    attack: "Burbuja",
    attackDescription: "Voltea una moneda. Si es cara, el Pokemon Defensor esta Paralizado.",
    attackDamage: 10,
    secondAttack: "Pistola Agua",
    secondAttackDamage: 30,
    weakness: "grass",
    resistance: "-",
    retreatCost: 1,
    price: 19.99,
    image: "🐢",
    rarity: "common" as const,
    cardNumber: "007/165",
    flavorText: "Cuando retrae su largo cuello en el caparazon, dispara agua a una presion increible.",
  },
]

export function ProductsSection() {
  return (
    <section id="productos" className="py-20 bg-[#07224E]">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between mb-12">
          <div>
            <span className="text-[#FFCB08] font-mono text-xs uppercase tracking-wider">
              Coleccion exclusiva
            </span>
            <h2 className="text-2xl md:text-3xl font-mono text-[#FFFFFF] mt-2">
              Productos Destacados
            </h2>
            <p className="text-[#BCBDC0] mt-2 max-w-xl text-lg">
              Descubre nuestros Funko Pop mas populares. Cada figura viene con su carta coleccionable.
            </p>
          </div>
          <Button
            variant="outline"
            className="mt-4 md:mt-0 border-[#FFCB08] text-[#FFCB08] hover:bg-[#FFCB08] hover:text-[#07224E]"
          >
            Ver Todo
            <ChevronRight className="w-4 h-4 ml-2" />
          </Button>
        </div>

        {/* Filter Tabs */}
        <div className="flex flex-wrap gap-2 mb-8">
          {["Todos", "Populares", "Nuevos", "En Oferta", "Exclusivos"].map((filter, index) => (
            <button
              key={filter}
              className={`px-4 py-2 rounded-full font-mono text-xs transition-all ${
                index === 0
                  ? "bg-[#FFCB08] text-[#07224E]"
                  : "bg-[#0B4DA2] text-[#FFFFFF] hover:bg-[#3561AD]"
              }`}
            >
              {filter}
            </button>
          ))}
        </div>

        {/* Products Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8 justify-items-center">
          {products.map((product) => (
            <PokemonCard key={product.name} {...product} />
          ))}
        </div>

        {/* Load More */}
        <div className="text-center mt-12">
          <Button
            size="lg"
            className="bg-[#3561AD] hover:bg-[#FFCB08] text-[#FFFFFF] hover:text-[#07224E] font-bold px-12"
          >
            Cargar Más Productos
          </Button>
        </div>
      </div>
    </section>
  )
}
