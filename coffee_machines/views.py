from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


from coffee_machines import models
from coffee_machines.serializers import CoffeeMachinesSerializer


class CoffeeMachineListAPIView(ListAPIView):
    """Class Responsible for Listing and filtering coffee machines"""
    queryset = models.CoffeeMachines.objects.all()
    serializer_class = CoffeeMachinesSerializer
    filter_backends = (DjangoFilterBackend,)
    # this is fields we will filter on
    filter_fields = ('machine_type', 'water_line_compatiple')
