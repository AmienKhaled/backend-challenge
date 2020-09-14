from rest_framework import serializers
from coffee_machines import models


class CoffeeMachinesSerializer(serializers.ModelSerializer):
    """Serializers for coffee machines data"""
    class Meta:
        model = models.CoffeeMachines
        fields = ('__all__')
