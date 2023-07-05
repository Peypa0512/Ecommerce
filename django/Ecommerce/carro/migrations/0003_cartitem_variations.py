# Generated by Django 4.1.4 on 2023-05-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_variation"),
        ("carro", "0002_alter_cartitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]
