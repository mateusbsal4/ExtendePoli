from django.db import models
from django.conf import settings
from django.urls import reverse
from django.views import generic


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.URLField(max_length=1000, null=True)
    descricao = models.CharField(max_length=500, null=True)


    def __str__(self):
        return f'{self.nome}'

class Membro(models.Model):
    equipes = models.ManyToManyField(Equipe)
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length = 50)
    entrada_equipe = models.DateField()
    def __str__(self):
        return f'{self.nome}'

class Foto(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    link = models.URLField(max_length=1000, null=True)


class Evento(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()
    descricao = models.CharField(max_length=500, null=True)

    def __str__(self):
        return f'{self.nome}'







class Interessado(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    repr_senha = models.CharField(max_length=50)
    ingresso = models.DateField()
    curso = models.CharField(max_length=50)
    def __str__(self):
        return f'"{self.nome}" - {self.email}'
