"use client"

import { useState, useRef } from "react"
import { ShoppingCart } from "lucide-react"
import { Button } from "@/components/ui/button"

interface PokemonCardProps {
  name: string
  type: string
  hp: number
  attack: string
  attackDescription?: string
  attackDamage: number
  secondAttack?: string
  secondAttackDamage?: number
  weakness: string
  resistance: string
  retreatCost: number
  price: number
  image: string
  rarity: "common" | "uncommon" | "rare" | "ultra-rare"
  cardNumber?: string
  flavorText?: string
}

export function PokemonCard({
  name,
  type,
  hp,
  attack,
  attackDescription = "",
  attackDamage,
  secondAttack = "",
  secondAttackDamage = 0,
  weakness,
  resistance,
  retreatCost = 1,
  price,
  image,
  rarity,
  cardNumber = "001/151",
  flavorText = "Coleccionable exclusivo de Funkomon.",
}: PokemonCardProps) {
  const cardRef = useRef<HTMLDivElement>(null)
  const [rotation, setRotation] = useState({ x: 0, y: 0 })
  const [isHovered, setIsHovered] = useState(false)

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current) return

    const rect = cardRef.current.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    const centerX = rect.width / 2
    const centerY = rect.height / 2

    const rotateX = (y - centerY) / 8
    const rotateY = (centerX - x) / 8

    setRotation({ x: rotateX, y: rotateY })
  }

  const handleMouseLeave = () => {
    setRotation({ x: 0, y: 0 })
    setIsHovered(false)
  }

  const handleMouseEnter = () => {
    setIsHovered(true)
  }

  // Type colors matching Pokemon card colors
  const getTypeStyles = () => {
    switch (type.toLowerCase()) {
      case "electric":
        return { 
          border: "#FFCB08", 
          bg: "linear-gradient(180deg, #FFF9C4 0%, #FFEB3B 50%, #FBC02D 100%)",
          icon: "⚡"
        }
      case "fire":
        return { 
          border: "#E21C25", 
          bg: "linear-gradient(180deg, #FFCCBC 0%, #FF7043 50%, #E64A19 100%)",
          icon: "🔥"
        }
      case "water":
        return { 
          border: "#3561AD", 
          bg: "linear-gradient(180deg, #B3E5FC 0%, #29B6F6 50%, #0288D1 100%)",
          icon: "💧"
        }
      case "grass":
        return { 
          border: "#4CAF50", 
          bg: "linear-gradient(180deg, #C8E6C9 0%, #66BB6A 50%, #43A047 100%)",
          icon: "🌿"
        }
      case "psychic":
        return { 
          border: "#9C27B0", 
          bg: "linear-gradient(180deg, #E1BEE7 0%, #AB47BC 50%, #7B1FA2 100%)",
          icon: "🔮"
        }
      case "fighting":
        return { 
          border: "#BF360C", 
          bg: "linear-gradient(180deg, #FFCCBC 0%, #FF7043 50%, #BF360C 100%)",
          icon: "👊"
        }
      case "normal":
        return { 
          border: "#9E9E9E", 
          bg: "linear-gradient(180deg, #FAFAFA 0%, #E0E0E0 50%, #BDBDBD 100%)",
          icon: "⭐"
        }
      default:
        return { 
          border: "#3561AD", 
          bg: "linear-gradient(180deg, #B3E5FC 0%, #29B6F6 50%, #0288D1 100%)",
          icon: "💧"
        }
    }
  }

  const typeStyles = getTypeStyles()

  const getRarityStars = () => {
    switch (rarity) {
      case "ultra-rare": return "★★★★"
      case "rare": return "★★★"
      case "uncommon": return "★★"
      default: return "★"
    }
  }

  // Energy icons based on type
  const EnergyIcon = ({ energyType = type }: { energyType?: string }) => {
    const colors: Record<string, { bg: string; border: string }> = {
      electric: { bg: "#FFCB08", border: "#B8860B" },
      fire: { bg: "#E21C25", border: "#8B0000" },
      water: { bg: "#3561AD", border: "#1A237E" },
      grass: { bg: "#4CAF50", border: "#2E7D32" },
      psychic: { bg: "#9C27B0", border: "#4A148C" },
      fighting: { bg: "#BF360C", border: "#6D1B0C" },
      normal: { bg: "#9E9E9E", border: "#616161" },
      colorless: { bg: "#FFFFFF", border: "#9E9E9E" },
    }
    const style = colors[energyType.toLowerCase()] || colors.colorless
    return (
      <div 
        className="w-4 h-4 rounded-full flex items-center justify-center text-[8px] shadow-sm"
        style={{ 
          background: style.bg, 
          border: `1.5px solid ${style.border}`,
        }}
      >
        {energyType.toLowerCase() === "colorless" ? "☆" : ""}
      </div>
    )
  }

  return (
    <div
      ref={cardRef}
      className="pokemon-card cursor-pointer w-[280px]"
      style={{
        perspective: "1000px",
      }}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      onMouseEnter={handleMouseEnter}
    >
      <div
        className="relative transition-transform duration-150 ease-out"
        style={{
          transform: `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg) ${isHovered ? "scale(1.05)" : "scale(1)"}`,
          transformStyle: "preserve-3d",
        }}
      >
        {/* Card Outer Border */}
        <div 
          className="rounded-xl p-[3px] shadow-2xl"
          style={{
            background: typeStyles.border,
            boxShadow: isHovered ? `0 20px 40px rgba(0,0,0,0.4), 0 0 20px ${typeStyles.border}40` : "0 10px 30px rgba(0,0,0,0.3)",
          }}
        >
          {/* Card Inner */}
          <div 
            className="rounded-lg overflow-hidden"
            style={{ background: typeStyles.bg }}
          >
            {/* Holographic Shine Effect */}
            <div
              className="absolute inset-0 pointer-events-none z-20 rounded-lg"
              style={{
                background: `linear-gradient(105deg, transparent 30%, rgba(255,255,255,0.3) 45%, rgba(255,255,255,0.5) 50%, rgba(255,255,255,0.3) 55%, transparent 70%)`,
                transform: `translateX(${rotation.y * 8}px)`,
                opacity: isHovered ? 1 : 0,
                transition: "opacity 0.3s ease",
              }}
            />

            <div className="p-2.5 relative">
              {/* Top Row: Stage, Name, HP */}
              <div className="flex items-center justify-between mb-1.5">
                <div className="flex items-center gap-2">
                  <span 
                    className="text-[8px] font-mono px-1.5 py-0.5 rounded bg-white/80 text-gray-700 border border-gray-300"
                  >
                    BASICO
                  </span>
                  <span className="font-mono text-sm text-gray-900 font-bold tracking-tight">
                    {name}
                  </span>
                </div>
                <div className="flex items-center gap-1">
                  <span className="text-[10px] font-mono text-gray-700">PS</span>
                  <span className="font-mono text-xl font-bold text-gray-900">{hp}</span>
                  <span className="text-lg">{typeStyles.icon}</span>
                </div>
              </div>

              {/* Image Container - Pokemon TCG Style */}
              <div 
                className="relative rounded border-4 mb-1.5 overflow-hidden"
                style={{ borderColor: typeStyles.border }}
              >
                <div className="bg-gradient-to-b from-blue-200 via-blue-100 to-green-100 h-28 flex items-center justify-center relative">
                  {/* Background scene */}
                  <div className="absolute inset-0 opacity-30">
                    <div className="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-green-300 to-transparent" />
                    <div className="absolute top-2 right-3 w-6 h-6 bg-yellow-200 rounded-full blur-sm" />
                  </div>
                  {/* Pokemon/Funko Image */}
                  <span className="text-6xl relative z-10 drop-shadow-lg">{image}</span>
                </div>
                {/* Info bar under image */}
                <div className="bg-white/90 px-2 py-0.5 flex justify-between items-center text-[7px] text-gray-500 font-mono">
                  <span>N.º FUNKO Edicion Funkomon</span>
                  <span>Alt: 0.4 m Peso: 6.0 kg</span>
                </div>
              </div>

              {/* Type Tag */}
              <div className="flex justify-center mb-2">
                <span 
                  className="text-[9px] font-mono px-3 py-0.5 rounded-full text-white shadow-sm"
                  style={{ background: typeStyles.border }}
                >
                  Funko Pop tipo {type}
                </span>
              </div>

              {/* Attacks Section */}
              <div className="bg-white/60 rounded-lg p-2 mb-2 space-y-2">
                {/* First Attack */}
                <div className="border-b border-gray-300/50 pb-2">
                  <div className="flex items-start justify-between">
                    <div className="flex items-center gap-2">
                      <div className="flex gap-0.5">
                        <EnergyIcon />
                        <EnergyIcon energyType="colorless" />
                      </div>
                      <div>
                        <span className="font-mono text-xs font-bold text-gray-900">{attack}</span>
                        {attackDescription && (
                          <p className="text-[7px] text-gray-600 mt-0.5 max-w-[150px] leading-tight">
                            {attackDescription}
                          </p>
                        )}
                      </div>
                    </div>
                    <span className="font-mono text-base font-bold text-gray-900">{attackDamage}</span>
                  </div>
                </div>

                {/* Second Attack */}
                {secondAttack && (
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <div className="flex gap-0.5">
                        <EnergyIcon />
                        <EnergyIcon />
                      </div>
                      <span className="font-mono text-xs font-bold text-gray-900">{secondAttack}</span>
                    </div>
                    <span className="font-mono text-base font-bold text-gray-900">{secondAttackDamage}</span>
                  </div>
                )}
              </div>

              {/* Bottom Stats Row */}
              <div className="flex justify-between items-center text-[8px] mb-2 px-1 bg-white/40 rounded py-1">
                <div className="flex items-center gap-1">
                  <span className="text-gray-600 font-mono">Debilidad</span>
                  <div className="flex items-center">
                    <span className="text-sm">{weakness === "fire" ? "🔥" : weakness === "water" ? "💧" : weakness === "grass" ? "🌿" : "⚡"}</span>
                    <span className="text-gray-900 font-bold">×2</span>
                  </div>
                </div>
                <div className="flex items-center gap-1">
                  <span className="text-gray-600 font-mono">Resistencia</span>
                  <span className="text-gray-400">—</span>
                </div>
                <div className="flex items-center gap-1">
                  <span className="text-gray-600 font-mono">Retirada</span>
                  <div className="flex gap-0.5">
                    {Array.from({ length: retreatCost }).map((_, i) => (
                      <EnergyIcon key={i} energyType="colorless" />
                    ))}
                  </div>
                </div>
              </div>

              {/* Flavor Text & Card Info */}
              <div className="bg-white/50 rounded p-1.5 mb-2">
                <p className="text-[7px] text-gray-600 italic leading-tight font-mono">
                  {flavorText}
                </p>
              </div>

              {/* Card Number & Illustrator */}
              <div className="flex justify-between items-center text-[7px] text-gray-500 font-mono px-1">
                <span>Illus. FUNKOMON</span>
                <span>{cardNumber} {getRarityStars()}</span>
              </div>

              {/* Price & Buy - Outside card aesthetic */}
              <div 
                className="mt-2 pt-2 flex items-center justify-between rounded-lg p-2"
                style={{ background: typeStyles.border }}
              >
                <div className="flex items-center gap-1">
                  <span className="font-mono text-lg font-bold text-white drop-shadow">${price}</span>
                  <span className="text-[10px] font-mono text-white/80">USD</span>
                </div>
                <Button
                  size="sm"
                  className="bg-white hover:bg-gray-100 text-gray-900 font-mono text-[10px] transition-colors shadow-md"
                >
                  <ShoppingCart className="w-3 h-3 mr-1" />
                  Comprar
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
