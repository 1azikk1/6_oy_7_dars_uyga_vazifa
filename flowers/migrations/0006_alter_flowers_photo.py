# Generated by Django 5.1.3 on 2024-12-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0005_alter_flowers_options_alter_flowers_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowers',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='flowers/photos'),
        ),
    ]
