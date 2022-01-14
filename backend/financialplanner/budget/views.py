from django.db import reset_queries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from financialplanner.budget import serializers, models
import decimal
from datetime import datetime


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        # Get all categories with their data.
        categories = serializers.CategorySerializer(
            models.Category.objects.all(), many=True).data
        # Harvest all transactions and calculate the spending by category.
        transactions = models.Transaction.objects.filter(
            date__month=datetime.now().month)
        category_spending = {category["name"]: 0 for category in categories}
        for transaction in transactions:
            category_spending[transaction.category.name] += transaction.amount

        for category in categories:
            category["spent"] = category_spending[category["name"]]
        return Response(data=categories)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer
    permission_classes = (IsAuthenticated,)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = models.Transaction.objects.all().order_by("date")
    serializer_class = serializers.TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        budget_category = models.Category.objects.get(name=request.data["category"])
        budget_category.balance -= decimal.Decimal(request.data["amount"])
        budget_category.save()
        return super().create(request)

    def destroy(self, request, pk=None):
        print(pk)
        transaction = models.Transaction.objects.get(id=pk)
        transaction.category.balance += decimal.Decimal(transaction.amount)
        transaction.category.save()
        transaction.delete()
        return Response()