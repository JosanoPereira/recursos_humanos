from django.db import models


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return self.motivo
