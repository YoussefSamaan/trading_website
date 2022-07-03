# Generated by Django 4.0.5 on 2022-06-27 21:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_remove_stock_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='shares',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]