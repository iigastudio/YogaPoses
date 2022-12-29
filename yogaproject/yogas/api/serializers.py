# Import serialier from Django Rest Framework
from rest_framework.serializers import ModelSerializer

# Import yoga model
from yogas.models import Yoga

# Create serializer to convert Yoga model into JSON
class YogaSerializer(ModelSerializer):
    class Meta:
        # Define model
        model = Yoga
        # Define attributes to serialize
        fields = '__all__'
