# Generated by Django 4.2.5 on 2023-11-28 22:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion_app', '0004_alter_reservas_nombre_alter_reservas_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='correo',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]
