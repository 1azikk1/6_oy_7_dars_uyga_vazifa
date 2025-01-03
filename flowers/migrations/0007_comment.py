# Generated by Django 5.1.3 on 2024-12-30 07:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0006_alter_flowers_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Izoh Matni')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flowers')),
            ],
            options={
                'verbose_name': 'izoh ',
                'verbose_name_plural': 'izohlar',
                'ordering': ['-created'],
            },
        ),
    ]