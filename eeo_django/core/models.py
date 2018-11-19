from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    email = models.EmailField()
