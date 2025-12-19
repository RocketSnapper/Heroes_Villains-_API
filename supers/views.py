from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer


@api_view(['GET', 'POST'])
def supers(request):
    
    if request.method == 'GET':
        super_type_param = request.query_params.get('super_type')
        if super_type_param == 'Hero':
            supers= Super.objects.filter(super_type=1)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        elif super_type_param == 'Villain':     
            supers= Super.objects.filter(super_type=2)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        elif super_type_param == '':
            heroes = Super.objects.filter(super_type=1)
            villains = Super.objects.filter(super_type=2)
            hero_serializer = SuperSerializer(heroes, many=True)
            villain_serializer = SuperSerializer(villains, many=True)
            custom_response_dictionary = {"Heroes": [hero_serializer.data], "Villains": [villain_serializer.data]}
            return Response(custom_response_dictionary)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def specific_super(request, pk):
        super = get_object_or_404(Super, pk=pk)
        if request.method == 'GET':
            serializer = SuperSerializer(super)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = SuperSerializer(super, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            super.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
