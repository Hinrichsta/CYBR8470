from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id','name','size','friendliness','trainability','shedding','exercise']

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id','name','age','breed','gender','color','favoritefood','favoritetoy']

