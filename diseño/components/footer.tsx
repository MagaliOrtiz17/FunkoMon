import { Facebook, Instagram, Twitter, Youtube, Mail, Phone, MapPin } from "lucide-react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export function Footer() {
  return (
    <footer id="contacto" className="bg-[#07224E] border-t-4 border-[#FFCB08]">
      {/* Newsletter Section */}
      <div className="bg-gradient-to-r from-[#0B4DA2] to-[#3561AD] py-12">
        <div className="container mx-auto px-4">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div>
              <h3 className="text-base font-mono text-[#FFFFFF]">
                Unete a nuestra comunidad!
              </h3>
              <p className="text-[#BCBDC0] text-lg">
                Recibe las ultimas novedades y ofertas exclusivas
              </p>
            </div>
            <div className="flex gap-2 w-full md:w-auto">
              <Input
                type="email"
                placeholder="Tu email..."
                className="bg-[#07224E] border-[#3561AD] text-[#FFFFFF] placeholder:text-[#BCBDC0] md:w-64"
              />
              <Button className="bg-[#FFCB08] hover:bg-[#E21C25] text-[#07224E] hover:text-[#FFFFFF] font-mono text-xs whitespace-nowrap">
                Suscribirse
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Footer */}
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Brand Column */}
          <div>
            <div className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 bg-[#E21C25] rounded-full flex items-center justify-center border-2 border-[#FFFFFF]">
                <div className="w-4 h-4 bg-[#FFFFFF] rounded-full border-2 border-[#07224E]" />
              </div>
              <span className="text-lg font-mono">
                <span className="text-[#FFCB08]">FUNKO</span>
                <span className="text-[#FFFFFF]">MON</span>
              </span>
            </div>
            <p className="text-[#BCBDC0] text-sm mb-4">
              La tienda #1 de Funko Pop de Pokémon. Colecciona todos tus favoritos con nosotros.
            </p>
            <div className="flex gap-4">
              <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] transition-colors">
                <Facebook className="w-5 h-5" />
              </a>
              <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] transition-colors">
                <Instagram className="w-5 h-5" />
              </a>
              <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] transition-colors">
                <Twitter className="w-5 h-5" />
              </a>
              <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] transition-colors">
                <Youtube className="w-5 h-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-[#FFFFFF] font-mono text-xs mb-4">Enlaces Rapidos</h4>
            <ul className="space-y-2">
              {["Inicio", "Productos", "Categorías", "Ofertas", "Novedades"].map((link) => (
                <li key={link}>
                  <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] text-sm transition-colors">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Help */}
          <div>
            <h4 className="text-[#FFFFFF] font-mono text-xs mb-4">Ayuda</h4>
            <ul className="space-y-2">
              {["Preguntas Frecuentes", "Envíos", "Devoluciones", "Términos", "Privacidad"].map((link) => (
                <li key={link}>
                  <a href="#" className="text-[#BCBDC0] hover:text-[#FFCB08] text-sm transition-colors">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-[#FFFFFF] font-mono text-xs mb-4">Contacto</h4>
            <ul className="space-y-3">
              <li className="flex items-center gap-2 text-[#BCBDC0] text-sm">
                <Mail className="w-4 h-4 text-[#FFCB08]" />
                info@funkomon.com
              </li>
              <li className="flex items-center gap-2 text-[#BCBDC0] text-sm">
                <Phone className="w-4 h-4 text-[#FFCB08]" />
                +1 (555) 123-4567
              </li>
              <li className="flex items-center gap-2 text-[#BCBDC0] text-sm">
                <MapPin className="w-4 h-4 text-[#FFCB08]" />
                Pallet Town, Kanto 12345
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-[#3561AD] py-6">
        <div className="container mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-4">
          <p className="text-[#BCBDC0] text-sm text-center md:text-left">
            © 2024 Funkomon. Todos los derechos reservados. Pokémon es una marca registrada.
          </p>
          <div className="flex gap-4">
            <img src="https://img.icons8.com/color/48/visa.png" alt="Visa" className="h-8" />
            <img src="https://img.icons8.com/color/48/mastercard.png" alt="Mastercard" className="h-8" />
            <img src="https://img.icons8.com/color/48/paypal.png" alt="PayPal" className="h-8" />
          </div>
        </div>
      </div>
    </footer>
  )
}
