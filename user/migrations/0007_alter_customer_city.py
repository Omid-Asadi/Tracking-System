# Generated by Django 4.2.5 on 2023-09-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_delete_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="city",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
