"use client"

import { Zap, Flame, Droplets, Leaf, Star, Ghost, Moon, Mountain } from "lucide-react"

const categories = [
  {
    name: "Eléctrico",
    icon: Zap,
    color: "bg-[#FFCB08]",
    textColor: "text-[#07224E]",
    count: 45,
    emoji: "⚡",
  },
  {
    name: "Fuego",
    icon: Flame,
    color: "bg-[#E21C25]",
    textColor: "text-[#FFFFFF]",
    count: 38,
    emoji: "🔥",
  },
  {
    name: "Agua",
    icon: Droplets,
    color: "bg-[#3561AD]",
    textColor: "text-[#FFFFFF]",
    count: 52,
    emoji: "💧",
  },
  {
    name: "Planta",
    icon: Leaf,
    color: "bg-green-500",
    textColor: "text-[#FFFFFF]",
    count: 41,
    emoji: "🌿",
  },
  {
    name: "Psíquico",
    icon: Star,
    color: "bg-purple-500",
    textColor: "text-[#FFFFFF]",
    count: 33,
    emoji: "🔮",
  },
  {
    name: "Fantasma",
    icon: Ghost,
    color: "bg-purple-800",
    textColor: "text-[#FFFFFF]",
    count: 28,
    emoji: "👻",
  },
  {
    name: "Siniestro",
    icon: Moon,
    color: "bg-[#07224E]",
    textColor: "text-[#FFFFFF]",
    count: 25,
    emoji: "🌙",
  },
  {
    name: "Roca",
    icon: Mountain,
    color: "bg-[#BCBDC0]",
    textColor: "text-[#07224E]",
    count: 31,
    emoji: "🪨",
  },
]

export function CategoriesSection() {
  return (
    <section id="categorias" className="py-20 bg-[#0B4DA2]">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-12">
          <span className="text-[#FFCB08] font-mono text-xs uppercase tracking-wider">
            Explora por tipo
          </span>
          <h2 className="text-2xl md:text-3xl font-mono text-[#FFFFFF] mt-2 mb-4">
            Categorias
          </h2>
          <p className="text-[#BCBDC0] max-w-2xl mx-auto text-lg">
            Encuentra tu tipo favorito de Pokemon y descubre nuestra coleccion completa de Funko Pop
          </p>
        </div>

        {/* Categories Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {categories.map((category) => {
            const Icon = category.icon
            return (
              <div
                key={category.name}
                className="group cursor-pointer"
              >
                <div className="relative bg-[#07224E] rounded-2xl p-6 border-2 border-[#3561AD] hover:border-[#FFCB08] transition-all duration-300 hover:scale-105 hover:shadow-lg hover:shadow-[#FFCB08]/20">
                  {/* Category Icon */}
                  <div className={`${category.color} w-16 h-16 rounded-full flex items-center justify-center mb-4 mx-auto group-hover:scale-110 transition-transform`}>
                    <span className="text-3xl">{category.emoji}</span>
                  </div>

                  {/* Category Info */}
                  <h3 className="text-[#FFFFFF] font-mono text-xs text-center mb-1">
                    {category.name}
                  </h3>
                  <p className="text-[#BCBDC0] text-base text-center">
                    {category.count} Funkos
                  </p>

                  {/* Hover Overlay */}
                  <div className="absolute inset-0 bg-gradient-to-t from-[#FFCB08]/10 to-transparent rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity" />
                </div>
              </div>
            )
          })}
        </div>

        {/* Featured Types Banner */}
        <div className="mt-12 bg-gradient-to-r from-[#FFCB08] via-[#E21C25] to-[#3561AD] p-1 rounded-2xl">
          <div className="bg-[#07224E] rounded-xl p-6 md:p-8 flex flex-col md:flex-row items-center justify-between gap-4">
            <div>
              <h3 className="text-[#FFFFFF] font-mono text-sm md:text-base">
                No encuentras tu tipo favorito?
              </h3>
              <p className="text-[#BCBDC0] text-lg">
                Tenemos mas de 18 tipos diferentes de Pokemon Funko Pop
              </p>
            </div>
            <button className="bg-[#FFCB08] hover:bg-[#E21C25] text-[#07224E] hover:text-[#FFFFFF] font-mono text-xs px-6 py-3 rounded-lg transition-colors whitespace-nowrap">
              Ver Todos los Tipos
            </button>
          </div>
        </div>
      </div>
    </section>
  )
}
