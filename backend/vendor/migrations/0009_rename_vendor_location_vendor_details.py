# Generated by Django 4.1.7 on 2024-02-29 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_alter_vendor_vendor_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='vendor_location',
            new_name='details',
        ),
    ]
