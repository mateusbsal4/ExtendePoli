from django.db import models
from django.conf import settings


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.URLField(max_length=200, null=True)
    descricao = models.CharField(max_length=500, null=True)


    def __str__(self):
        return f'{self.name}'


class Evento(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()
    #descriçao = 

    def __str__(self):
        return f'{self.nome}'

class Membro(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length = 50)
    entrada_equipe = models.DateField()
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
