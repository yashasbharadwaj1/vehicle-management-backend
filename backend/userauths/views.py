from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics,views,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken



class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(views.APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)
