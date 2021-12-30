from financialplanner.budget import models
from rest_framework import serializers


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ["name"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ["name", "subcategory", "allowance", "sum"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Transaction
        fields = ["category", "amount"]