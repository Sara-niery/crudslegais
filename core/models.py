from django.db import models

class livro(models.Model):
    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=100)
    edicao = models.IntegerField('Edição')