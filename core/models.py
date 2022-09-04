from django.db import models

class gravadora(models.Model):
    nome1 = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=20)
    endereco = models.CharField('Endereço', max_length=50)
    numero = models.IntegerField('numero')

class cliente(models.Model):
    nome2 = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF',max_length=11)
    email = models.CharField('E-mail',max_length=50)

class musica(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    autor = models.CharField('Autor',max_length= 100)
    album = models.CharField('Album',max_length=50)
    capa = models.ImageField('capa',upload_to='images/', null=True)