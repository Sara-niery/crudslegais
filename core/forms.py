from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import cliente, editora, livro

class LivroForm(ModelForm):
    class Meta:
        model = livro
        fields = ['titulo', 'autor', 'edicao']

class EditoraForm(ModelForm):
    class Meta:
        model = editora
        fields = ['nome1', 'cnpj', 'endereco', 'numero']

class ClienteForm(ModelForm):
    class Meta:
        model = cliente
        fields = ['nome2', 'cpf', 'email']