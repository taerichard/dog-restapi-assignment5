
from games.models import Dog
from games.models import Breed
from games.serializers import BreedSerializer, DogSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    name = 'breed-list'

    #  def get(self, request, format=None):
    #     breeds = Breed.objects.all()
    #     serializer = BreedSerializer(breeds, many=True)
    #     return Response(serializer.data)

    #  def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    
    #  def post(self, request, format=None):
    #     serializer = BreedSerializer(data=request.data)
    #     print('HIGM')
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    name = 'dog-list'

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer
  name = 'dog-detail'

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Breed.objects.all()
  serializer_class = BreedSerializer
  name = 'breed-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'breeds':reverse(BreedList.name, request=request),
            'dogs':reverse(DogList.name, request=request),
            })
