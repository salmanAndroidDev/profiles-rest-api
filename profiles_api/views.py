from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View """
    serializer_class =  serializers.HelloSerializer

    def get(self, request, format=None):
        """ return list of API View features """
        an_apiView = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped  manually to URLs',
            'Also salman barani is a good person',
            ]

        return Response({'message': 'Hello', 'api_view': an_apiView})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'Delete'})
