# Generated by Django 4.0 on 2021-12-31 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_remove_category_sum_category_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='budget.subcategory'),
        ),
    ]