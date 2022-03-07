"""
Book: Building RESTful Python Web Services
"""
from rest_framework import serializers
from dogs.models import Dog
from dogs.models import Breed

class DogSerializer(serializers.HyperlinkedModelSerializer):
    # We want to display the dog's name instead of the id
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name') 
    gender = serializers.ChoiceField(choices=Dog.genderoptions)
    genderdescription = serializers.CharField(
        source='get_gender_display',
        read_only=True)
    
    class Meta:
        model = Dog
        fields = (
            'url',
            'breed',
            'name',
             'age',
            'gender',
            'color',
            'favoritefood',
            'favoritetoy',
            )

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    dogs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='dog-detail'
    )
    #size = serializers.ChoiceField(choices=Breed.SIZE_CHOICES)

    #deleted pk since we are using names 

    class Meta:
        model = Breed
        fields = (
            'url',
            'name',
            'size',
            'exerciseneeds'
            'friendliness',
            'trainability',
            'sheddingamount',
            'dogs'
            )

