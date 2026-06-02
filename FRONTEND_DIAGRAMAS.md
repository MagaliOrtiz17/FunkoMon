# 🎭 FunkoMon — Diagramas de Flujo (Semana 1)

## 1. FLUJO COMPLETO DE COMPRA

```mermaid
graph TD
    A["👤 Inicio (No autenticado)"] --> B["🔍 Navegar Catálogo<br/>/productos"]
    B --> C["📦 Ver Detalle Producto<br/>/productos/:id"]
    C --> D{"¿Agregar al<br/>carrito?"}
    D -->|Sí| E["✓ Producto agregado<br/>localStorage"]
    D -->|No| B
    E --> F{"¿Más<br/>productos?"}
    F -->|Sí| B
    F -->|No| G["🛒 Ver Carrito<br/>/carrito"]
    G --> H["🔐 Ir a Checkout"]
    H --> I{"¿Autenticado?"}
    I -->|No| J["🔑 Login<br/>/login"]
    J --> K["✓ Sesión creada<br/>Token en localStorage"]
    I -->|Sí| K
    K --> L["📍 Paso 1: Confirmar items<br/>/checkout?step=1"]
    L --> M["🚚 Paso 2: Seleccionar envío<br/>/checkout?step=2"]
    M --> N["💳 Paso 3: Datos de Pago<br/>/checkout?step=3"]
    N --> O["💰 Procesar Pago"]
    O --> P{"¿Pago<br/>aprobado?"}
    P -->|Éxito| Q["✅ Confirmación<br/>/confirmacion/:pedido_id"]
    P -->|Error| R["❌ Error en pago<br/>Reintentar"]
    R --> N
    Q --> S["🏠 Volver a Inicio"]
    style A fill:#e1f5ff
    style Q fill:#c8e6c9
    style R fill:#ffcdd2
```

---

## 2. FLUJO DE AUTENTICACIÓN (LOGIN)

```mermaid
graph TD
    A["🔐 Pantalla Login<br/>/login"] --> B{"¿Método de<br/>autenticación?"}
    
    B -->|Tradicional| C["📝 Email/Usuario"]
    C --> D["🔒 Contraseña"]
    D --> E["⏳ Backend: Validar credenciales"]
    E --> F{"¿Válido?"}
    F -->|Sí ✓| G["🔑 Retorna TOKEN"]
    F -->|No ✕| H["❌ Error: Credenciales inválidas"]
    H --> I["🔄 Reintentar"]
    I --> C
    
    B -->|Biométrico| J["👤 Ingresa Usuario"]
    J --> K["📹 Solicitar permisos cámara"]
    K --> L{"¿Permisos<br/>otorgados?"}
    L -->|No| M["❌ Acceso denegado<br/>Usar método tradicional"]
    M --> C
    L -->|Sí| N["🎥 Capturar video stream"]
    N --> O["⏳ Usuario posiciona rostro"]
    O --> P["📸 Click: Capturar"]
    P --> Q["🖼️ Canvas frame → Blob"]
    Q --> R["⏳ Enviar a backend<br/>POST /api/login-biometrico/"]
    R --> S["🧠 Backend: face_recognition encoding"]
    S --> T{"¿Rostro<br/>coincide?"}
    T -->|Sí ✓| G
    T -->|No ✕| U["❌ Rostro no reconocido"]
    U --> V{"¿Reintentar?"}
    V -->|Sí| O
    V -->|No| M
    
    G --> W["💾 localStorage.setItem('token', TOKEN)"]
    W --> X["✅ Sesión creada"]
    X --> Y["📍 Redirigir a /"]
    
    style A fill:#bbdefb
    style G fill:#c8e6c9
    style H fill:#ffcdd2
    style U fill:#ffcdd2
```

---

## 3. FLUJO DE REGISTRO + BIOMETRÍA

```mermaid
graph TD
    A["📋 Formulario Registro<br/>/registro"] --> B["👤 Nombre completo"]
    B --> C["📧 Email"]
    C --> D["🔒 Contraseña"]
    D --> E["🔒 Confirmar Contraseña"]
    E --> F{"¿Contraseñas<br/>coinciden?"}
    F -->|No| G["❌ Error: Las contraseñas no coinciden"]
    G --> E
    
    F -->|Sí| H["📤 Enviar a backend<br/>POST /api/usuarios/"]
    H --> I{"¿Email ya<br/>existe?"}
    I -->|Sí| J["❌ Error: Email duplicado"]
    J --> C
    I -->|No| K["✓ Usuario creado en DB"]
    
    K --> L{"¿Configurar<br/>Face ID ahora?"}
    L -->|No| M["✅ Registro completado<br/>Ir a /login"]
    L -->|Sí| N["📹 CONFIGURAR BIOMETRÍA"]
    
    N --> O["🎯 Solicitar permisos cámara"]
    O --> P{"¿Permisos?"}
    P -->|No| M
    P -->|Sí| Q["🎥 Mostrar video stream"]
    Q --> R["⏳ Usuario posiciona rostro"]
    
    R --> S["📸 Captura 1/3"]
    S --> T["🧠 Backend: Encoding facial"]
    T --> U["✓ Vector 1 almacenado"]
    
    U --> V["📸 Captura 2/3"]
    V --> W["🧠 Backend: Encoding facial"]
    W --> X["✓ Vector 2 almacenado"]
    
    X --> Y["📸 Captura 3/3"]
    Y --> Z["🧠 Backend: Encoding facial"]
    Z --> AA["✓ Vector 3 almacenado"]
    
    AA --> AB["🧮 Backend: Promediar 3 vectores"]
    AB --> AC["💾 Vector definitivo en Perfil"]
    
    AC --> AD["✅ Biometría configurada"]
    AD --> M
    M --> AE["🔑 Redirigir a /login"]
    
    style A fill:#fff9c4
    style M fill:#c8e6c9
    style J fill:#ffcdd2
    style G fill:#ffcdd2
```

---

## 4. FLUJO DE NAVEGACIÓN SEGÚN AUTENTICACIÓN

```mermaid
graph TD
    A["🌐 Usuario visita sitio"] --> B{"¿Token en<br/>localStorage?"}
    
    B -->|No| C["❌ No autenticado"]
    C --> D["👁️ VER RUTAS"]
    D --> E["/ - Inicio"]
    E --> F["Barra lateral navega:"]
    F --> G["🔍 /productos - Catálogo"]
    F --> H["📦 /productos/:id - Detalle"]
    F --> I["🔐 /login - Iniciar Sesión"]
    F --> J["📝 /registro - Registrarse"]
    
    B -->|Sí| K["✓ Autenticado"]
    K --> L["🔏 VER RUTAS"]
    L --> M["/ - Inicio"]
    M --> N["Barra lateral navega:"]
    N --> O["🔍 /productos - Catálogo"]
    N --> P["📦 /productos/:id - Detalle"]
    N --> Q["🛒 /carrito - Mi Carrito"]
    N --> R["👤 /perfil - Mi Perfil"]
    N --> S["📋 /mis-pedidos - Historial"]
    N --> T["🔐 /perfil/biometria - Face ID"]
    N --> U["🚪 Cerrar Sesión"]
    
    U --> V["🗑️ localStorage.removeItem('token')"]
    V --> W["➡️ Redirigir a /login"]
    
    style C fill:#ffecb3
    style K fill:#c8e6c9
```

---

## 5. FLUJO DE CARRITO (Operaciones)

```mermaid
graph TD
    A["🛒 Estado Carrito"] --> B{"¿Usuario<br/>autenticado?"}
    
    B -->|No| C["💾 Carrito LOCAL<br/>localStorage"]
    C --> D["📦 JSON Array items"]
    D --> E["➕ Agregar item"]
    E --> F["✏️ Editar cantidad"]
    F --> G["❌ Eliminar item"]
    G --> H["🔄 Actualizar totales"]
    H --> I{"Usuario<br/>inicia sesión?"}
    I -->|Sí| J["☁️ Sincronizar carrito<br/>POST /api/carrito/merge/"]
    I -->|No| H
    
    B -->|Sí| K["☁️ Carrito SERVER<br/>Database"]
    K --> L["📊 ORM: CartItem"]
    L --> M["➕ Agregar item"]
    M --> N["✏️ Editar cantidad"]
    N --> O["❌ Eliminar item"]
    O --> P["🔄 Actualizar totales"]
    P --> Q["💾 Guardar en DB<br/>PATCH /api/carrito/"]
    Q --> R["⏳ Sincronizar respuesta"]
    
    J --> S["🧮 CÁLCULOS AUTOMÁTICOS"]
    Q --> S
    S --> T["Subtotal = Σ precio_unit × cantidad"]
    T --> U["Impuesto = Subtotal × % (8%)"]
    U --> V["Envío = Según método (std/expr/prio)"]
    V --> W["TOTAL = Subtotal + Impuesto + Envío"]
    W --> X["✅ Mostrar en UI"]
    
    style C fill:#fff9c4
    style K fill:#c8e6c9
    style S fill:#e1f5ff
```

---

## 6. FLUJO DE CHECKOUT (3 PASOS)

```mermaid
graph TD
    A["🛒 Carrito Completo<br/>/carrito"] --> B["➡️ Proceder Checkout"]
    B --> C["📍 PASO 1: REVISAR ITEMS"]
    C --> D["Mostrar items del carrito"]
    D --> E{"¿Cambios<br/>necesarios?"}
    E -->|Sí - Editar| F["Modificar cantidades"]
    F --> E
    E -->|No| G["✓ Confirmar items"]
    
    G --> H["📍 PASO 2: SELECCIONAR ENVÍO"]
    H --> I["Cargar dirección guardada"]
    I --> J{"¿Usar<br/>la misma?"}
    J -->|No| K["Ingresar nueva dirección"]
    K --> L["Validar dirección"]
    L --> M{"¿Válida?"}
    M -->|No| K
    M -->|Sí| N["✓ Dirección confirmada"]
    
    J -->|Sí| N
    N --> O["Seleccionar método envío"]
    O --> P["🚚 Estándar (5-7 días) - $9.99"]
    O --> Q["🚀 Express (2-3 días) - $24.99"]
    O --> R["⚡ Priority (24h) - $49.99"]
    P --> S["✓ Método seleccionado"]
    Q --> S
    R --> S
    
    S --> T["🔄 Recalcular TOTAL"]
    T --> U["PASO 3: DATOS DE PAGO"]
    
    U --> V["Seleccionar método pago"]
    V --> W["💳 Tarjeta de Crédito"]
    V --> X["🏦 Transferencia Bancaria"]
    V --> Y["📱 PayPal"]
    V --> Z["💰 Billetera Digital"]
    
    W --> AA["Ingresar datos tarjeta"]
    AA --> AB["Número, fecha exp, CVV"]
    AB --> AC["Enviar al backend (PCI DSS)"]
    AC --> AD{"¿Pago<br/>aprobado?"}
    
    X --> AE["Generar referencia transferencia"]
    AE --> AF["Mostrar instrucciones"]
    AF --> AG["Pagar en banco"]
    AG --> AD
    
    Y --> AH["Redirigir a PayPal"]
    AH --> AI["Confirmar en PayPal"]
    AI --> AD
    
    Z --> AJ["QR o enlace billetera"]
    AJ --> AK["Pagar"]
    AK --> AD
    
    AD -->|Éxito ✓| AL["✅ Pago procesado"]
    AD -->|Fallo ✕| AM["❌ Error en pago"]
    
    AM --> AN["Mostrar razón del error"]
    AN --> AO{"¿Reintentar?"}
    AO -->|Sí| U
    AO -->|No| AP["Cancelar compra"]
    AP --> AQ["Redirigir a /carrito"]
    
    AL --> AR["📝 CREAR PEDIDO"]
    AR --> AS["POST /api/pedidos/"]
    AS --> AT["Backend crea Pedido + ItemsPedido"]
    AT --> AU["Descontar stock de BD"]
    AU --> AV["✓ Pedido creado"]
    
    AV --> AW["✅ CONFIRMACIÓN"]
    AW --> AX["Mostrar número pedido"]
    AX --> AY["Mostrar resumen"]
    AY --> AZ["Enviar email confirmación"]
    AZ --> BA["Opción descargar PDF"]
    BA --> BB["Redirigir a /confirmacion/:id"]
    
    style C fill:#fff9c4
    style H fill:#f0f4c3
    style U fill:#e8f5e9
    style AL fill:#c8e6c9
    style AM fill:#ffcdd2
```

---

## 7. ESTRUCTURA COMPONENTES FRONTEND

```mermaid
graph TD
    A["App.jsx / index.html"] --> B["Router (React Router o vanilla)"]
    
    B --> C["Layouts"]
    C --> D["PublicLayout<br/>(sin navbar autenticado)"]
    C --> E["AuthLayout<br/>(con opciones de perfil)"]
    
    D --> F["Páginas Públicas"]
    F --> F1["Home.jsx"]
    F --> F2["Catalogo.jsx"]
    F --> F3["ProductoDetail.jsx"]
    F --> F4["Login.jsx"]
    F --> F5["Registro.jsx"]
    
    E --> G["Páginas Autenticadas"]
    G --> G1["Carrito.jsx"]
    G --> G2["Checkout.jsx"]
    G --> G3["Confirmacion.jsx"]
    G --> G4["Perfil.jsx"]
    G --> G5["MisPedidos.jsx"]
    G --> G6["ConfiguracionBiometria.jsx"]
    
    F1 --> H["Componentes Comunes"]
    F2 --> H
    F3 --> H
    G1 --> H
    G2 --> H
    G3 --> H
    G4 --> H
    G5 --> H
    G6 --> H
    
    H --> H1["Header.jsx"]
    H --> H2["Footer.jsx"]
    H --> H3["NavigationMenu.jsx"]
    H --> H4["LoadingSpinner.jsx"]
    H --> H5["ErrorAlert.jsx"]
    H --> H6["SuccessAlert.jsx"]
    
    F3 --> I["Componentes Específicos"]
    G1 --> I
    G2 --> I
    G4 --> I
    G6 --> I
    
    I --> I1["ProductCard.jsx"]
    I --> I2["CartItem.jsx"]
    I --> I3["Form.jsx"]
    I --> I4["VideoCapture.jsx"]
    I --> I5["PriceSummary.jsx"]
    
    H --> J["Utils & Services"]
    I --> J
    
    J --> J1["api.js - Fetch wrapper"]
    J --> J2["auth.js - Token management"]
    J --> J3["validators.js - Form validation"]
    J --> J4["biometria.js - Face ID functions"]
    J --> J5["localStorage.js - Storage utils"]
    
    style A fill:#e3f2fd
    style B fill:#e3f2fd
    style H fill:#f5f5f5
    style J fill:#f5f5f5
```

---

## 8. CICLO DE VIDA: LOGIN BIOMÉTRICO

```mermaid
sequenceDiagram
    participant User as 👤 Usuario
    participant Browser as 🌐 Navegador<br/>(JavaScript)
    participant Backend as 🔧 Backend<br/>(Django + DRF)
    participant DB as 💾 Database<br/>(MySQL)
    
    User ->> Browser: 1. Accede a /login
    Browser ->> Browser: 2. Renderizar formulario
    
    User ->> Browser: 3. Ingresa usuario
    User ->> Browser: 4. Click "Usar Face ID"
    
    Browser ->> Browser: 5. getUserMedia() solicita<br/>permisos cámara
    User ->> Browser: 6. Acepta permisos
    
    Browser ->> Browser: 7. Iniciar video stream
    Browser ->> Browser: 8. Mostrar video en pantalla
    
    User ->> Browser: 9. Posiciona rostro
    User ->> Browser: 10. Click "Capturar"
    
    Browser ->> Browser: 11. Canvas captura frame
    Browser ->> Browser: 12. Frame → Blob/File
    
    Browser ->> Backend: 13. POST /api/login-biometrico/<br/>username + imagen (FormData)
    
    Backend ->> Backend: 14. Recibir FormData<br/>(MultiPartParser)
    Backend ->> Backend: 15. Guardar archivo temporal
    
    Backend ->> Backend: 16. face_recognition.load_image_file()
    Backend ->> Backend: 17. face_recognition.face_encodings()<br/>→ Array [x128]
    
    Backend ->> DB: 18. SELECT Perfil WHERE usuario=X
    DB -->> Backend: 19. Perfil + vector_biometrico
    
    Backend ->> Backend: 20. face_recognition.compare_faces()<br/>[nuevo_encoding] vs [almacenado_encoding]
    Backend ->> Backend: 21. Calcular distancia euclidiana
    Backend ->> Backend: 22. ¿Distancia < tolerancia (0.6)?
    
    alt MATCH ✓
        Backend ->> Backend: 23. Generar Token DRF
        Backend ->> DB: 24. Registrar login en Logs
        Backend -->> Browser: 25. 200 OK<br/>{ token: "abc123...", usuario: {...} }
        
        Browser ->> Browser: 26. localStorage.setItem('token')<br/>localStorage.setItem('usuario')
        Browser ->> Browser: 27. Redirigir a /
        Browser ->> User: 28. ✅ Sesión iniciada
        
    else NO MATCH ✕
        Backend ->> DB: 24. Registrar intento fallido
        Backend -->> Browser: 25. 401 UNAUTHORIZED<br/>{ error: "Rostro no reconocido" }
        
        Browser ->> Browser: 26. Mostrar alerta error
        Browser ->> User: 27. ❌ "Rostro no reconocido,<br/>¿Reintentar?"
        User ->> Browser: 28. Click "Reintentar" o<br/>"Usar email/pwd"
    end
```

---

## 9. MATRIZ DE RESPONSABILIDADES: FRONTEND vs BACKEND

| Tarea | Frontend | Backend | Compartido |
|-------|----------|---------|-----------|
| **Autenticación Tradicional** | Formulario, validación client | Validar credenciales, generar token | ✓ Token |
| **Autenticación Biométrica** | Captura video, canvas, envio imagen | face_recognition, encoding, comparación | ✓ Imagen |
| **Registro** | Formulario, validación client | Crear usuario, hashear pwd | ✓ Datos |
| **Captura Biométrica** | getUserMedia, canvas, upload | Encoding, almacenar vector | ✓ Vector |
| **Listado Productos** | UI grid, filtros client | Consultar DB, aplicar filtros DB | ✓ Filtros |
| **Detalle Producto** | Mostrar info, reviews | Consultar DB | ✓ API |
| **Carrito** | Mostrar items, UI edición | CRUD en DB (si autenticado) | ✓ Sincronización |
| **Checkout** | Formulario, cálculos UI | Crear pedido, descontar stock | ✓ Datos |
| **Pago** | Formulario tarjeta (opcional) | Procesar pago (gateway externo) | ✓ Seguridad |
| **Confirmación** | Mostrar comprobante | Generar PDF, enviar email | ✓ Datos |

---

## 10. CHECKLIST DE FUNCIONALIDADES (SEMANA 1)

### Pantalla: HOME
- [ ] Banner principal con CTA (Call To Action)
- [ ] Categorías destacadas (mini cards)
- [ ] Productos destacados (grid 4 productos)
- [ ] Footer con links
- [ ] Responsive mobile/tablet/desktop

### Pantalla: CATÁLOGO
- [ ] Listado paginado de productos (12 por página)
- [ ] Grid responsive (1 col mobile, 2 tablet, 3+ desktop)
- [ ] Filtros (categoría, precio, rating)
- [ ] Ordenamiento (precio, nombre, rating)
- [ ] Búsqueda en tiempo real
- [ ] Cards con imagen, precio, rating

### Pantalla: DETALLE PRODUCTO
- [ ] Galería de imágenes con miniaturas
- [ ] Información producto (precio, stock, rating)
- [ ] Descripción larga
- [ ] Selector cantidad
- [ ] Botón "Agregar al Carrito"
- [ ] Reviews/opiniones
- [ ] Productos relacionados (cross-sell)

### Pantalla: LOGIN
- [ ] Formulario email + password
- [ ] Validación campos
- [ ] "Mostrar/ocultar contraseña"
- [ ] Recordar usuario (checkbox)
- [ ] Link "¿Olvidaste tu contraseña?"
- [ ] Integración API `/api/token/`
- [ ] Manejo errores (401, 400)
- [ ] **[NEW]** Opción Face ID
  - [ ] Acceso a cámara
  - [ ] Video stream
  - [ ] Canvas captura
  - [ ] Envío imagen
  - [ ] Manejo respuesta

### Pantalla: REGISTRO
- [ ] Formulario (nombre, email, pwd)
- [ ] Validación campos
- [ ] Confirmación contraseña
- [ ] Link login
- [ ] Integración API `/api/usuarios/`
- [ ] Manejo errores
- [ ] **[NEW]** Opción captura biométrica
  - [ ] Video stream
  - [ ] 3 capturas
  - [ ] Envío a backend
  - [ ] Manejo respuesta

### Header/Navigation
- [ ] Logo
- [ ] Buscador (UI básica, sin funcionalidad aún)
- [ ] Iconos: 👤 Perfil, 🛒 Carrito, ☰ Menú
- [ ] Menú hamburguesa (mobile)
- [ ] Dropdown menú perfil (si autenticado)
- [ ] Hover effects

### Estado Sesión
- [ ] Token almacenado en localStorage
- [ ] Redirecciones condicionales
- [ ] Cierre de sesión
- [ ] Persistencia al recargar

---

**Próximas semanas:**
- Semana 2: Carrito + Checkout
- Semana 3: Pedidos + Perfil + Face ID avanzado
- Semana 4: Pulido, testing, optimización
