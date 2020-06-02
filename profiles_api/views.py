from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View """

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
