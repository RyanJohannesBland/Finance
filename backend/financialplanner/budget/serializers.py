from financialplanner.budget import models
from rest_framework import serializers


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["name", "subcategory", "allowance", "balance"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ["id", "date", "category", "amount"]