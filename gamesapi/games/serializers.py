"""
Book: Building RESTful Python Web Services
"""
from rest_framework import serializers
from games.models import Dog
from games.models import Breed

class DogSerializer(serializers.HyperlinkedModelSerializer):
    # We want to display the game cagory's name instead of the id
    breed = serializers.SlugRelatedField(queryset=Breed.objects.all(), slug_field='name')
    
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
    # We want to display the game cagory's name instead of the id
    # dogs = serializers.HyperlinkedRelatedField(
    # #HyperlinkedRelatedField with many and read_only equal to True because it is a one-to-many relationship and it is read-only
    #     many=True,
    #     read_only=True,
    #     view_name='dog-detail')
    dogs = DogSerializer(many=True, read_only=True)
    size = serializers.ChoiceField(choices=Breed.SIZE_CHOICES)

    class Meta:
        model = Breed
        fields = (
            'url',
            'pk',
            'name',
            'size',
            'exerciseneeds'
            'friendliness',
            'trainability',
            'sheddingamount',
            'dogs'
            )

