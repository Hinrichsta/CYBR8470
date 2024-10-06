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



#class DogList(APIView):
#    """
#    List all dogs or create a new dog
#    """
#    def get(self, request, format=None):
#        query = Dog.objects.all()
#        serializer = DogSerializer(query, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    
#    def post(self, request, format=None):
#        serializer = DogSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#class DogDetail(APIView):
#    """
#    Retrieve, Update, or Delete an instance of Dog Data
#    """
#    def get_object(self, pk):
#        try:
#            return Dog.objects.get(pk=pk)
#        except Dog.DoesNotExist:
#            raise Http404
#        
#    def get(self, request, pk, format=None):
#        query = self.get_object(pk)
#        serializer = DogSerializer(query)
#        return Response(serializer.data)
#    
#    def put(self, request, pk, format=None):
#        query = self.get_object(pk)
#        serializer = DogSerializer(query, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    
#    def delete(self, request, pk, format=None):
#        query = self.get_object(pk)
#        query.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
#    
#class BreedList(APIView):
#    """
#    List all breeds or create a new breed
#    """
#    def get(self, request, format=None):
#        query = Breed.objects.all()
#        serializer = BreedSerializer(query, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
#    
#    def post(self, request, format=None):
#        serializer = BreedSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#class BreedDetail(APIView):
#    """
#    Retrieve, Update, or Delete an instance of Dog Data
#    """
#    def get_object(self, pk):
#        try:
#            return Breed.objects.get(pk=pk)
#        except Breed.DoesNotExist:
#            raise Http404
#        
#    def get(self, request, pk, format=None):
#        query = self.get_object(pk)
#        serializer = BreedSerializer(query)
#        return Response(serializer.data)
#    
#    def put(self, request, pk, format=None):
#        query = self.get_object(pk)
#        serializer = BreedSerializer(query, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#    
#    def delete(self, request, pk, format=None):
#        query = self.get_object(pk)
#        query.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)