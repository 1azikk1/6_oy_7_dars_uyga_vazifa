# Generated by Django 5.1.3 on 2024-12-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_flowers_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]