from dataclasses import fields
from pyexpat import model
from django import forms
from .models import cliente,gravadora, musica

class GravadoraForm(forms.ModelForm):
    class Meta:
        model = gravadora
        fields = ['nome1', 'cnpj', 'endereco', 'numero']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nome2', 'cpf', 'email']

class MusicaForm(forms.ModelForm):
    capa = forms.FileField(required=False)
    class Meta:
        model = musica
        fields = ['titulo', 'autor','album', 'capa']