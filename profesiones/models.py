from django.db import models

class Profesion(models.Model):

    profesion = models.CharField("Profesion", max_length=50)

    def __str__(self):
        return self.profesion