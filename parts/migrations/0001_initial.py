# Generated by Django 5.0.6 on 2024-06-07 21:47

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Part",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=150)),
                ("sku", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=1024)),
                ("weight_ounces", models.IntegerField()),
                ("is_active", models.BooleanField()),
            ],
            options={
                "db_table": "part",
                "managed": True if settings.UNDER_TEST else False,
            },
        ),
    ]
