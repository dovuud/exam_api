from django.contrib.auth.views import LoginView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('turpaket/',TurPaketList.as_view(),name='turpaket_list'),
    path('turpaket/<int:pk>',TurPaketDetail.as_view(),name='turpaket_detail'),
]