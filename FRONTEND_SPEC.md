# 🎭 FunkoMon — Especificación Frontend

**Proyecto:** E-commerce de figuras Funko Pop con autenticación biométrica  
**Semana:** 1 - Especificación UI/UX  
**Desarrollador:** Frontend

---

## 📍 1. MAPA DE NAVEGACIÓN

```
┌─────────────────────────────────────────────────────┐
│                    FUNKOMON                         │
│         E-commerce Funko Pop + Face ID              │
└─────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    [NO AUTENTICADO]   [AUTENTICADO]    [ADMIN/STAFF]
        │                  │                  │
        ├─ Inicio          ├─ Inicio         ├─ Dashboard
        ├─ Catálogo        ├─ Catálogo       ├─ Gestionar Productos
        ├─ Producto Detail ├─ Carrito        ├─ Gestionar Pedidos
        ├─ Login           ├─ Checkout       └─ Gestionar Usuarios
        └─ Registro        ├─ Mi Perfil
                           ├─ Mis Pedidos
                           ├─ Face ID
                           └─ Cerrar Sesión
```

### 📊 Jerarquía de Rutas

**Sistema de Autenticación:**
- `/` → Home (Pública)
- `/login` → Formulario de Login + Face ID
- `/registro` → Formulario de Registro + Captura Biométrica

**Catálogo (Pública):**
- `/productos` → Listado de productos (con filtros)
- `/productos/:id` → Detalle de producto

**Carrito & Checkout (Autenticada):**
- `/carrito` → Ver carrito
- `/checkout` → Procesar pago
- `/pedidos/:id` → Confirmación de pedido

**Perfil de Usuario (Autenticada):**
- `/perfil` → Editar datos personales
- `/perfil/biometria` → Configurar/actualizar Face ID
- `/mis-pedidos` → Historial de compras
- `/configuracion` → Preferencias

---

## 🎨 2. BOCETOS DE PANTALLAS

### A. PANTALLA DE INICIO (Home)
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]        🔍 Buscar...    👤 | 🛒 | ☰  │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌────────────────────────────────────────────────┐  │
│  │     BIENVENIDO A FUNKOMON                      │  │
│  │   Tu tienda de Funko Pop favorita              │  │
│  │                                                │  │
│  │   [Explorar Catálogo]  [Ver Ofertas]          │  │
│  └────────────────────────────────────────────────┘  │
│                                                       │
│  ━━━ CATEGORÍAS DESTACADAS ━━━                       │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ Películas│  │ Series   │  │ Deportes │           │
│  │   20     │  │   15     │  │   10     │           │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                       │
│  ━━━ PRODUCTOS DESTACADOS ━━━                        │
│                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │
│  │ [Imagen]    │  │ [Imagen]    │  │ [Imagen]    │  │
│  │ Producto 1  │  │ Producto 2  │  │ Producto 3  │  │
│  │ $29.99 ⭐⭐ │  │ $34.99 ⭐⭐⭐│  │ $49.99 ⭐   │  │
│  │ [Agregar]   │  │ [Agregar]   │  │ [Agregar]   │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### B. PANTALLA DE CATÁLOGO (Productos)
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]        🔍 Buscar...    👤 | 🛒 | ☰  │
├──────────────────────────────────────────────────────┤
│                                                       │
│ [Filtros ▼]                                          │
│ ├─ Categoría: [Todos ▼]                             │
│ ├─ Precio: $[0] — $[100]                            │
│ ├─ Rating: [⭐⭐⭐+]                                │
│ └─ [Aplicar] [Limpiar]                              │
│                                                       │
├──────────────────────────────────────────────────────┤
│ Mostrando 1-12 de 45 productos | Ordenar: [Precio▼] │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ [Imagen] │  │ [Imagen] │  │ [Imagen] │           │
│  │ Funko 1  │  │ Funko 2  │  │ Funko 3  │           │
│  │ $29.99   │  │ $34.99   │  │ $49.99   │           │
│  │ 🏷 Film  │  │ 🏷 Serie │  │ 🏷 Games │           │
│  │ ⭐⭐⭐⭐  │  │ ⭐⭐⭐  │  │ ⭐⭐    │           │
│  │ [Detalles]   │ [Detalles]   │ [Detalles]          │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │ [Imagen] │  │ [Imagen] │  │ [Imagen] │           │
│  │   ...    │  │   ...    │  │   ...    │           │
│  └──────────┘  └──────────┘  └──────────┘           │
│                                                       │
│  [◄ Anterior]  1  2  3  ...  [Siguiente ►]          │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### C. PANTALLA DE DETALLE DE PRODUCTO
```
┌──────────────────────────────────────────────────────┐
│ [◄ Volver]  LOGO  🔍        👤 | 🛒 | ☰             │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌──────────────────┐    ┌─────────────────────────┐ │
│  │                  │    │ Funko Pop - Ironman    │ │
│  │                  │    │ Categoría: Marvel Film │ │
│  │    [Imagen       │    │ SKU: FM-001            │ │
│  │     Grande]      │    │                         │ │
│  │                  │    │ Precio: $49.99         │ │
│  │                  │    │ Rating: ⭐⭐⭐⭐⭐    │ │
│  │  ◄ [▼] ►        │    │ (127 reviews)          │ │
│  │ Miniaturas      │    │                         │ │
│  │  [img][img]     │    │ Stock: ✓ Disponible     │ │
│  │  [img][img]     │    │                         │ │
│  └──────────────────┘    │ Descripción:            │ │
│                          │ Funko Pop edición       │ │
│                          │ limitada de Ironman...  │ │
│                          │                         │ │
│                          │ Especificaciones:       │ │
│                          │ • Altura: 10cm          │ │
│                          │ • Edición: Limitada     │ │
│                          │ • Año: 2023             │ │
│                          │                         │ │
│                          │ Cantidad: [1 ▼]        │ │
│                          │                         │ │
│                          │ [Agregar al Carrito] ✓ │ │
│                          │ [❤ Favorito]           │ │
│                          └─────────────────────────┘ │
│                                                       │
│  ━━━ OPINIONES DE CLIENTES ━━━                       │
│                                                       │
│  Juan P. - ⭐⭐⭐⭐⭐ "Excelente calidad"           │
│  María G. - ⭐⭐⭐⭐ "Entrega rápida"               │
│  Carlos L. - ⭐⭐⭐⭐⭐ "Totalmente recomendado"    │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### D. PANTALLA DE CARRITO
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]        🔍 Buscar...    👤 | 🛒 | ☰  │
├──────────────────────────────────────────────────────┤
│ Mi Carrito (3 artículos)                             │
├──────────────────────────────────────────────────────┤
│                                                       │
│ ┌──────────────────────────────────────────────────┐ │
│ │ Producto           Cant  Precio Unit  Subtotal  │ │
│ ├──────────────────────────────────────────────────┤ │
│ │ Ironman (Marvel)    1      $49.99     $49.99    │ │
│ │                                      [✎] [✕]    │ │
│ │                                                  │ │
│ │ Batman (DC)         2      $34.99     $69.98    │ │
│ │                                      [✎] [✕]    │ │
│ │                                                  │ │
│ │ Pikachu (Pokémon)   1      $29.99     $29.99    │ │
│ │                                      [✎] [✕]    │ │
│ └──────────────────────────────────────────────────┘ │
│                                                       │
│  ━━━ RESUMEN ━━━                                     │
│  Subtotal:                              $149.96     │
│  Envío:                                  $9.99      │
│  Impuesto:                              $12.75      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       │
│  TOTAL:                                $172.70     │
│                                                       │
│  [Seguir Comprando]  [Proceder al Pago]            │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### E. PANTALLA DE LOGIN CON FACE ID
```
┌──────────────────────────────────────────────────────┐
│              FUNKOMON - INICIAR SESIÓN              │
├──────────────────────────────────────────────────────┤
│                                                       │
│                    [FunkoMon Logo]                    │
│                                                       │
│  ┌─ Opción 1: Login Tradicional ──────────────────┐ │
│  │                                                 │ │
│  │ Email/Usuario: [_________________________]      │ │
│  │                                                 │ │
│  │ Contraseña:    [_________________________]  👁 │ │
│  │                                                 │ │
│  │ [ ] Recordarme    [¿Olviste tu contraseña?]   │ │
│  │                                                 │ │
│  │           [Iniciar Sesión]                      │ │
│  └─────────────────────────────────────────────────┘ │
│                                                       │
│                         ─ O ─                         │
│                                                       │
│  ┌─ Opción 2: Login Biométrico (Face ID) ────────┐ │
│  │                                                 │ │
│  │  ┌────────────────────────────────────────┐   │ │
│  │  │                                        │   │ │
│  │  │      📹 [Video Stream]                 │   │ │
│  │  │                                        │   │ │
│  │  │    Posiciona tu rostro aquí            │   │ │
│  │  │                                        │   │ │
│  │  └────────────────────────────────────────┘   │ │
│  │                                                 │ │
│  │  Usuario: [________________________]            │ │
│  │                                                 │ │
│  │          [Capturar Rostro]  🎥                │ │
│  │          [Descargar Imagen]  📥                │ │
│  │                                                 │ │
│  │  Status: [ Esperando captura... ]              │ │
│  └─────────────────────────────────────────────────┘ │
│                                                       │
│  ¿No tienes cuenta? [Registrarse]                   │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### F. PANTALLA DE CHECKOUT
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]   Paso 2 de 3: CHECKOUT             │
├──────────────────────────────────────────────────────┤
│                                                       │
│  [1.Carrito ✓]  [2.Envío ▸]  [3.Pago]              │
│                                                       │
│ ┌─ Dirección de Envío ──────────────────────────┐  │
│ │ [✓] Usar dirección registrada                  │  │
│ │     Juan Pérez                                 │  │
│ │     Calle Principal 123, Apartamento 4B        │  │
│ │     Ciudad, Estado 12345                       │  │
│ │                                                 │  │
│ │ [ ] Usar otra dirección                        │  │
│ │     [Campos de entrada]                        │  │
│ └─────────────────────────────────────────────────┘  │
│                                                       │
│ ┌─ Método de Envío ────────────────────────────┐   │
│ │ [✓] Estándar (5-7 días)      $9.99           │   │
│ │ [ ] Express (2-3 días)       $24.99          │   │
│ │ [ ] Priority (24h)           $49.99          │   │
│ └─────────────────────────────────────────────────┘  │
│                                                       │
│ ┌─ Método de Pago ─────────────────────────────┐   │
│ │ [✓] Tarjeta de Crédito                        │   │
│ │ [ ] Transferencia Bancaria                    │   │
│ │ [ ] PayPal                                    │   │
│ │ [ ] Billetera Digital                         │   │
│ └─────────────────────────────────────────────────┘  │
│                                                       │
│ ┌─ Resumen ─────────────────────────────────────┐  │
│ │ Subtotal:          $149.96                    │  │
│ │ Envío:              $9.99                     │  │
│ │ Impuesto:          $12.75                     │  │
│ │ ─────────────────────────────                 │  │
│ │ TOTAL:            $172.70                     │  │
│ └─────────────────────────────────────────────────┘  │
│                                                       │
│  [◄ Atrás]                    [Continuar Pago ►]   │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### G. PANTALLA DE PERFIL DE USUARIO
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]        🔍 Buscar...    👤 ▼ | 🛒 | ☰ │
├──────────────────────────────────────────────────────┤
│ Mi Perfil                                            │
├──────────────────────────────────────────────────────┤
│                                                       │
│  ┌───────────────────────────────────────────────┐  │
│  │  👤  [Avatar]                                 │  │
│  │      Juan Pérez García                        │  │
│  │      juan.perez@email.com                     │  │
│  │      Miembro desde: 15 de Mayo, 2024          │  │
│  │                                               │  │
│  │      [ Editar Perfil ]                        │  │
│  └───────────────────────────────────────────────┘  │
│                                                       │
│  ━━━ INFORMACIÓN PERSONAL ━━━                        │
│  Nombre: Juan Pérez García                           │
│  Email: juan.perez@email.com                         │
│  Teléfono: +34 612 345 678                           │
│  Dirección: Calle Principal 123, Ciudad             │
│                                                       │
│  [ Editar ]  [ Cambiar Contraseña ]                 │
│                                                       │
│  ━━━ DATOS BIOMÉTRICOS (FACE ID) ━━━                │
│  Estado: ✓ Configurado (Última actualización: hoy)  │
│  [ Actualizar Biometría ]  [ Eliminar ]             │
│                                                       │
│  ━━━ PREFERENCIAS ━━━                                │
│  [ ] Notificaciones por email                       │
│  [✓] Notificaciones por SMS                         │
│  [✓] Newsletter semanal                             │
│                                                       │
│  [ Guardar Cambios ]                                │
│                                                       │
│  ━━━ ACCIONES ━━━                                    │
│  [ Mis Pedidos ]  [ Descargar Datos ]  [ Cerrar Sesión ] │
│                                                       │
└──────────────────────────────────────────────────────┘
```

### H. PANTALLA DE CONFIGURACIÓN BIOMÉTRICA
```
┌──────────────────────────────────────────────────────┐
│ LOGO [FunkoMon]        🔍 Buscar...    👤 | 🛒 | ☰  │
├──────────────────────────────────────────────────────┤
│ [◄ Volver a Perfil]  CONFIGURAR FACE ID             │
├──────────────────────────────────────────────────────┤
│                                                       │
│  Status Actual: ✓ CONFIGURADO (Mayo 15, 2024)       │
│                                                       │
│  ┌─ Instrucciones ───────────────────────────────┐  │
│  │ 1. Busca una zona bien iluminada              │  │
│  │ 2. Colócate frente a la cámara                │  │
│  │ 3. Abre los ojos completamente                │  │
│  │ 4. Mantente quieto durante la captura         │  │
│  │ 5. Se tomarán 3 fotos de referencia           │  │
│  └───────────────────────────────────────────────┘  │
│                                                       │
│  ┌────────────────────────────────────────┐         │
│  │                                        │         │
│  │      📹 [Video Stream en Vivo]         │         │
│  │                                        │         │
│  │      Espacio para captura...           │         │
│  │                                        │         │
│  └────────────────────────────────────────┘         │
│                                                       │
│  🟢 Cámara Detectada: Webcam 1 (HD)                 │
│                                                       │
│  Progreso: [████████░░] 80%                          │
│                                                       │
│  [ Iniciar Captura ]  [ Cancelar ]                  │
│                                                       │
│  ━━━ HISTORIAL DE CAPTURAS ━━━                       │
│  ✓ Captura 1: Exitosa (Mayo 15, 2024 14:30)        │
│  ✓ Captura 2: Exitosa (Mayo 15, 2024 14:32)        │
│  ✓ Captura 3: Exitosa (Mayo 15, 2024 14:35)        │
│                                                       │
│  Siguiente captura recomendada: Junio 15, 2025      │
│                                                       │
└──────────────────────────────────────────────────────┘
```

---

## 🔄 3. FLUJO DE USUARIO

### A. FLUJO DE COMPRA (Autenticado)

```
START
  │
  ├─→ [Inicio] Usuario navega catálogo
  │    │
  │    ├─→ [Producto Detail] Selecciona producto
  │    │    │
  │    │    └─→ [Carrito] ✓ Agrega al carrito
  │         │
  │         └─→ ¿Más compras?
  │            ├─ SÍ → [Catálogo] (vuelve al paso anterior)
  │            │
  │            └─ NO → [Carrito] Ver resumen
  │                 │
  │                 ├─→ [Editar Carrito] ¿Cambios?
  │                 │    ├─ SÍ (editar qty/eliminar)
  │                 │    │
  │                 │    └─ NO → Continuar
  │                 │
  │                 └─→ [Checkout - Paso 1]
  │                      │
  │                      ├─→ [Checkout - Paso 2] Seleccionar envío
  │                      │
  │                      ├─→ [Checkout - Paso 3] Datos de pago
  │                      │
  │                      └─→ [Procesar Pago]
  │                           ├─ ÉXITO ✓ → [Confirmación Pedido]
  │                           │             │
  │                           │             └─→ [Descargar Comprobante]
  │                           │
  │                           └─ ERROR ✕ → [Error] Reintentar
  │
  END
```

### B. FLUJO DE AUTENTICACIÓN (Login)

```
START
  │
  ├─→ [Login] Usuario elige método
  │    │
  │    ├─ MÉTODO 1: Tradicional (Email + Contraseña)
  │    │   │
  │    │   ├─→ Ingresa email/usuario y contraseña
  │    │   │
  │    │   ├─→ [Backend] Valida credenciales
  │    │   │    ├─ VÁLIDO ✓ → Retorna TOKEN
  │    │   │    │
  │    │   │    └─ INVÁLIDO ✕ → Mostrar error
  │    │   │
  │    │   └─→ ¿Crear sesión?
  │    │
  │    └─ MÉTODO 2: Biométrico (Face ID)
  │        │
  │        ├─→ Ingresa usuario
  │        │
  │        ├─→ Habilita cámara (getUserMedia)
  │        │
  │        ├─→ Usuario posiciona rostro
  │        │
  │        ├─→ [Capturar] Fotografía del usuario
  │        │
  │        ├─→ [Backend] face_recognition encoding
  │        │    ├─ MATCH ✓ → Retorna TOKEN
  │        │    │             (dentro de tolerancia)
  │        │    │
  │        │    └─ NO MATCH ✕ → Mostrar error
  │        │                    ¿Reintentar?
  │        │
  │        └─→ ¿Crear sesión?
  │
  ├─ ÉXITO ✓ → Guardar TOKEN (localStorage/sessionStorage)
  │            Redirigir a [Inicio] Autenticado
  │
  └─ ERROR ✕ → Mostrar mensaje
              ¿Reintentar?
```

### C. FLUJO DE REGISTRO + CONFIGURACIÓN BIOMÉTRICA

```
START
  │
  ├─→ [Registro] Formulario de datos
  │    │
  │    ├─→ Ingresa nombre, email, contraseña
  │    │
  │    ├─→ Confirma contraseña
  │    │
  │    ├─→ [Backend] Valida datos
  │    │    ├─ VÁLIDO ✓ → Crea usuario
  │    │    │
  │    │    └─ INVÁLIDO ✕ → Mostrar errores
  │    │
  │    └─→ ¿Continuar con Face ID?
  │
  ├─→ [Configurar Biometría]
  │    │
  │    ├─→ Permiso de cámara (getUserMedia)
  │    │    └─ DENEGADO ✕ → Saltar paso
  │    │
  │    ├─→ Posiciona rostro en área de captura
  │    │
  │    ├─→ [Capturar Rostro] × 3 tomas
  │    │    │
  │    │    ├─→ CAPTURA 1 ✓
  │    │    │   └─→ [Backend] Encoding facial
  │    │    │
  │    │    ├─→ CAPTURA 2 ✓
  │    │    │   └─→ [Backend] Encoding facial
  │    │    │
  │    │    └─→ CAPTURA 3 ✓
  │    │        └─→ [Backend] Encoding facial + Promediar
  │    │
  │    ├─→ ¿Configuración completada?
  │    │    ├─ SÍ ✓ → Vector almacenado
  │    │    │
  │    │    └─ NO ✕ → Reintentar o Saltar
  │    │
  │    └─→ [Confirmación Registro]
  │
  ├─ ÉXITO ✓ → Redirigir a [Login]
  │
  └─ ERROR ✕ → Mostrar mensaje
```

### D. FLUJO DE NAVEGACIÓN GENERAL

```
┌─────────────────────────────────────┐
│      ESTRUCTURA GENERAL SITIO       │
└─────────────────────────────────────┘

┌─ HEADER (Presente en todas) ──────────────────┐
│ [Logo]  🔍Buscar  👤Perfil | 🛒Carrito | ☰Menu│
└───────────────────────────────────────────────┘

┌─ USUARIOS NO AUTENTICADOS ─────────────────┐
│                                             │
│ / [Inicio]                                  │
│ │ └─ /productos [Catálogo Completo]        │
│ │   │ └─ /productos/:id [Detalle]          │
│ │                                           │
│ └─ /login [Formulario Login]                │
│   │ ├─ Tradicional (email + pwd)            │
│   │ └─ Biométrico (Face ID)                 │
│                                             │
│ └─ /registro [Formulario Registro]          │
│    └─ Captura biométrica (opcional)         │
│                                             │
└─────────────────────────────────────────────┘

┌─ USUARIOS AUTENTICADOS ────────────────────┐
│                                             │
│ / [Inicio]                                  │
│ │ └─ /productos [Catálogo]                 │
│ │   └─ /productos/:id [Detalle + Carrito]  │
│ │                                           │
│ ├─ /carrito [Ver Carrito]                   │
│ │ └─ /checkout [Procesar Pedido]           │
│ │   └─ /confirmacion/:id [Recibo]          │
│ │                                           │
│ ├─ /perfil [Mi Perfil]                      │
│ │ ├─ Editar datos                           │
│ │ ├─ Cambiar contraseña                     │
│ │ ├─ /perfil/biometria [Configurar Face]   │
│ │ └─ /mis-pedidos [Historial]              │
│ │                                           │
│ └─ Cerrar sesión → /login                   │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 🛠️ 4. ESPECIFICACIONES TÉCNICAS POR PANTALLA

### Pantalla: LOGIN CON FACE ID

**Tecnologías Frontend:**
- HTML5 + CSS3 + JavaScript Vainilla (o Framework React/Vue)
- `MediaDevices.getUserMedia()` para acceso a cámara
- `fetch()` o `axios` para peticiones HTTP

**Flujo de Captura Biométrica:**
1. Usuario permite acceso a cámara (permisos del navegador)
2. Se carga video stream en elemento `<video>`
3. Usuario posiciona rostro en área de detección
4. Click en botón "Capturar" → Se captura frame de canvas
5. Frame se convierte a Blob/File
6. Se envía con `FormData` al endpoint `/api/login-biometrico/`
   ```
   POST /api/login-biometrico/
   Content-Type: multipart/form-data
   
   username: "juan.perez"
   imagen: <binary file>
   ```
7. Backend retorna `{ token: "abc123...", usuario: {...} }`
8. Token se almacena en `localStorage`

**Errores Comunes:**
- Permisos denegados → Mostrar instrucciones claras
- Imagen borrosa → Pedir mejor iluminación
- Rostro no detectado → Backend retorna error 400
- Match fallido → Mostrar "Rostro no reconocido"

---

### Pantalla: DETALLE DE PRODUCTO

**Componentes:**
- Galería de imágenes con zoom
- Información: precio, stock, rating
- Botón "Agregar al Carrito"
- Selector de cantidad
- Sección de opiniones/reviews
- Productos relacionados

**Peticiones API:**
```
GET /api/productos/:id/
GET /api/productos/:id/reviews/
GET /api/productos/?categoria=X&limit=4  # Relacionados
```

---

### Pantalla: CARRITO

**Funcionalidades:**
- Listar items con cantidad, precio unit, subtotal
- Editar cantidad de cada item (incrementar/decrementar)
- Eliminar items
- Calcular automáticamente totales (subtotal, impuestos, envío)
- Botones: "Seguir Comprando" y "Proceder al Pago"

**Almacenamiento:**
- Carrito temporal en `localStorage` (si no autenticado)
- Carrito en DB (si autenticado) — sincronizar con backend

**Peticiones API:**
```
GET    /api/carrito/                   # Obtener carrito
POST   /api/carrito/                   # Agregar item
PATCH  /api/carrito/items/:id/         # Editar cantidad
DELETE /api/carrito/items/:id/         # Eliminar item
POST   /api/carrito/vaciar/            # Vaciar carrito
```

---

## 📱 5. RESPONSIVE DESIGN

**Breakpoints:**
- **Mobile (XS):** < 576px
- **Tablet (SM):** 576px - 768px
- **Desktop (MD):** 768px - 992px
- **Large (LG):** > 992px

**Recomendaciones:**
- Menú hamburguesa en mobile
- Grid de 1 columna en mobile, 2 en tablet, 3+ en desktop
- Barra lateral filtros → Colapsable en mobile
- Modales para login en mobile

---

## 🎯 6. TAREAS ESPECÍFICAS PARA ESTA SEMANA

### Semana 1: Estructura Base + Autenticación

**✓ Tareas:**

1. **Setup Inicial**
   - [ ] Estructura HTML base (index.html, plantillas)
   - [ ] Sistema de enrutamiento (React Router / vanilla JS)
   - [ ] Estructura CSS (variables, clases base)
   - [ ] Gestión de estado (localStorage, Context API/Vuex)

2. **Pantalla de Login**
   - [ ] Formulario tradicional (email + pwd)
   - [ ] Integración con API `/api/token/`
   - [ ] Validación de campos
   - [ ] Manejo de errores

3. **Pantalla de Login Biométrico (Face ID)**
   - [ ] Acceso a cámara del dispositivo
   - [ ] Captura de video stream
   - [ ] Canvas para capturar frame
   - [ ] Envío de imagen al backend
   - [ ] Manejo de respuesta (token)

4. **Pantalla de Registro**
   - [ ] Formulario de datos
   - [ ] Validación cliente (email, pwd strength)
   - [ ] Captura biométrica (opcional)
   - [ ] Integración con API `/api/usuarios/`

5. **Header Navigation**
   - [ ] Logo + marca
   - [ ] Buscador (funcional o placeholder)
   - [ ] Iconos: perfil, carrito, menú
   - [ ] Responsive design

6. **Almacenamiento de Sesión**
   - [ ] Token en localStorage
   - [ ] Detección automática de autenticación
   - [ ] Redirecciones condicionales
   - [ ] Cerrar sesión

---

## 📦 7. RECURSOS Y REFERENCIAS

### APIs Backend Disponibles

```
# Autenticación
POST   /api/token/                  # Login tradicional
POST   /api/login-biometrico/       # Login Face ID
POST   /api/usuarios/               # Registrar usuario
GET    /api/perfil/                 # Obtener perfil
PATCH  /api/perfil/                 # Actualizar perfil

# Productos
GET    /api/productos/              # Listar con filtros
GET    /api/productos/:id/          # Detalle
GET    /api/categorias/             # Categorías

# Carrito
GET    /api/carrito/
POST   /api/carrito/
PATCH  /api/carrito/items/:id/
DELETE /api/carrito/items/:id/

# Pedidos
POST   /api/pedidos/                # Crear pedido
GET    /api/pedidos/                # Listar mis pedidos
GET    /api/pedidos/:id/            # Detalle pedido
```

### Librerías Recomendadas

- **HTTP:** `fetch` (nativa) o `axios`
- **Enrutamiento:** `React Router` (si React) o `vanilla router`
- **Estilos:** CSS3 (SCSS si prefieres) o Tailwind CSS
- **Componentes UI:** Bootstrap 5 o custom CSS
- **Validación:** `validator.js` o validación manual
- **Almacenamiento:** `localStorage` API (nativa)

---

## ✅ CHECKLIST DE ENTREGA (Fin de Semana)

- [ ] Todas las pantallas bocetadas implementadas
- [ ] Login tradicional funcional
- [ ] Login biométrico funcional (captura + envío)
- [ ] Registro con captura biométrica
- [ ] Header navegación completo
- [ ] Responsivo (mobile, tablet, desktop)
- [ ] Almacenamiento de sesión (localStorage)
- [ ] Redirecciones condicionales (autenticado/no autenticado)
- [ ] Manejo básico de errores
- [ ] Sin errores en consola (JavaScript)

---

**Última actualización:** Junio 2, 2026  
**Versión:** 1.0  
**Estado:** 🟢 Listo para desarrollo
