from rest_framework import serializers
from coffee_pods import models


class CoffeePodsSerializer(serializers.ModelSerializer):
    """Serializers for coffee machines data"""
    class Meta:
        model = models.CoffeePods
        fields = ('__all__')
