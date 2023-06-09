# Generated by Django 4.1.6 on 2023-02-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Celebrity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unique_no", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                ("net_worth", models.FloatField()),
                ("address", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Celebrity",
                "verbose_name_plural": "Celebrities",
            },
        ),
    ]
