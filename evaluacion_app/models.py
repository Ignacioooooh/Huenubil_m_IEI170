from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, EmailValidator
from django.db import models

class Reservas(models.Model):
    id_reserva = models.CharField(max_length=20, unique=True) 
    nombre = models.CharField(max_length=81, validators=[MaxLengthValidator(80)])
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo = models.EmailField(validators=[EmailValidator()])
    estado_choices = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )
    estado = models.CharField(max_length=20, choices=estado_choices)
    observacion = models.TextField(blank=True, null=True)
