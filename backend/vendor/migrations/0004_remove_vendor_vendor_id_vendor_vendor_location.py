# Generated by Django 4.1.7 on 2024-02-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_order_order_id_alter_product_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_id',
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
