# Generated by Django 4.1.7 on 2024-02-29 15:16

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_user_type_of_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
    ]
