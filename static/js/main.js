/* ============================================================
   FunkoMon · Interacciones de la interfaz
   - Navegación de sesión (token en localStorage)
   - Menú móvil
   - Efecto 3D (tilt) en las tarjetas Pokémon
   ============================================================ */
(function () {
  "use strict";

  /* ---------- Navegación de sesión ---------- */
  function renderAuth() {
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username");

    const loggedIn = `
      <span style="color:var(--color-primary);font-size:var(--fs-sm)">👤 ${username}</span>
      <button class="btn btn--sm btn--accent" data-logout>Cerrar Sesión</button>`;
    const loggedOut = `
      <a href="/login/" class="btn btn--sm btn--outline">Iniciar Sesión</a>
      <a href="/registro/" class="btn btn--sm">Registrarse</a>`;

    const html = token && username ? loggedIn : loggedOut;
    document.querySelectorAll("#nav-auth, #nav-auth-mobile").forEach((el) => {
      if (!el) return;
      el.style.display = "inline-flex";
      el.style.gap = "var(--space-2)";
      el.style.alignItems = "center";
      el.innerHTML = html;
    });

    document.querySelectorAll("[data-logout]").forEach((btn) =>
      btn.addEventListener("click", () => {
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        window.location.href = "/login/";
      })
    );
  }

  /* ---------- Menú móvil ---------- */
  function setupMobileMenu() {
    const toggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("mobile-menu");
    if (!toggle || !menu) return;
    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("is-open");
      toggle.textContent = open ? "✕" : "☰";
    });
  }

  /* ---------- Efecto 3D de las tarjetas ---------- */
  function setupCardTilt() {
    const cards = document.querySelectorAll("[data-tilt]");
    cards.forEach((card) => {
      const tilt = card.querySelector(".pcard__tilt");
      if (!tilt) return;

      card.addEventListener("mousemove", (e) => {
        const r = card.getBoundingClientRect();
        const x = e.clientX - r.left;
        const y = e.clientY - r.top;
        const rotX = (y - r.height / 2) / 8;
        const rotY = (r.width / 2 - x) / 8;
        tilt.style.transform =
          `rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.05)`;
        const shine = card.querySelector(".pcard__shine");
        if (shine) shine.style.transform = `translateX(${rotY * 8}px)`;
      });

      card.addEventListener("mouseleave", () => {
        tilt.style.transform = "rotateX(0) rotateY(0) scale(1)";
      });
    });
  }

  /* ---------- Filtros (sólo estado visual por ahora) ---------- */
  function setupFilters() {
    const filters = document.querySelectorAll(".filter");
    filters.forEach((f) =>
      f.addEventListener("click", () => {
        filters.forEach((x) => x.classList.remove("is-active"));
        f.classList.add("is-active");
      })
    );
  }

  /* ---------- Actualizar contador carrito ---------- */
  function updateCartCount() {
    const carrito = JSON.parse(localStorage.getItem("carrito") || "{}");
    const total = Object.values(carrito).reduce((a, b) => a + b, 0);
    const cartCountEl = document.getElementById("cart-count");
    if (cartCountEl) cartCountEl.textContent = total;
  }

  document.addEventListener("DOMContentLoaded", () => {
    renderAuth();
    setupMobileMenu();
    setupCardTilt();
    setupFilters();
    updateCartCount();

    // Actualizar carrito al agregar
    window.addEventListener("cartUpdated", updateCartCount);
  });
})();
