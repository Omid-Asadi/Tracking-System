# Generated by Django 4.2.5 on 2023-09-10 05:26

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_customer_address_alter_customer_phone_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="retailer",
            name="country",
            field=django_countries.fields.CountryField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
