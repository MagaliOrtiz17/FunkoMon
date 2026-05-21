# 🎭 FunkoMon — Backend

> E-commerce de figuras Funko Pop con autenticación biométrica facial **(Face ID)**
> **Evaluación de Proyectos · 7° Año Programación**

---

## 📋 Índice

- [Stack tecnológico](#-stack-tecnológico)
- [Tecnologías evaluadas y rechazadas](#-tecnologías-evaluadas-y-rechazadas)
- [Arquitectura](#-arquitectura)
- [Apps de Django](#-apps-de-django)
- [Resoluciones técnicas clave](#-resoluciones-técnicas-clave)
- [Instalación](#-instalación)

---

## 🛠 Stack tecnológico

| Tecnología | Versión | Rol en el proyecto |
| :--- | :--- | :--- |
| **Python** | 3.11+ | Lenguaje principal del backend |
| **Django** | 4.2 LTS | Framework web: ORM, admin, routing, autenticación |
| **Django REST Framework** | 3.15 | Construcción de la API REST (endpoints JSON) |
| **face_recognition** | 1.3.x | Motor biométrico: encoding y comparación de rostros |
| **dlib** | 19.24.1 | Dependencia de `face_recognition`; motor de detección de puntos faciales |
| **opencv-python** | 4.x | Preprocesamiento de imágenes de cámara |
| **MySQL 8** | 8.x | Base de datos relacional (transacciones ACID) |
| **Laragon** | 6.x | Servidor de desarrollo local |

---

## ❌ Tecnologías evaluadas y rechazadas

### Framework Backend — Django vs Node.js vs PHP
Se adoptó **Django**. La integración del motor biométrico (`face_recognition`, `dlib`) es nativa en Python. Migrar a Node.js habría implicado crear microservicios separados, añadiendo complejidad innecesaria. Django además provee ORM y panel de administración listos para usar.

### Base de Datos — MySQL vs SQLite vs PostgreSQL
Se adoptó **MySQL 8**. SQLite se descartó porque no garantiza integridad en operaciones concurrentes (como confirmar una compra y descontar stock simultáneamente). PostgreSQL es robusto pero Laragon ya incluye MySQL sin requerir configuración adicional.

### Autenticación — Token DRF vs JWT
Se eligió la autenticación nativa por **Token de DRF**. JWT añadía complejidad en la gestión de refresh/access tokens innecesaria para el alcance actual del MVP.

---

## 🏗 Arquitectura

FunkoMon sigue una arquitectura **cliente-servidor desacoplada**. El backend actúa como servidor de API REST puro: recibe peticiones, gestiona la base de datos, procesa imágenes y responde exclusivamente con JSON.

```
[Cliente / Navegador]
         ↕  Peticiones JSON / FormData + Token CSRF
[Frontend — HTML/JS Vainilla o SPA]
         ↕
[Backend — Django + DRF] ↔ [Motor Biométrico: face_recognition + dlib]
         ↕  ORM / mysqlclient
[Base de Datos — MySQL (Laragon)]
```

### Flujo biométrico (Face ID)

| Paso | Descripción |
| :---: | :--- |
| 1 | El frontend captura un frame con `getUserMedia` (JS) y lo envía al endpoint mediante `FormData` |
| 2 | El endpoint de Django (configurado con `MultiPartParser`) recibe la imagen |
| 3 | `face_recognition` extrae un vector de 128 dimensiones (array NumPy) |
| 4 | El vector se serializa y se almacena en el modelo `Perfil` del usuario en MySQL |
| 5 | En el login, se comparan los vectores con un umbral de tolerancia — si coinciden, se retorna el Token de sesión |

---

## 📦 Apps de Django

| App | Responsabilidad principal | Modelos (preliminares) |
| :--- | :--- | :--- |
| `productos` | CRUD del catálogo y stock | `Funko`, `Categoria` |
| `carrito` | Gestión de compras temporales | `Carrito`, `ItemCarrito` |
| `pedidos` | Historial y confirmación final | `Pedido`, `ItemPedido` |
| `usuarios` / `profiles` | Registro, autenticación y almacenamiento del vector biométrico JSON | Extensión del modelo `User` |

---

## 🔧 Resoluciones técnicas clave

**Instalación de dlib en Windows**
`pip install dlib` falla en Windows con Python 3.11+ por incompatibilidad de compilación C++. Solución: instalar el `.whl` precompilado directamente.
```bash
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```
> Disponible en: [github.com/z-mahmud22/Dlib_Windows_Python3.x](https://github.com/z-mahmud22/Dlib_Windows_Python3.x)

**Soporte de imágenes en la API REST**
Los endpoints biométricos reciben simultáneamente strings (username) y archivos binarios (imagen). Requiere configurar los parsers en la vista:
```python
parser_classes = [MultiPartParser, FormParser]
```

**Seguridad CSRF en Fetch**
Las peticiones asíncronas desde JavaScript necesitan enviar el token CSRF de Django en el header:
```javascript
headers: { 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value }
```

---

## 🚀 Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/MagaliOrtiz17/FunkoMon
cd funkomon

# 2. Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS

# 3. Instalar dlib (ver nota arriba)
pip install \funkomon\dlib-19.24.1-cp311-cp311-win_amd64.whl

# 4. Instalar dependencias
pip install -r requerimientos.txt

# 5. Configurar variables de entorno
cp .env.example .env          # completar con tus datos de MySQL

# 6. Aplicar migraciones
python manage.py migrate

# 7. Levantar el servidor
python manage.py runserver
```

---

*FunkoMon · Semana 1 · Sebastión López*
