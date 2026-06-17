"""Vistas del proyecto FunkoMon: home, detalle, carrito, checkout, órdenes."""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from productos.models import Producto, Categoria
from pedidos.models import Orden, DetalleOrden
from decimal import Decimal
import json

ICONOS_TIPO = {
    "electric": "⚡", "fire": "🔥", "water": "💧", "grass": "🌿",
    "psychic": "🔮", "fighting": "👊", "normal": "⭐", "bug": "🐛",
    "poison": "☠️", "rock": "🪨", "ghost": "👻", "ground": "🏜️",
    "ice": "❄️", "dragon": "🐉",
}

# Mapeo de nombres españoles a slugs para clases CSS
TIPOS_MAPEO = {
    "Eléctrico": "electric", "Fuego": "fire", "Agua": "water", "Planta": "grass",
    "Psíquico": "psychic", "Lucha": "fighting", "Normal": "normal", "Bicho": "bug",
    "Veneno": "poison", "Roca": "rock", "Fantasma": "ghost", "Tierra": "ground",
    "Hielo": "ice", "Dragón": "dragon",
}


def _producto_a_dict(p):
    """Convierte un Producto ORM a dict para el template."""
    tipo_slug = TIPOS_MAPEO.get(p.categoria.nombre, "water")  # slug para CSS
    return {
        "id": p.id,
        "nombre": p.nombre,
        "tipo": tipo_slug,  # para clase CSS (.pcard--fire, .pcard--water, etc)
        "tipo_label": p.categoria.nombre,
        "icono": ICONOS_TIPO.get(tipo_slug, "💧"),
        "imagen": p.get_imagen(),  # método que agregamos
        "imagen_url": p.imagen_url,  # URL de imagen (PokeAPI)
        "hp": p.hp,
        "ataque": p.ataque,
        "ataque_desc": p.ataque_desc,
        "ataque_dmg": p.ataque_dmg,
        "ataque2": p.ataque2,
        "ataque2_dmg": p.ataque2_dmg,
        "debilidad_icono": ICONOS_TIPO.get("fighting", "⚡"),  # simplificado
        "retirada": range(p.retirada),
        "precio": str(p.precio),
        "numero": p.numero_carta,
        "estrellas": p.estrellas,
        "flavor": p.flavor_text,
    }


def home(request):
    """Home con filtro por tipo y búsqueda."""
    # Obtener parámetros de búsqueda y filtro
    query = request.GET.get("q", "").strip()
    tipo_filtro = request.GET.get("tipo", "").strip()

    # Filtrar productos
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    if tipo_filtro:
        productos = productos.filter(categoria__nombre__iexact=tipo_filtro)

    productos = productos[:50]  # Máximo 50
    productos_dict = [_producto_a_dict(p) for p in productos]

    # Categorías con contador
    categorias = []
    for cat in Categoria.objects.all():
        categorias.append({
            "nombre": cat.nombre,
            "emoji": ICONOS_TIPO.get(cat.nombre.lower(), "⭐"),
            "color": "#3561ad",
            "count": cat.productos.count(),
        })

    return render(request, "home.html", {
        "productos": productos_dict,
        "categorias": categorias,
        "filtros": ["Todos", "Populares", "Nuevos", "En Oferta", "Exclusivos"],
        "query": query,
        "tipo_filtro": tipo_filtro,
    })


def product_detail(request, producto_id):
    """Detalle de un producto."""
    producto = get_object_or_404(Producto, id=producto_id)
    p_dict = _producto_a_dict(producto)

    # Datos adicionales
    carrito = request.session.get("carrito", {})
    cantidad_en_carrito = carrito.get(str(producto_id), 0)

    return render(request, "product_detail.html", {
        "producto": p_dict,
        "producto_obj": producto,
        "cantidad_en_carrito": cantidad_en_carrito,
    })


@require_http_methods(["POST"])
def add_to_cart(request):
    """Agrega producto al carrito (sesión)."""
    try:
        data = json.loads(request.body)
        producto_id = data.get("producto_id")
        cantidad = int(data.get("cantidad", 1))

        if not producto_id:
            return JsonResponse({"error": "producto_id requerido"}, status=400)

        # Validar que el producto existe
        producto = get_object_or_404(Producto, id=producto_id)

        # Carrito en sesión
        if "carrito" not in request.session:
            request.session["carrito"] = {}

        carrito = request.session["carrito"]
        producto_id_str = str(producto_id)

        if producto_id_str in carrito:
            carrito[producto_id_str] += cantidad
        else:
            carrito[producto_id_str] = cantidad

        request.session["carrito"] = carrito
        request.session.modified = True

        # Calcular total items
        total_items = sum(carrito.values())

        return JsonResponse({
            "success": True,
            "mensaje": f"✓ {producto.nombre} agregado al carrito",
            "total_items": total_items,
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["POST"])
def remove_from_cart(request):
    """Remueve producto del carrito."""
    try:
        data = json.loads(request.body)
        producto_id = str(data.get("producto_id"))

        carrito = request.session.get("carrito", {})

        if producto_id in carrito:
            del carrito[producto_id]
            request.session["carrito"] = carrito
            request.session.modified = True

        total_items = sum(carrito.values())

        return JsonResponse({
            "success": True,
            "total_items": total_items,
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def cart_view(request):
    """Ver carrito."""
    carrito_ids = request.session.get("carrito", {})
    carrito_items = []
    total = Decimal("0")

    for producto_id_str, cantidad in carrito_ids.items():
        try:
            producto = Producto.objects.get(id=int(producto_id_str))
            subtotal = producto.precio * cantidad
            total += subtotal
            carrito_items.append({
                "id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": ICONOS_TIPO.get(producto.categoria.nombre.lower(), "💧"),
            })
        except Producto.DoesNotExist:
            pass

    return render(request, "cart.html", {
        "items": carrito_items,
        "total": total,
        "total_items": sum(carrito_ids.values()),
    })


@login_required(login_url="/login/")
def checkout_view(request):
    """Checkout y crear orden."""
    if request.method == "GET":
        carrito_ids = request.session.get("carrito", {})
        if not carrito_ids:
            return redirect("/carrito/")

        # Armar resumen
        total = Decimal("0")
        items = []
        for producto_id_str, cantidad in carrito_ids.items():
            try:
                producto = Producto.objects.get(id=int(producto_id_str))
                subtotal = producto.precio * cantidad
                total += subtotal
                items.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})
            except Producto.DoesNotExist:
                pass

        return render(request, "checkout.html", {
            "items": items,
            "total": total,
            "usuario": request.user,
        })

    elif request.method == "POST":
        # Crear orden
        carrito_ids = request.session.get("carrito", {})
        if not carrito_ids:
            return redirect("/carrito/")

        # Calcular total
        total = Decimal("0")
        orden = Orden.objects.create(
            usuario=request.user,
            estado="pendiente",
            total=Decimal("0"),
        )

        # Agregar items
        for producto_id_str, cantidad in carrito_ids.items():
            try:
                producto = Producto.objects.get(id=int(producto_id_str))
                subtotal = producto.precio * cantidad
                total += subtotal
                DetalleOrden.objects.create(
                    orden=orden,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio,
                )
            except Producto.DoesNotExist:
                pass

        # Actualizar total
        orden.total = total
        orden.save()

        # Limpiar carrito
        request.session["carrito"] = {}
        request.session.modified = True

        return redirect(f"/mis-ordenes/?nueva={orden.id}")


@login_required(login_url="/login/")
def user_orders_view(request):
    """Ver órdenes del usuario autenticado."""
    ordenes = Orden.objects.filter(usuario=request.user).order_by("-id")

    ordenes_list = []
    for orden in ordenes:
        detalles = DetalleOrden.objects.filter(orden=orden)
        ordenes_list.append({
            "id": orden.id,
            "fecha": orden.fecha_creacion if hasattr(orden, 'fecha_creacion') else "N/A",
            "estado": orden.estado,
            "total": orden.total,
            "cantidad_items": sum(d.cantidad for d in detalles),
            "detalles": detalles,
        })

    nueva_orden_id = request.GET.get("nueva")

    return render(request, "orders.html", {
        "ordenes": ordenes_list,
        "nueva_orden_id": nueva_orden_id,
    })
