from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]