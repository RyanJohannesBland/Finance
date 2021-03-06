# Generated by Django 4.0 on 2021-12-31 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sum',
        ),
        migrations.AddField(
            model_name='category',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default='2021-10-20'),
            preserve_default=False,
        ),
    ]
