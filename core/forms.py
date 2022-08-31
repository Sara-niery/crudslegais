from dataclasses import fields
from pyexpat import model
from django import forms
from .models import cliente, editora, livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = livro
        fields = ['titulo', 'autor', 'edicao', 'capa']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = editora
        fields = ['nome1', 'cnpj', 'endereco', 'numero']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nome2', 'cpf', 'email']