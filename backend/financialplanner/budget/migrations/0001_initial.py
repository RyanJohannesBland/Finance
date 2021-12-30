# Generated by Django 4.0 on 2021-12-30 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('allowance', models.IntegerField()),
                ('sum', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget.category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budget.subcategory'),
        ),
    ]