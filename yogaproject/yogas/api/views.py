# Import decorator for api view from DRF
from rest_framework.decorators import api_view
# Import Response from DRF
from rest_framework.response import Response
from yogas.models import Yoga
from .serializers import YogaSerializer

# Use decorator to define allowed methods
@api_view(['GET'])
# Create api to get available routes
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/yogas',
        'GET /api/yogas/:id'
    ]
    # Return dict as DRF response
    return Response(routes)


@api_view(['GET'])
def getYogas(request):
    # Queryset for all yogas
    yogas = Yoga.objects.all()
    # Serialize queryset
    serializer = YogaSerializer(yogas, many=True)
    return Response(serializer.data)


# API that accepts get requests with pk to get movie by id
@api_view(['GET'])
def getYoga(request, pk):
    # Queryset for yoga with matching id
    yoga = Yoga.objects.get(id=pk)
    # Serialize queryset
    serializer = YogaSerializer(yoga, many=False)
    return Response(serializer.data)
