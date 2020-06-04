from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models, permissions
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication

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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a Hello Message """
        a_viewset = [
        'Salman', 'Amer', 'Mohammad', 'Naser', 'Hasem', 'Abdollah'
        ]

        return Response({'Message':'Hello from list', 'view_sets': a_viewset})

    def create(self, request):
        """Create a new Hello message """
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}, nice to meet U.'
            return Response({"Message": message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by ID"""
        return Response({"Method": 'Retrieve or GET'})

    def update(self, request, pk=None):
        """Handle updating an object by ID"""
        return Response({"Method": 'Update or PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update an object by ID"""
        return Response({'Method': 'partial update or PATCH'})

    def destroy(self, request, pk=None):
        """Deleting an object"""
        return  Response({'Method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
