from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.

class AboutView(generics.GenericAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ContactView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer
