from django.db import models

class Point(models.Model):
    campo_texto = models.CharField(max_length=100)
    campo_numero = models.IntegerField()
    campo_fecha = models.DateField()

    def __str__(self):
        return self.campo_texto

class Silicon(models.Model):
    campo_texto = models.CharField(max_length=100)
    campo_numero = models.IntegerField()
    campo_fecha = models.DateField()

    def __str__(self):
        return self.campo_texto