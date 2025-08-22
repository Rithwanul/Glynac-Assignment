from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello_world(request):
    """
    A simple Hello World API endpoint.
    ---
    responses:
        200:
            description: Returns a hello world message
    """
    return Response({"message": "Hello world"})

