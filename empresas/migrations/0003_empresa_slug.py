# Generated by Django 5.1.1 on 2024-10-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_area_slug_componente_slug_equipamento_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
