from django.urls import path
from .views import RegistroView, LoginView, RegistrarFaceIDView, LoginFaceIDView

urlpatterns = [
    path('auth/register/', RegistroView.as_view(), name='auth_register'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    
    path('auth/face-id/register/', RegistrarFaceIDView.as_view(), name='face_id_register'),
    path('auth/face-id/login/', LoginFaceIDView.as_view(), name='face_id_login'),
]