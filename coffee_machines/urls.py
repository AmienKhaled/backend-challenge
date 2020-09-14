from django.urls import path
from coffee_machines import views as machines_views
from coffee_pods import views as pods_views

urlpatterns = [
    path('',
         machines_views.CoffeeMachineListAPIView.as_view(), name="machines"),

    path('machines/',
         machines_views.CoffeeMachineListAPIView.as_view(), name="machines"),

    path('pods/',
         pods_views.CoffeePodsListAPIView.as_view(), name="pods"),
]
