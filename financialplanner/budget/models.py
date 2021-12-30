from django.db import models


class SubCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=200)


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    allowance = models.IntegerField()
    sum = models.BooleanField()


class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # Can store values up to 1 billion.
    amount = models.DecimalField(max_digits=19, decimal_places=2)