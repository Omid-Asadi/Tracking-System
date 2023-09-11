# Generated by Django 4.2.5 on 2023-09-11 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_orderdetail_order_alter_orderdetail_product"),
        ("shipment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shipment",
            name="order",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shipment",
                to="order.order",
            ),
        ),
    ]
