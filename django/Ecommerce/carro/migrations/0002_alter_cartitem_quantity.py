# Generated by Django 4.1.4 on 2023-05-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carro", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(),
        ),
    ]
