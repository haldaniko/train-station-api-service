# Generated by Django 5.0.7 on 2024-07-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("station_api", "0003_train_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ticket",
            options={"ordering": ["seat"]},
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("journey", "seat")},
        ),
    ]
