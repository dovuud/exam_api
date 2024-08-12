from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from .models import *
from.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TurPaketList(generics.ListCreateAPIView):
    queryset = Tur_paket.objects.all()
    serializer_class = TurPaketSerializer

class TurPaketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tur_paket.objects.all()
    serializer_class = TurPaketSerializer