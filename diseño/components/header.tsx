"use client"

import { useState } from "react"
import { ShoppingCart, Menu, X, Search } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="sticky top-0 z-50 bg-[#07224E] border-b-4 border-[#FFCB08]">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center gap-2">
            <div className="relative">
              <div className="w-10 h-10 bg-[#E21C25] rounded-full flex items-center justify-center border-2 border-[#FFFFFF]">
                <div className="w-4 h-4 bg-[#FFFFFF] rounded-full border-2 border-[#07224E]" />
              </div>
            </div>
            <span className="text-xl font-bold font-mono">
              <span className="text-[#FFCB08]">FUNKO</span>
              <span className="text-[#FFFFFF]">MON</span>
            </span>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-6">
            <a href="#inicio" className="text-[#FFFFFF] hover:text-[#FFCB08] font-mono text-xs transition-colors">
              Inicio
            </a>
            <a href="#productos" className="text-[#FFFFFF] hover:text-[#FFCB08] font-mono text-xs transition-colors">
              Productos
            </a>
            <a href="#categorias" className="text-[#FFFFFF] hover:text-[#FFCB08] font-mono text-xs transition-colors">
              Categorías
            </a>
            <a href="#contacto" className="text-[#FFFFFF] hover:text-[#FFCB08] font-mono text-xs transition-colors">
              Contacto
            </a>
          </nav>

          {/* Search & Cart */}
          <div className="hidden md:flex items-center gap-4">
            <div className="relative">
              <Input
                type="search"
                placeholder="Buscar Funkos..."
                className="w-64 bg-[#0B4DA2] border-[#3561AD] text-[#FFFFFF] placeholder:text-[#BCBDC0] pr-10"
              />
              <Search className="absolute right-3 top-1/2 -translate-y-1/2 w-4 h-4 text-[#BCBDC0]" />
            </div>
            <Button className="bg-[#FFCB08] hover:bg-[#E21C25] text-[#07224E] hover:text-[#FFFFFF] relative">
              <ShoppingCart className="w-5 h-5" />
              <span className="absolute -top-2 -right-2 w-5 h-5 bg-[#E21C25] text-[#FFFFFF] text-xs rounded-full flex items-center justify-center">
                3
              </span>
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden text-[#FFFFFF]"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-[#3561AD]">
            <nav className="flex flex-col gap-4">
              <a href="#inicio" className="text-[#FFFFFF] hover:text-[#FFCB08] font-semibold transition-colors">
                Inicio
              </a>
              <a href="#productos" className="text-[#FFFFFF] hover:text-[#FFCB08] font-semibold transition-colors">
                Productos
              </a>
              <a href="#categorias" className="text-[#FFFFFF] hover:text-[#FFCB08] font-semibold transition-colors">
                Categorías
              </a>
              <a href="#contacto" className="text-[#FFFFFF] hover:text-[#FFCB08] font-semibold transition-colors">
                Contacto
              </a>
              <div className="flex items-center gap-4 pt-4 border-t border-[#3561AD]">
                <Input
                  type="search"
                  placeholder="Buscar Funkos..."
                  className="flex-1 bg-[#0B4DA2] border-[#3561AD] text-[#FFFFFF] placeholder:text-[#BCBDC0]"
                />
                <Button className="bg-[#FFCB08] hover:bg-[#E21C25] text-[#07224E] hover:text-[#FFFFFF] relative">
                  <ShoppingCart className="w-5 h-5" />
                  <span className="absolute -top-2 -right-2 w-5 h-5 bg-[#E21C25] text-[#FFFFFF] text-xs rounded-full flex items-center justify-center">
                    3
                  </span>
                </Button>
              </div>
            </nav>
          </div>
        )}
      </div>
    </header>
  )
}
