# Investigación de Diseño E-commerce
## Referencias Visuales • Benchmark • Moodboard UI/UX

---

## 1. ANÁLISIS DE REFERENCIAS VISUALES

### 1.1 Tiendas E-commerce de Referencia

#### **Shopify/Productos Genéricos - Alto Rendimiento**
- **Tienda**: Amazon Product Pages
  - **Características clave**:
    - Hero section limpio con imagen grande del producto
    - Breadcrumb navigation clara
    - Grid de imágenes en miniatura lateral izquierda
    - Detalles de producto lado derecho (precio, rating, stock)
    - CTA principal destacado (Add to Cart)
    - Reseñas y ratings integradas

#### **Diseño Minimalista - Conversión Alta**
- **Tienda**: Uniqlo
  - **Características clave**:
    - Tipografía limpia y espacios en blanco generoso
    - Paleta de colores neutral (blanco, gris, negro)
    - Imágenes de producto en fondo limpio
    - Filters/Categorías laterales intuitivas
    - Hover effects sutiles en productos

#### **Premium & Aspiracional**
- **Tienda**: Apple Store / Lululemon
  - **Características clave**:
    - Imágenes de alta calidad (fotografía profesional)
    - Storytelling a través de categorías
    - Scroll infinito o paginación discreta
    - Tipografía sans-serif moderna
    - Espacios amplios entre elementos
    - Animaciones suaves y refinadas

#### **Diseño Dinámico - Gen Z**
- **Tienda**: Zara / Urban Outfitters
  - **Características clave**:
    - Carruseles de productos destacados
    - Grid dinámico (2-4 columnas responsive)
    - Overlay effects en hover (muestra información adicional)
    - Colores vibrantes en acciones (botones)
    - Badges/Labels para productos nuevos o en oferta

#### **Experiencia Social - Engagement**
- **Tienda**: Etsy / Depop
  - **Características clave**:
    - Reseñas y ratings prominentes
    - Fotos de usuarios reales (social proof)
    - Secciones de "Explorar" y "Descubrir"
    - Filtros avanzados pero no invasivos
    - Comunidad integrada

---

## 2. BENCHMARK COMPETITIVO

### 2.1 Matriz de Características Críticas

| Característica | Amazon | Shopify | Uniqlo | Apple | Zara | Etsy |
|---|---|---|---|---|---|---|
| **Navegación Principal** | Hamburger + Categorías | Clara y jerárquica | Limpia | Minimalista | Múltiples niveles | Simple |
| **Búsqueda/Filtros** | Avanzada | Buena | Excelente | Integrada | Múltiples | Básica |
| **Grid de Productos** | Flexible | Flexible | Fijo 4 cols | Flexible | Dinámico 2-4 | Masonry |
| **Imagen Principal** | Zoom, galería | Zoom, galería | Fija | Zoom inteligente | Carousel | Carousel |
| **Info Producto** | Lateral derecha | Bajo imagen | Lateral derecha | Debajo | Overlay | Debajo |
| **Rating/Reviews** | Prominente | Opcional | Integrado | Subtil | Integrado | Muy prominente |
| **CTA Principal** | Destacado | Destacado | Destacado | Minimalista | Vibrante | Destacado |
| **Carrito Flotante** | Fijo superior | Fijo superior | Fijo lateral | Fijo superior | Deslizable | Fijo superior |
| **Checkout** | Multi-step simple | Multi-step | Multi-step | Minimizado | Multi-step | Integrado |
| **Animaciones** | Sutiles | Sutiles | Mínimas | Fluidas | Modernas | Modernas |

### 2.2 Patrones de Conversión Validados

✅ **Elementos que AUMENTAN conversión:**
- CTA principal sobre fondo de color contraste
- Imágenes de producto de 360° o zoom
- Social proof (reseñas, cantidad de compras)
- Indicadores de urgencia (stock bajo, "últimas unidades")
- Shipping info visible antes de checkout
- Opciones de pago múltiples

❌ **Elementos que DISMINUYEN conversión:**
- Demasiados popups/overlays
- Autoplay de videos sin control
- Imágenes de mala calidad
- Falta de información de shipping
- CTA poco claro o secundario
- Proceso de checkout complejo (>3 pasos)

---

## 3. ARQUITECTURA UI/UX RECOMENDADA

### 3.1 Estructura de Navegación

```
┌─────────────────────────────────────────┐
│ HEADER (Sticky)                         │
│ Logo | Nav | Search | Cart | User       │
└─────────────────────────────────────────┘
│
├─ Home
├─ Categorías
│  ├─ Electrónica
│  ├─ Ropa
│  ├─ Hogar
│  └─ Accesorios
├─ Ofertas
├─ Nuevo
└─ Contacto
│
┌─────────────────────────────────────────┐
│ FOOTER                                  │
│ Links | Social | Newsletter | Info      │
└─────────────────────────────────────────┘
```

### 3.2 Flujos de Usuario Críticos

#### **Flujo: Exploración de Productos**
```
1. Landing Page → Hero + Featured Products
2. Categoría → Grid de Productos + Filtros
3. Producto → Detalles + Reviews + Related
4. Carrito → Quick View (sin dejar página)
5. Checkout → Pago
6. Confirmación
```

#### **Flujo: Búsqueda**
```
1. Search Box (header sticky)
2. Resultados con filtros laterales
3. Producto específico
4. Agregar al carrito
5. Checkout
```

---

## 4. PALETA DE COLORES & TIPOGRAFÍA

### 4.1 Paleta Recomendada (Versátil para Productos Genéricos)

**Opción 1: Limpia y Profesional** (Recomendada)
```
Primario:      #2563EB (Azul profesional)
Secundario:    #10B981 (Verde de éxito)
Acento:        #F59E0B (Naranja para ofertas)
Neutro Light:  #F3F4F6 (Fondo)
Neutro Dark:   #1F2937 (Texto principal)
Error:         #EF4444 (Rojo)
```

**Opción 2: Moderna y Vibrante** (Alternativa)
```
Primario:      #6366F1 (Índigo)
Secundario:    #EC4899 (Rosa)
Acento:        #14B8A6 (Teal)
Neutro Light:  #F8FAFC (Fondo)
Neutro Dark:   #0F172A (Texto)
Error:         #DC2626 (Rojo)
```

### 4.2 Tipografía Recomendada

**Heading (Títulos)**
- Font: Inter, Poppins o Outfit
- Peso: 600-700 (Semi-bold / Bold)
- Tamaño: H1 (32-48px), H2 (24-32px), H3 (18-24px)
- Uso: Titles, CTAs, nombres de producto

**Body (Cuerpo)**
- Font: Inter, System Font o Roboto
- Peso: 400-500 (Regular / Medium)
- Tamaño: 14-16px
- Line-height: 1.5-1.6

**Code/Small**
- Font: JetBrains Mono o similar
- Peso: 400
- Tamaño: 12-14px
- Uso: Precios, SKUs, información técnica

---

## 5. COMPONENTES CRÍTICOS

### 5.1 Hero Section
```
┌─────────────────────────────────┐
│  [Imagen Grande + Overlay]      │
│  Texto: "Descubre Nuestros      │
│         Productos"              │
│  CTA: [Explorar Ahora] ────────→│ (Color Primario)
└─────────────────────────────────┘
```
**Recomendaciones:**
- Altura: 60-70vh (viewport height)
- Imagen de alta calidad (lazy loaded)
- Overlay subtil para legibilidad de texto
- CTA claro y destacado

### 5.2 Grid de Productos
```
┌─────────────┬─────────────┬─────────────┐
│[Producto]   │[Producto]   │[Producto]   │
│             │             │             │
│ [Img]       │ [Img]       │ [Img]       │
│ Título      │ Título      │ Título      │
│ ⭐⭐⭐⭐⭐    │ ⭐⭐⭐⭐⭐    │ ⭐⭐⭐⭐⭐    │
│ $99 → $79   │ $99 → $79   │ $99 → $79   │
│ [+ Carrito] │ [+ Carrito] │ [+ Carrito] │
└─────────────┴─────────────┴─────────────┘
```
**Breakpoints:**
- Desktop: 4 columnas
- Tablet: 2-3 columnas
- Mobile: 1-2 columnas

### 5.3 Card de Producto (Detallado)
```
┌──────────────────────────────┐
│ [Badge "NUEVO"]              │
│ ┌──────────────────────────┐ │
│ │                          │ │
│ │    Imagen del Producto   │ │
│ │    (Responsive)          │ │
│ │                          │ │
│ └──────────────────────────┘ │
│ Nombre del Producto          │
│ ⭐ 4.8 (156 reseñas)         │
│ ────────────────────────────│
│ $99.99  [Antes: $129.99]    │
│ Stock: 15 unidades           │
│ ────────────────────────────│
│ [+ Agregar al Carrito]  ────→│ Verde
│ [♡ Guardar]                 │
└──────────────────────────────┘
```

### 5.4 Página de Producto Detallado
```
┌─────────────────────────────────────────┐
│ ← Atrás | Categoría > Subcategoría      │
├──────────────────┬──────────────────────┤
│  [Galería        │ Nombre Producto      │
│   Vertical       │ ⭐⭐⭐⭐⭐ (156)      │
│   360° View]     │ Precio: $99          │
│                  │ Stock: 15            │
│                  │ ────────────────────│
│                  │ [Talla] [Color]     │
│                  │ Cantidad: [- 1 +]   │
│                  │ ────────────────────│
│                  │ [✓ COMPRAR AHORA]   │
│                  │ [♡ GUARDAR]         │
│                  │ ────────────────────│
│                  │ • Envío en 2 días   │
│                  │ • Devoluciones fácil│
│                  │ • Garantía 1 año    │
└──────────────────┴──────────────────────┘
├─ Descripción
├─ Especificaciones
├─ Reseñas
└─ Productos Relacionados
```

### 5.5 Carrito (Flotante/Sidebar)
```
┌──────────────────────┐
│ Carrito (3 items)    │
├──────────────────────┤
│[Img] Producto 1      │
│      $79 x 1 = $79   │
│      [- 1 +] [x]     │
├──────────────────────┤
│[Img] Producto 2      │
│      $49 x 2 = $98   │
│      [- 1 +] [x]     │
├──────────────────────┤
│ Subtotal: $177       │
│ Envío: Calcular      │
│ Total: $177          │
├──────────────────────┤
│ [IR AL CARRITO]      │
│ [CONTINUAR COMPRA]   │
└──────────────────────┘
```

---

## 6. ANIMACIONES & MICRO-INTERACCIONES

### 6.1 Transiciones Recomendadas

| Elemento | Trigger | Animación | Duración |
|---|---|---|---|
| Hover en producto | Mouse over | Lift shadow + Zoom 1.05x | 200ms |
| Hover en botón | Mouse over | Scale 1.02x | 200ms |
| Agregar a carrito | Click | Pulse + Toast notificación | 400ms |
| Filtros | Change | Fade + Slide | 300ms |
| Navegación | Page change | Fade in | 300ms |
| Rating stars | Hover | Animate fill | 150ms |

### 6.2 Estados de Componentes

**Botón CTA**
- Default: Color primario
- Hover: Shade más oscuro + Cursor pointer
- Active: Scale 0.98x
- Disabled: Opacity 50% + Cursor not-allowed

**Card de Producto**
- Default: Shadow subtil
- Hover: Shadow más pronunciada + Translate Y -4px
- Active: Presionado

**Input/Search**
- Default: Border gris claro
- Focus: Border color primario + Shadow color primario
- Error: Border rojo

---

## 7. MOODBOARD VISUAL

### 7.1 Inspiración Estética

#### **Color Mood**
```
Profesional:     Azul + Blanco + Gris
Energía:         Verde + Naranja + Blanco
Premium:         Oscuro + Gold + Blanco
Moderno:         Índigo + Rosa + Blanco
```

#### **Tipografía Mood**
- Headlines: Bold, sans-serif, espaciado generoso
- Body: Regular, legible, line-height 1.6
- Accents: Medium weight para highlights

#### **Espaciado**
- Padding componentes: 16px / 24px / 32px
- Gap entre items: 16px / 24px
- Margen sections: 48px / 64px / 80px

#### **Bordes & Radios**
- Cards: 8px - 12px border-radius
- Botones: 6px - 8px border-radius
- Inputs: 6px border-radius
- Líneas divisoras: 1px, color neutro claro

---

## 8. RECOMENDACIONES PARA ESTE PROYECTO

### 8.1 Componentes a Implementar/Mejorar

Basado en tu archivo `components.tsx`, recomiendo enfoque en:

✅ **Ya presente:**
- `hero-section.tsx` → Mantener limpio y responsive
- `products-section.tsx` → Grid flexible 4/3/2/1 columnas
- `pokemon-card.tsx` → Card bien estructurado

🔄 **A Mejorar:**
- Agregar **product-detail page** con galería 360°
- Mejorar **cart experience** (persistencia, actualizaciones)
- Crear **filters component** avanzado
- Implementar **wishlist/favorites**
- Agregar **reviews section** con photos de usuarios

### 8.2 Paleta de Colores Propuesta

Para tienda de productos genéricos (Pokemon/Coleccionables):

```tsx
// colors.ts
export const colors = {
  primary: {
    50: '#EFF6FF',
    500: '#2563EB',
    600: '#1D4ED8',
    700: '#1E40AF',
  },
  success: {
    500: '#10B981',
    600: '#059669',
  },
  warning: {
    500: '#F59E0B',
    600: '#D97706',
  },
  neutral: {
    50: '#F9FAFB',
    100: '#F3F4F6',
    200: '#E5E7EB',
    500: '#6B7280',
    700: '#374151',
    900: '#111827',
  }
}
```

### 8.3 Tipografía Propuesta

```tsx
// typography.ts
export const typography = {
  h1: 'font-bold text-4xl md:text-5xl',
  h2: 'font-bold text-3xl md:text-4xl',
  h3: 'font-semibold text-2xl',
  body: 'font-normal text-base leading-relaxed',
  small: 'font-normal text-sm',
  caption: 'font-normal text-xs text-neutral-500',
}
```

### 8.4 Estructura de Página Recomendada

```
1. Header (Sticky)
   - Logo
   - Nav principal
   - Search bar
   - Cart icon
   - User account

2. Hero Section
   - Banner grande
   - CTA principal

3. Categorías
   - Grid horizontal o carousel
   - Scroll horizontal mobile

4. Productos Destacados
   - Grid 4/3/2/1 responsive
   - Sort/Filter sidebar
   - Load more / Paginación

5. Newsletter
   - Email signup
   - Background subtil

6. Footer
   - Links útiles
   - Social media
   - Contact info
```

---

## 9. REFERENCIAS EXTERNAS DE INSPIRACIÓN

### Recursos de Diseño
- **Dribbble**: Buscar "e-commerce product page"
- **Behance**: Keyword "shopify design"
- **Awwwards**: Tiendas online premiadas
- **Nike Store**: Premium execution
- **Vercel Showcase**: Proyectos Next.js

### Herramientas de Investigación
- **SimilarWeb**: Analytics de tiendas competencia
- **WhatFont**: Identificar tipografías
- **Adobe Color**: Extraer paletas de referencias
- **Figma Community**: Design systems gratuitos

---

## 10. CHECKLIST DE IMPLEMENTACIÓN

- [ ] Definir paleta de colores definitiva
- [ ] Seleccionar tipografía (headlines + body)
- [ ] Crear sistema de espaciado (spacing scale)
- [ ] Implementar breakpoints responsive
- [ ] Diseñar y codear hero section
- [ ] Grid de productos con filtros
- [ ] Página de detalle de producto
- [ ] Sistema de carrito con persistencia
- [ ] Checkout flow (al menos 3 pasos)
- [ ] Agregar micro-interacciones (hover, click)
- [ ] Testing en dispositivos reales
- [ ] Performance optimization (image optimization, lazy loading)
- [ ] Accesibilidad (WCAG 2.1 AA)

---

## CONCLUSIÓN

Para una tienda e-commerce de productos genéricos exitosa, el enfoque debe ser:
1. **Simplicidad**: Navegación clara, sin ruido visual
2. **Confianza**: Social proof, información de envío, reviews
3. **Conversión**: CTAs prominentes, proceso checkout simple
4. **Performance**: Imágenes optimizadas, carga rápida
5. **Responsive**: Perfecta en mobile, tablet, desktop

El diseño debe salir del camino y dejar que el producto brille. Menos es más.

---

*Documento generado: Mayo 2026*
*Stack: Next.js 14 + React + TypeScript + Tailwind CSS*
