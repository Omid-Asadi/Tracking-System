# Generated by Django 4.2.5 on 2023-09-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_orderdetail_order_alter_orderdetail_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="quantity",
            field=models.IntegerField(default=1, verbose_name="Quantity"),
        ),
    ]
