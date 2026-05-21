from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import RegistroSerializer
from .utils import generar_encoding_facial, comparar_rostros
from .models import Profile

# ==========================================
# 1. AUTENTICACIÓN TRADICIONAL
# ==========================================

class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "mensaje": "Usuario y perfil creados con éxito.",
                "token": token.key,
                "user_id": user.pk,
                "username": user.username
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Por favor, ingresa usuario y contraseña."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "mensaje": "Inicio de sesión correcto."
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)


# ==========================================
# 2. AUTENTICACIÓN BIOMÉTRICA (FACE ID)
# ==========================================

class RegistrarFaceIDView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        foto = request.FILES.get('foto')
        
        if not foto:
            return Response({"error": "No se proporcionó ninguna imagen."}, status=status.HTTP_400_BAD_REQUEST)
        
        encoding_json = generar_encoding_facial(foto)
        
        if not encoding_json:
            return Response({"error": "No se detectó ningún rostro claro. Inténtalo de nuevo."}, status=status.HTTP_400_BAD_REQUEST)
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.biometria_facial = encoding_json
        profile.save()
        
        return Response({"mensaje": "¡FaceID registrado con éxito! Tu rostro ya está vinculado."}, status=status.HTTP_200_OK)


class LoginFaceIDView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        username = request.data.get('username')
        foto = request.FILES.get('foto')
        
        if not username or not foto:
            return Response({"error": "Se requiere el nombre de usuario y la captura de la cámara."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(username=username).first()
        if not user or not hasattr(user, 'profile') or not user.profile.biometria_facial:
            return Response({"error": "El usuario no existe o no tiene un FaceID registrado."}, status=status.HTTP_400_BAD_REQUEST)
        
        es_valido = comparar_rostros(user.profile.biometria_facial, foto)
        
        if es_valido:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "mensaje": f"¡Identidad biométrica confirmada! Bienvenido, {user.username}."
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Acceso denegado. El rostro no coincide con los registros."}, status=status.HTTP_401_UNAUTHORIZED)