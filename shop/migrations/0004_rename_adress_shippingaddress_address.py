# Generated by Django 4.2.7 on 2023-12-09 12:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_rename_shippingadress_shippingaddress"),
    ]

    operations = [
        migrations.RenameField(
            model_name="shippingaddress",
            old_name="adress",
            new_name="address",
        ),
    ]
