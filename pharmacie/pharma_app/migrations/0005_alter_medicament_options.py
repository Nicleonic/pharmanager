# Generated by Django 5.0.4 on 2024-05-10 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_app', '0004_agent_achat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicament',
            options={'permissions': [('publish_medicament', 'Can publish a Medecine')]},
        ),
    ]