from django.urls import path
from coffee_machines import views


urlpatterns = [
    # path('', include(router.urls)),
    path('machines/',
         views.CoffeeMachineListAPIView.as_view(), name="machines"),
]
