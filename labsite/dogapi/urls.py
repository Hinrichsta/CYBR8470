from django.urls import path
from . import views

urlpatterns = [
    path('Dog/', views.DogList.as_view()),
    #path('Dog/<int:pk/')
    #path('Breed/'),
    #path('Breed/<int:pk/')
]