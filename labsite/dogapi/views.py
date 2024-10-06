from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from dogapi.models import *
from dogapi.serializers import *

class DogList(APIView):
    """
    List all dogs or create a new dog
    """
    def get(self, request, format=None):
        query = Dog.objects.all()
        serializer = DogSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):
    """
    Retrieve, Update, or Delete an instance of Dog Data
    """
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = DogSerializer(query)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = DogSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BreedList(APIView):
    """
    List all breeds or create a new breed
    """
    def get(self, request, format=None):
        query = Breed.objects.all()
        serializer = BreedSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BreedDetail(APIView):
    """
    Retrieve, Update, or Delete an instance of Dog Data
    """
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = BreedSerializer(query)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = BreedSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)