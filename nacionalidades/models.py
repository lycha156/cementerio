from django.db import models

class Nacionalidad(models.Model):

    nacionalidad = models.CharField("Nacionalidad", max_length=50)

    def __str__(self):
        return self.nacionalidad
