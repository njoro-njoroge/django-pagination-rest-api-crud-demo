from django.urls import path
from .views import create_fruit,get_fruits,fruit_details

urlpatterns = [
    path('fruits/', get_fruits, name='get-fruits'),
    path('fruits/create/', create_fruit, name='create-fruits'),
    path('fruits/<int:pk>/', fruit_details, name='fruit-detail'),  # Detail view
]
