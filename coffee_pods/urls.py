from django.urls import path
from coffee_pods import views as pods_views

urlpatterns = [
    path('pods/',
         pods_views.CoffeePodsListAPIView.as_view(), name="pods"),
]
