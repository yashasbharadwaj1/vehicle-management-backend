# Generated by Django 5.0.2 on 2024-03-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='number',
            field=models.CharField(default='KAO4KD8347', max_length=30),
        ),
    ]
