from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

dog_list = DogViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

dog_detail = DogViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

breed_list = BreedViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

breed_detail = BreedViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('dog/', dog_list, name='DogList'),
    path('dog/<int:pk>/', dog_detail, name='DogDetail'),
    path('breed/', breed_list, name='BreedList'),
    path('breed/<int:pk>/', breed_detail, name='BreedDetail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]