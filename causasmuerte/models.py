from django.db import models

class CausaMuerte(models.Model):

    causa = models.CharField("Causa de Muerte", max_length=50)

    def __str__(self):
        return self.causa
