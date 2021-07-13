from rest_framework import serializers
from .models import MoringaMerch

# A serializer is a component that converts Django models to JSON objects and vice-versa. 
class MerchSerializer(serializers.ModelSerializer):
    class Meta:#meta subsclass to show the only fields that we want to show.
        model = MoringaMerch
        fields = ('name', 'description', 'price')