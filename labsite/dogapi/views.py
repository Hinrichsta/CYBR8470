from django.shortcuts import render
from django.http import Http404
from rest_framework import status, viewsets, permissions,renderers
from rest_framework.response import Response
from rest_framework.views import APIView
from dogapi.models import *
from dogapi.serializers import *
from django.contrib.auth import authenticate

def authenticate_user(request):
    """
    Authenticates a user using HTTP Basic Authentication.

    Returns:
        user (User): The authenticated user object, or None if authentication fails.
        error_response (tuple): A tuple containing the HTTP status code and message if authentication fails.
    """
    if 'HTTP_AUTHORIZATION' in request:
        auth = request['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2 and auth[0].lower() == 'basic':
            import base64
            try:
                username, password = base64.b64decode(auth[1]).decode('utf-8').split(':')
                user = authenticate(username=username, password=password)
                if user is not None and user.is_authenticated:
                    return user, None
            except (UnicodeDecodeError, ValueError):
                pass

    # Authentication failed
    return None, (401, 'Unauthorized', {'WWW-Authenticate': 'Basic realm="DogService"'})

class DogViewSet(viewsets.ModelViewSet):
    """
    List all dogs or create a new dog
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BreedViewSet(viewsets.ModelViewSet):
    """
    List all breeds or create a new breed
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]