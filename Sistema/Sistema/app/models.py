from django.db import models

class Task(models.Model):
    Product = models.CharField(max_length=200, default='Sin producto')
    
    descripcion = models.TextField(default='Sin descripción')

    ESTADOS = [
        ('Sin previo', 'Sin previo'),
        ('Grabando', 'Para Grabar'),
        ('Entregar', 'Para Entregar'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Sin previo'
    )

    nombre = models.CharField(max_length=200, default='Cliente')

    fecha = models.DateField(default='2026-01-01')

    hora = models.TimeField(default='12:00')

    numero_telefono = models.CharField(max_length=20, default='0000000000')

    tipografia = models.CharField(max_length=200, default='Arial')

    def __str__(self):
        return self.Product