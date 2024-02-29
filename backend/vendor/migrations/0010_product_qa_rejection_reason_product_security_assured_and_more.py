# Generated by Django 4.1.7 on 2024-02-29 17:03

import backend.storage_backends
from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_rename_vendor_location_vendor_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qa_rejection_reason',
            field=models.CharField(default='reason for qa guy to reject', max_length=400),
        ),
        migrations.AddField(
            model_name='product',
            name='security_assured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='security_rejection_reason',
            field=models.CharField(default='reason for security guy to reject', max_length=400),
        ),
        migrations.AddField(
            model_name='qaguy',
            name='qa_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
        migrations.AddField(
            model_name='securityguy',
            name='security_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(default='default.jpg', storage=backend.storage_backends.PublicMediaStorage(), upload_to='product'),
        ),
    ]
