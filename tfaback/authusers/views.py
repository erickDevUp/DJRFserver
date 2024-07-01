from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from.serializers import CustomUserSerializer
from.models import CustomUser
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class RegistrarUsuario(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]  # Permite el acceso sin autenticación, pero verifica el token si está presente

    serializer_class = CustomUserSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=400)
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])  # Ahora establece la contraseña
        user.save()
       
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': serializer.data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)



class IniciarSesion(APIView):
    serializer_class = CustomUserSerializer  # Define el serializador que vas a usar

    def post(self, request, format=None):  
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'user':CustomUserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    
