# Generated by Django 4.2.5 on 2023-11-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
