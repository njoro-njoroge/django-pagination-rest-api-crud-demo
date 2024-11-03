from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializer import FruitSerializers
from .models import Fruit


@api_view(["POST"])
def create_fruit(request):
    serializer = FruitSerializers(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_fruits(request):
    fruits = Fruit.objects.all()

    if not fruits.exists():  # Check if queryset is empty
        return Response({"message": "No fruit available"}, status=status.HTTP_404_NOT_FOUND)

    # Set up pagination
    paginator = PageNumberPagination()
    paginator.page_size = 5  # You can set a custom page size here

    # Apply pagination to the queryset
    paginated_fruits = paginator.paginate_queryset(fruits, request)

    # Serialize the paginated queryset and pass the request context
    serializer = FruitSerializers(paginated_fruits, many=True, context={'request': request})

    return paginator.get_paginated_response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def fruit_details(request, pk):
    try:
        fruit = Fruit.objects.get(pk=pk)
    except Fruit.DoesNotExist:
        return Response({"message": "Fruit not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FruitSerializers(fruit, context={'request': request})
        return Response({"results": serializer.data})

    elif request.method == "PUT":
        serializer = FruitSerializers(fruit, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update successful", "results": serializer.data})

        return Response(
            {"message": "Update failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        fruit.delete()
        return Response({"message": "Fruit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
