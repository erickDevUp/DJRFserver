from django.db import models
import datetime

class Entry(models.Model):
    ENTRY_STATUS_CHOICES = [
        ('Bien', 'Bien'),
        ('Regular', 'Regular'),
        ('Mal', 'Mal'),
    ]

    ENTRY_STATE_CHOICES = [
        ('Tecnológico', 'Tecnológico'),
        ('Mobiliario', 'Mobiliario'),
        ('Útil', 'Útil'),
    ]

    cant = models.PositiveIntegerField()
    description = models.TextField()
    createdAt = models.DateTimeField(default=datetime.datetime.now)  # Asumiendo que createAt es un timestamp Unix
    status = models.CharField(max_length=20, choices=ENTRY_STATUS_CHOICES, default='Bien')
    state = models.CharField(max_length=30, choices=ENTRY_STATE_CHOICES)

