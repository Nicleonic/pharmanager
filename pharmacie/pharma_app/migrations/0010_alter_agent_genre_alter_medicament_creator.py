# Generated by Django 5.0.4 on 2024-05-14 12:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0009_medicament_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='genre',
            field=models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=10),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]