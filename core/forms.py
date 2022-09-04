from django import forms
from .models import cliente,gravadora, musica
from django.forms import ModelForm

class GravadoraForm(ModelForm):
    class Meta:
        model = gravadora
        fields = ['nome1', 'cnpj', 'endereco', 'numero']

class ClienteForm(ModelForm):
    class Meta:
        model = cliente
        fields = ['nome2', 'cpf', 'email']

class MusicaForm(ModelForm):
    capa = forms.FileField 
    class Meta:
       
        model = musica
        fields = ['titulo', 'autor','album', 'capa']