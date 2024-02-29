# Generated by Django 4.1.7 on 2024-02-29 15:16

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
    ]
