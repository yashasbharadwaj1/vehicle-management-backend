# Generated by Django 4.1.7 on 2024-02-29 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_product_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securityguy',
            name='vendor',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='vendor',
            new_name='vendor_id',
        ),
        migrations.DeleteModel(
            name='QAGuy',
        ),
        migrations.DeleteModel(
            name='SecurityGuy',
        ),
    ]
