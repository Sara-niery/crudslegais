from django.db import models

class livro(models.Model):
    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=100)
    edicao = models.IntegerField('Edição')

class editora(models.Model):
    nome1 = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=20)
    endereco = models.CharField('Endereço', max_length=50)
    numero = models.IntegerField('numero')

class cliente(models.Model):
    nome2 = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF',max_length=11)
    email = models.CharField('E-mail',max_length=50)
