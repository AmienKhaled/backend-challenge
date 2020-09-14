from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


from coffee_pods import models
from coffee_pods.serializers import CoffeePodsSerializer


class CoffeePodsListAPIView(ListAPIView):
    """Class Responsible for Listing and filtering coffee pods"""
    queryset = models.CoffeePods.objects.all()
    serializer_class = CoffeePodsSerializer
    filter_backends = (DjangoFilterBackend,)
    # this is fields we will filter on
    filter_fields = ('flavors', 'pack_size')
