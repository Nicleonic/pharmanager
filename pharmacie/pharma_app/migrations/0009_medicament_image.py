# Generated by Django 5.0.4 on 2024-05-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0008_medicament_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='medicament_images'),
        ),
    ]