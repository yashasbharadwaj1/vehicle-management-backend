# Generated by Django 4.1.7 on 2024-02-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0012_remove_securityguy_vendor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Vehicle',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='details',
            field=models.CharField(blank=True, default='details', max_length=200),
        ),
    ]
