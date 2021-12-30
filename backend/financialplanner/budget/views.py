from rest_framework import viewsets
from rest_framework import permissions
from financialplanner.budget import serializers, models


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

