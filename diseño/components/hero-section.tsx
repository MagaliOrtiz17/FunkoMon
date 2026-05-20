"use client"

import { Button } from "@/components/ui/button"
import { Sparkles, Zap } from "lucide-react"

export function HeroSection() {
  return (
    <section id="inicio" className="relative min-h-[80vh] flex items-center overflow-hidden">
      {/* Background Pattern */}
      <div className="absolute inset-0 bg-[#07224E]">
        <div className="absolute inset-0 opacity-10">
          {Array.from({ length: 50 }).map((_, i) => (
            <div
              key={i}
              className="absolute w-8 h-8 border-2 border-[#FFCB08] rounded-full"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
                animationDelay: `${Math.random() * 2}s`,
              }}
            />
          ))}
        </div>
      </div>

      {/* Animated Pokeball Background */}
      <div className="absolute right-0 top-1/2 -translate-y-1/2 opacity-20">
        <div className="w-96 h-96 relative">
          <div className="absolute inset-0 bg-[#E21C25] rounded-full" />
          <div className="absolute inset-x-0 bottom-0 h-1/2 bg-[#FFFFFF] rounded-b-full" />
          <div className="absolute inset-x-0 top-1/2 -translate-y-1/2 h-8 bg-[#07224E]" />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-24 h-24 bg-[#FFFFFF] rounded-full border-8 border-[#07224E]" />
        </div>
      </div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-2xl">
          <div className="flex items-center gap-2 mb-4">
            <Sparkles className="w-6 h-6 text-[#FFCB08]" />
            <span className="text-[#FFCB08] font-mono text-sm">La coleccion definitiva!</span>
          </div>

          <h1 className="text-3xl md:text-5xl font-mono mb-6 leading-relaxed">
            <span className="text-[#FFFFFF]">Colecciona</span>
            <br />
            <span className="text-[#FFCB08]">Tus Pokemon</span>
            <br />
            <span className="text-[#E21C25]">Favoritos</span>
          </h1>

          <p className="text-[#BCBDC0] text-lg mb-8 leading-relaxed">
            Descubre la colección más grande de Funko Pop de Pokémon. 
            Desde los clásicos hasta las ediciones más exclusivas. 
            ¡Hazte con todos!
          </p>

          <div className="flex flex-wrap gap-4">
            <Button
              size="lg"
              className="bg-[#FFCB08] hover:bg-[#E21C25] text-[#07224E] hover:text-[#FFFFFF] font-bold text-lg px-8 transition-all hover:scale-105"
            >
              <Zap className="w-5 h-5 mr-2" />
              Ver Colección
            </Button>
            <Button
              size="lg"
              variant="outline"
              className="border-[#FFCB08] text-[#FFCB08] hover:bg-[#FFCB08] hover:text-[#07224E] font-bold text-lg px-8"
            >
              Novedades
            </Button>
          </div>

          {/* Stats */}
          <div className="flex gap-8 mt-12 pt-8 border-t border-[#3561AD]">
            <div>
              <div className="text-2xl font-mono text-[#FFCB08]">500+</div>
              <div className="text-[#BCBDC0] text-xs font-mono">Funkos</div>
            </div>
            <div>
              <div className="text-2xl font-mono text-[#E21C25]">150+</div>
              <div className="text-[#BCBDC0] text-xs font-mono">Pokemon</div>
            </div>
            <div>
              <div className="text-2xl font-mono text-[#3561AD]">50k+</div>
              <div className="text-[#BCBDC0] text-xs font-mono">Clientes</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
