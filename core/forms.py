from dataclasses import fields
from django.forms import ModelForm
from .models import livro

class LivroForm(ModelForm):
    class Meta:
        model = livro
        fields = ['titulo', 'autor', 'ano']