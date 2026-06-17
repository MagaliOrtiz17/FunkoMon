from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('productos.urls')), # Productos
    path('api/', include('profiles.urls')),  # Auth

    # Frontend
    path('', views.home, name='home'),
    path('producto/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('agregar-carrito/', views.add_to_cart, name='add_to_cart'),
    path('remover-carrito/', views.remove_from_cart, name='remove_from_cart'),
    path('carrito/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('mis-ordenes/', views.user_orders_view, name='orders'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('registro/', TemplateView.as_view(template_name='registro.html'), name='registro'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
