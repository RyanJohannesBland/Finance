# Generated by Django 4.0 on 2022-01-03 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_category_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='income',
        ),
    ]
