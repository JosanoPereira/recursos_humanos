from django.db import models


class Documento(models.Model):
    num_doc = models.CharField(max_length=14)

    def __str__(self):
        return self.num_doc
