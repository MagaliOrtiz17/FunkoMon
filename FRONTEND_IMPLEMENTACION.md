# 🎭 FunkoMon — Guía de Implementación Frontend (Semana 1)

## 📁 ESTRUCTURA DE CARPETAS RECOMENDADA

```
frontend/
├── index.html                  # Entrada principal HTML
├── css/
│   ├── style.css              # Estilos globales
│   ├── variables.css          # Variables CSS (colores, espacios)
│   ├── responsive.css         # Media queries
│   └── components/
│       ├── header.css
│       ├── buttons.css
│       ├── forms.css
│       ├── cards.css
│       └── modals.css
├── js/
│   ├── main.js                # Punto de entrada
│   ├── router.js              # Enrutamiento (si vanilla JS)
│   ├── store.js               # Estado global (localStorage wrapper)
│   ├── api.js                 # Cliente HTTP (fetch wrapper)
│   ├── auth.js                # Gestión autenticación
│   ├── biometria.js           # Funciones Face ID
│   ├── validators.js          # Validación de formularios
│   ├── utils.js               # Funciones auxiliares
│   └── components/
│       ├── header.js
│       ├── footer.js
│       ├── navigation.js
│       ├── productCard.js
│       ├── cartItem.js
│       ├── videoCapture.js
│       └── forms.js
├── pages/
│   ├── home.html
│   ├── catalogo.html
│   ├── producto.html
│   ├── carrito.html
│   ├── checkout.html
│   ├── confirmacion.html
│   ├── login.html
│   ├── registro.html
│   ├── perfil.html
│   ├── misPedidos.html
│   └── biometria.html
├── images/
│   ├── logo.png
│   ├── placeholders/
│   └── icons/
└── data/
    └── mock.js               # Datos mock para testing
```

---

## 🎨 PALETA DE COLORES

```css
:root {
    /* Primarios */
    --color-primary: #6200EA;        /* Púrpura (FunkoMon branding) */
    --color-secondary: #FF6B6B;      /* Rojo (acciones) */
    --color-success: #4CAF50;        /* Verde (éxito) */
    --color-warning: #FFC107;        /* Amarillo (advertencias) */
    --color-danger: #F44336;         /* Rojo (errores) */
    
    /* Escala de grises */
    --color-dark: #212121;
    --color-light: #F5F5F5;
    --color-gray-600: #757575;
    --color-gray-300: #E0E0E0;
    
    /* Sombras */
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.16);
    --shadow-lg: 0 8px 16px rgba(0,0,0,0.20);
    
    /* Espaciado */
    --spacing-xs: 0.5rem;
    --spacing-sm: 0.75rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
    
    /* Tipografía */
    --font-main: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    --font-heading: 'Poppins', sans-serif;
}
```

---

## 🔑 ARCHIVO: auth.js (Gestión de Autenticación)

```javascript
/**
 * Gestión centralizada de autenticación y sesión
 */

const AUTH = {
    TOKEN_KEY: 'funkomon_token',
    USER_KEY: 'funkomon_user',
    
    /**
     * Guardar token y usuario en localStorage
     */
    setToken(token, user) {
        localStorage.setItem(this.TOKEN_KEY, token);
        localStorage.setItem(this.USER_KEY, JSON.stringify(user));
        return true;
    },
    
    /**
     * Obtener token actual
     */
    getToken() {
        return localStorage.getItem(this.TOKEN_KEY);
    },
    
    /**
     * Obtener datos usuario actual
     */
    getUser() {
        const user = localStorage.getItem(this.USER_KEY);
        return user ? JSON.parse(user) : null;
    },
    
    /**
     * Verificar si está autenticado
     */
    isAuthenticated() {
        return !!this.getToken();
    },
    
    /**
     * Cerrar sesión
     */
    logout() {
        localStorage.removeItem(this.TOKEN_KEY);
        localStorage.removeItem(this.USER_KEY);
        window.location.href = '/login.html';
    },
    
    /**
     * Obtener headers para peticiones autenticadas
     */
    getHeaders() {
        const token = this.getToken();
        return {
            'Content-Type': 'application/json',
            'Authorization': token ? `Token ${token}` : '',
        };
    },
    
    /**
     * Redirigir a login si no está autenticado
     */
    requireAuth() {
        if (!this.isAuthenticated()) {
            window.location.href = '/login.html';
            return false;
        }
        return true;
    }
};
```

---

## 🌐 ARCHIVO: api.js (Cliente HTTP Wrapper)

```javascript
/**
 * Cliente HTTP centralizado para todas las peticiones API
 */

const API_BASE_URL = 'http://localhost:8000/api';

class APIClient {
    constructor(baseURL = API_BASE_URL) {
        this.baseURL = baseURL;
    }
    
    /**
     * Método genérico para peticiones HTTP
     */
    async request(endpoint, method = 'GET', body = null, headers = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        const options = {
            method,
            headers: {
                ...AUTH.getHeaders(),
                ...headers,
            },
        };
        
        if (body && method !== 'GET') {
            // Si body es FormData (para archivos), no setear Content-Type
            if (body instanceof FormData) {
                options.body = body;
                delete options.headers['Content-Type'];
            } else {
                options.body = JSON.stringify(body);
            }
        }
        
        try {
            const response = await fetch(url, options);
            
            if (!response.ok) {
                if (response.status === 401) {
                    // Token expirado o inválido
                    AUTH.logout();
                    throw new Error('Sesión expirada');
                }
                throw new Error(`HTTP ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }
    
    // Métodos de conveniencia
    get(endpoint) {
        return this.request(endpoint, 'GET');
    }
    
    post(endpoint, body) {
        return this.request(endpoint, 'POST', body);
    }
    
    patch(endpoint, body) {
        return this.request(endpoint, 'PATCH', body);
    }
    
    delete(endpoint) {
        return this.request(endpoint, 'DELETE');
    }
}

const API = new APIClient();

/**
 * ENDPOINTS DISPONIBLES
 */
const Endpoints = {
    // Autenticación
    LOGIN: '/token/',
    LOGIN_BIOMETRICO: '/login-biometrico/',
    REGISTRO: '/usuarios/',
    
    // Productos
    PRODUCTOS: '/productos/',
    PRODUCTO_DETAIL: (id) => `/productos/${id}/`,
    CATEGORIAS: '/categorias/',
    
    // Carrito
    CARRITO: '/carrito/',
    CARRITO_ITEMS: '/carrito/items/',
    CARRITO_ITEM_DETAIL: (id) => `/carrito/items/${id}/`,
    
    // Pedidos
    PEDIDOS: '/pedidos/',
    PEDIDO_DETAIL: (id) => `/pedidos/${id}/`,
    
    // Perfil
    PERFIL: '/perfil/',
    PERFIL_BIOMETRIA: '/perfil/biometria/',
};
```

---

## 🎥 ARCHIVO: biometria.js (Funciones Face ID)

```javascript
/**
 * Gestión de captura biométrica (Face ID)
 */

const BIOMETRIA = {
    /**
     * Solicitar acceso a cámara
     * @returns {Promise<MediaStream>}
     */
    async requestCameraAccess() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({
                video: {
                    width: { ideal: 1280 },
                    height: { ideal: 720 },
                    facingMode: 'user'
                },
                audio: false
            });
            return stream;
        } catch (error) {
            if (error.name === 'NotAllowedError') {
                throw new Error('Permiso de cámara denegado');
            } else if (error.name === 'NotFoundError') {
                throw new Error('No se encontró cámara');
            }
            throw error;
        }
    },
    
    /**
     * Iniciar video stream en elemento video
     */
    startVideoStream(videoElement, stream) {
        videoElement.srcObject = stream;
        return new Promise((resolve) => {
            videoElement.onloadedmetadata = () => {
                videoElement.play();
                resolve();
            };
        });
    },
    
    /**
     * Detener video stream
     */
    stopVideoStream(videoElement) {
        if (videoElement.srcObject) {
            videoElement.srcObject.getTracks().forEach(track => track.stop());
        }
    },
    
    /**
     * Capturar frame del video en canvas
     */
    captureFrame(videoElement, canvasElement) {
        const ctx = canvasElement.getContext('2d');
        
        // Espejo horizontal para cámara frontal
        ctx.scale(-1, 1);
        ctx.drawImage(videoElement, -videoElement.width, 0);
        
        return canvasElement;
    },
    
    /**
     * Convertir canvas a Blob
     */
    async canvasToBlob(canvasElement) {
        return new Promise((resolve) => {
            canvasElement.toBlob((blob) => {
                resolve(blob);
            }, 'image/jpeg', 0.95);
        });
    },
    
    /**
     * Enviar imagen capturada al backend para login
     */
    async sendBiometricLogin(username, imageBlob) {
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('imagen', imageBlob, 'capture.jpg');
            
            const response = await API.request(
                Endpoints.LOGIN_BIOMETRICO,
                'POST',
                formData
            );
            
            return response;
        } catch (error) {
            throw error;
        }
    },
    
    /**
     * Enviar imagen capturada al backend para registro
     */
    async sendBiometricCapture(imageBlob, captureIndex) {
        try {
            const formData = new FormData();
            formData.append('imagen', imageBlob, `capture_${captureIndex}.jpg`);
            
            const response = await API.request(
                Endpoints.PERFIL_BIOMETRIA,
                'POST',
                formData
            );
            
            return response;
        } catch (error) {
            throw error;
        }
    }
};
```

---

## ✅ ARCHIVO: validators.js (Validación de Formularios)

```javascript
/**
 * Funciones de validación de campos
 */

const VALIDATORS = {
    /**
     * Validar email
     */
    isValidEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    },
    
    /**
     * Validar contraseña (mínimo 8 caracteres, mayúscula, número)
     */
    isValidPassword(password) {
        return password.length >= 8 && 
               /[A-Z]/.test(password) && 
               /[0-9]/.test(password);
    },
    
    /**
     * Validar campo requerido
     */
    isRequired(value) {
        return value && value.trim().length > 0;
    },
    
    /**
     * Obtener mensaje de error de contraseña débil
     */
    getPasswordStrengthError(password) {
        if (password.length < 8) {
            return 'Mínimo 8 caracteres';
        }
        if (!/[A-Z]/.test(password)) {
            return 'Debe contener al menos una mayúscula';
        }
        if (!/[0-9]/.test(password)) {
            return 'Debe contener al menos un número';
        }
        return '';
    },
    
    /**
     * Validar contraseñas coincidentes
     */
    passwordsMatch(pwd1, pwd2) {
        return pwd1 === pwd2;
    },
    
    /**
     * Validar teléfono (formato básico)
     */
    isValidPhone(phone) {
        return /^[\d\s\-\+\(\)]{10,}$/.test(phone);
    },
    
    /**
     * Validar número (entero positivo)
     */
    isValidNumber(value) {
        return !isNaN(value) && parseInt(value) > 0;
    }
};
```

---

## 📄 ARCHIVO: pages/login.html (Página Login)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FunkoMon - Iniciar Sesión</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/components/forms.css">
</head>
<body class="login-page">
    <div class="login-container">
        <div class="login-card">
            <!-- Logo -->
            <div class="logo-section">
                <h1>🎭 FunkoMon</h1>
                <p>Tu tienda de Funko Pop favorita</p>
            </div>
            
            <!-- Tabs: Tradicional vs Biométrico -->
            <div class="login-tabs">
                <button class="tab-btn active" data-tab="tradicional">
                    📝 Email/Contraseña
                </button>
                <button class="tab-btn" data-tab="biometrico">
                    👤 Face ID
                </button>
            </div>
            
            <!-- TAB 1: Login Tradicional -->
            <div class="tab-content active" id="tab-tradicional">
                <form id="loginForm" class="form">
                    <div class="form-group">
                        <label for="email">Email o Usuario</label>
                        <input 
                            type="email" 
                            id="email" 
                            name="email"
                            placeholder="tu@email.com"
                            required
                        >
                        <span class="error-message"></span>
                    </div>
                    
                    <div class="form-group">
                        <label for="password">Contraseña</label>
                        <div class="password-input">
                            <input 
                                type="password" 
                                id="password" 
                                name="password"
                                placeholder="••••••••"
                                required
                            >
                            <button type="button" class="toggle-password">👁️</button>
                        </div>
                        <span class="error-message"></span>
                    </div>
                    
                    <div class="form-group checkbox">
                        <input type="checkbox" id="remember" name="remember">
                        <label for="remember">Recordarme</label>
                    </div>
                    
                    <button type="submit" class="btn btn-primary btn-full">
                        Iniciar Sesión
                    </button>
                    
                    <a href="#" class="link">¿Olvidaste tu contraseña?</a>
                </form>
            </div>
            
            <!-- TAB 2: Login Biométrico -->
            <div class="tab-content" id="tab-biometrico">
                <form id="biometricForm" class="form">
                    <div class="form-group">
                        <label for="username-bio">Usuario</label>
                        <input 
                            type="text" 
                            id="username-bio" 
                            name="username"
                            placeholder="Tu usuario"
                            required
                        >
                        <span class="error-message"></span>
                    </div>
                    
                    <!-- Video Stream -->
                    <div class="video-capture-container">
                        <video id="videoStream" autoplay></video>
                        <canvas id="captureCanvas" style="display: none;"></canvas>
                        <div class="video-overlay">
                            <p>Posiciona tu rostro aquí</p>
                        </div>
                    </div>
                    
                    <!-- Controles -->
                    <div class="capture-controls">
                        <button type="button" id="captureBtn" class="btn btn-secondary">
                            📸 Capturar Rostro
                        </button>
                        <button type="button" id="downloadBtn" class="btn btn-outline">
                            📥 Descargar Imagen
                        </button>
                    </div>
                    
                    <!-- Status -->
                    <div id="captureStatus" class="status-message">
                        Esperando captura...
                    </div>
                    
                    <button type="submit" class="btn btn-primary btn-full" disabled>
                        Iniciar Sesión con Face ID
                    </button>
                </form>
            </div>
            
            <!-- Registro Link -->
            <div class="auth-footer">
                <p>¿No tienes cuenta? <a href="../pages/registro.html">Registrarse</a></p>
            </div>
        </div>
    </div>
    
    <!-- Alert Modales -->
    <div id="errorAlert" class="alert alert-danger" style="display: none;"></div>
    <div id="successAlert" class="alert alert-success" style="display: none;"></div>
    
    <script src="../js/auth.js"></script>
    <script src="../js/api.js"></script>
    <script src="../js/validators.js"></script>
    <script src="../js/biometria.js"></script>
    <script src="../js/pages/login.js"></script>
</body>
</html>
```

---

## 📄 ARCHIVO: js/pages/login.js (Lógica Login)

```javascript
/**
 * Lógica de la página de login
 */

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const biometricForm = document.getElementById('biometricForm');
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    let videoStream = null;
    let capturedImage = null;
    
    // ============ TABS ============
    tabBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const tabName = e.target.dataset.tab;
            
            // Actualizar tabs activos
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            
            e.target.classList.add('active');
            document.getElementById(`tab-${tabName}`).classList.add('active');
            
            // Si se abre biométrico, iniciar cámara
            if (tabName === 'biometrico') {
                initializeCamera();
            } else {
                stopCamera();
            }
        });
    });
    
    // ============ LOGIN TRADICIONAL ============
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value;
        
        // Validar email
        if (!VALIDATORS.isValidEmail(email)) {
            showError('Email inválido', 'email');
            return;
        }
        
        // Validar contraseña
        if (!VALIDATORS.isRequired(password)) {
            showError('Contraseña requerida', 'password');
            return;
        }
        
        try {
            const response = await API.post(Endpoints.LOGIN, {
                username: email,
                password: password
            });
            
            // Guardar token y usuario
            AUTH.setToken(response.token, response.user);
            
            showSuccess('¡Bienvenido de vuelta!');
            setTimeout(() => {
                window.location.href = '../pages/home.html';
            }, 1500);
            
        } catch (error) {
            showError('Credenciales inválidas');
            console.error('Login error:', error);
        }
    });
    
    // ============ LOGIN BIOMÉTRICO ============
    document.getElementById('captureBtn').addEventListener('click', async (e) => {
        e.preventDefault();
        
        try {
            const video = document.getElementById('videoStream');
            const canvas = document.getElementById('captureCanvas');
            
            // Configurar canvas
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            
            // Capturar frame
            BIOMETRIA.captureFrame(video, canvas);
            
            // Convertir a blob
            capturedImage = await BIOMETRIA.canvasToBlob(canvas);
            
            // Actualizar UI
            document.getElementById('captureBtn').textContent = '📸 ✓ Capturado';
            document.getElementById('captureBtn').disabled = true;
            document.getElementById('downloadBtn').style.display = 'inline-block';
            
            updateCaptureStatus('✅ Rostro capturado. Presiona "Iniciar Sesión"', 'success');
            
            // Habilitar botón submit
            biometricForm.querySelector('button[type="submit"]').disabled = false;
            
        } catch (error) {
            updateCaptureStatus(`❌ Error: ${error.message}`, 'error');
        }
    });
    
    // Descargar imagen capturada
    document.getElementById('downloadBtn').addEventListener('click', (e) => {
        e.preventDefault();
        
        if (!capturedImage) return;
        
        const url = URL.createObjectURL(capturedImage);
        const a = document.createElement('a');
        a.href = url;
        a.download = `face_capture_${Date.now()}.jpg`;
        a.click();
        URL.revokeObjectURL(url);
    });
    
    // Submit biométrico
    biometricForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const username = document.getElementById('username-bio').value.trim();
        
        if (!VALIDATORS.isRequired(username)) {
            showError('Usuario requerido', 'username-bio');
            return;
        }
        
        if (!capturedImage) {
            updateCaptureStatus('❌ Debes capturar un rostro primero', 'error');
            return;
        }
        
        try {
            updateCaptureStatus('⏳ Verificando rostro...', 'loading');
            
            const response = await BIOMETRIA.sendBiometricLogin(username, capturedImage);
            
            // Guardar token y usuario
            AUTH.setToken(response.token, response.user);
            
            updateCaptureStatus('✅ ¡Sesión iniciada!', 'success');
            
            setTimeout(() => {
                window.location.href = '../pages/home.html';
            }, 1500);
            
        } catch (error) {
            const message = error.message.includes('401') 
                ? '❌ Rostro no reconocido' 
                : `❌ Error: ${error.message}`;
            updateCaptureStatus(message, 'error');
        }
    });
    
    // ============ UTILIDADES ============
    
    async function initializeCamera() {
        try {
            videoStream = await BIOMETRIA.requestCameraAccess();
            const video = document.getElementById('videoStream');
            await BIOMETRIA.startVideoStream(video, videoStream);
            updateCaptureStatus('✅ Cámara lista', 'success');
        } catch (error) {
            updateCaptureStatus(`❌ ${error.message}`, 'error');
        }
    }
    
    function stopCamera() {
        if (videoStream) {
            BIOMETRIA.stopVideoStream(document.getElementById('videoStream'));
            videoStream = null;
        }
    }
    
    function updateCaptureStatus(message, type = 'info') {
        const status = document.getElementById('captureStatus');
        status.textContent = message;
        status.className = `status-message status-${type}`;
    }
    
    function showError(message, fieldName = null) {
        const errorAlert = document.getElementById('errorAlert');
        errorAlert.textContent = message;
        errorAlert.style.display = 'block';
        
        if (fieldName) {
            const input = document.querySelector(`[name="${fieldName}"]`);
            if (input) {
                input.classList.add('error');
                const errorSpan = input.parentElement.querySelector('.error-message');
                if (errorSpan) errorSpan.textContent = message;
            }
        }
        
        setTimeout(() => {
            errorAlert.style.display = 'none';
        }, 5000);
    }
    
    function showSuccess(message) {
        const successAlert = document.getElementById('successAlert');
        successAlert.textContent = message;
        successAlert.style.display = 'block';
    }
    
    // Toggle mostrar/ocultar contraseña
    document.querySelector('.toggle-password').addEventListener('click', (e) => {
        e.preventDefault();
        const input = e.target.previousElementSibling;
        input.type = input.type === 'password' ? 'text' : 'password';
    });
});
```

---

## 🚀 INSTRUCCIONES DE SETUP INICIAL

### 1. Crear estructura base

```bash
# Desde la raíz del proyecto
mkdir -p frontend/css/components
mkdir -p frontend/js/components
mkdir -p frontend/js/pages
mkdir -p frontend/pages
mkdir -p frontend/images/icons
mkdir -p frontend/data
```

### 2. Crear archivos base

```bash
cd frontend

# HTML
touch index.html
touch pages/home.html
touch pages/login.html
touch pages/registro.html
touch pages/catalogo.html
touch pages/producto.html
touch pages/carrito.html
touch pages/checkout.html
touch pages/confirmacion.html
touch pages/perfil.html
touch pages/misPedidos.html
touch pages/biometria.html

# CSS
touch css/variables.css
touch css/style.css
touch css/responsive.css
touch css/components/header.css
touch css/components/forms.css
touch css/components/cards.css
touch css/components/buttons.css

# JavaScript
touch js/main.js
touch js/api.js
touch js/auth.js
touch js/biometria.js
touch js/validators.js
touch js/router.js
touch js/store.js
```

### 3. Instalar (si usas Node + npm)

```bash
npm init -y
npm install axios express-serve-static-core
```

### 4. Server de desarrollo (opcional)

Si usas Python:
```bash
# En la raíz del proyecto
python -m http.server 3000
```

Si usas Node:
```bash
npx http-server frontend -p 3000
```

Luego accede a: `http://localhost:3000`

---

## 🧪 TESTING MANUAL - CHECKLIST

### Pantalla LOGIN

- [ ] **Formato tradicional**
  - [ ] Validar email requerido
  - [ ] Validar contraseña requerida
  - [ ] Petición POST a `/api/token/`
  - [ ] Guardar token en localStorage
  - [ ] Redirigir a home si success
  - [ ] Mostrar error si fallan credenciales

- [ ] **Formato biométrico**
  - [ ] Click en tab Face ID
  - [ ] Solicita permisos cámara ✓
  - [ ] Video stream aparece
  - [ ] Click Capturar funciona
  - [ ] Canvas captura frame
  - [ ] Botón descargar imagen descarga JPG
  - [ ] Petición POST a `/api/login-biometrico/`
  - [ ] Mostrar error si rostro no coincide
  - [ ] Mostrar success si rostro válido

### Pantalla REGISTRO

- [ ] Validar todos los campos requeridos
- [ ] Validar email único
- [ ] Validar contraseña fuerte (8+ chars, mayús, números)
- [ ] Validar contraseñas coincidentes
- [ ] Petición POST a `/api/usuarios/`
- [ ] Opción captura biométrica (3 tomas)
- [ ] Redirigir a login si success

### Header

- [ ] Logo visible y clickeable
- [ ] Buscador presente (UI placeholder)
- [ ] Icono perfil presente
- [ ] Icono carrito muestra cantidad
- [ ] Menú hamburguesa en mobile (<768px)
- [ ] Links de navegación funcionales

### Responsive

- [ ] Mobile (375px): 1 columna, todo stackeado
- [ ] Tablet (768px): 2 columnas
- [ ] Desktop (1200px): 3+ columnas

---

## 📚 REFERENCIAS Y RECURSOS

### MDN Web Docs
- `fetch` API: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- `getUserMedia`: https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
- Canvas: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API
- `FormData`: https://developer.mozilla.org/en-US/docs/Web/API/FormData

### Django REST Framework
- Autenticación Token: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
- Parsers (multipart): https://www.django-rest-framework.org/api-guide/parsers/#multipartparser

### Biometría (Backend)
- `face_recognition`: https://github.com/ageitgey/face_recognition
- `dlib`: http://dlib.net/

---

## 🐛 TROUBLESHOOTING

**❌ "Permiso de cámara denegado"**
- Usuario rechazó en primer prompt
- Solución: Cambiar permisos en navegador → Recargar
- En HTTPS, permisos más restrictivos

**❌ "Rostro no detectado" del backend**
- Imagen muy oscura/borrosa
- Rostro muy pequeño o alejado
- Solución: Mejor iluminación, acercarse más

**❌ CORS error en fetch**
- Backend no tiene CORS configurado
- Solución: Agregar a `settings.py`:
  ```python
  INSTALLED_APPS = [..., 'corsheaders']
  MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware', ...]
  CORS_ALLOWED_ORIGINS = ['http://localhost:3000']
  ```

**❌ Token no se envía en requests autenticadas**
- Header `Authorization` no incluido
- Solución: Revisar función `getHeaders()` en `auth.js`

---

**Última actualización:** Junio 2, 2026  
**Versión:** 1.0  
**Estado:** 🟢 Listo para codificar
