# Generated by Django 5.0.2 on 2024-03-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_order_date_of_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
