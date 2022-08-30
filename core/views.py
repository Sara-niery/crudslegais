from multiprocessing import context
from django.shortcuts import render
from .models import livro
from .forms import LivroForm

def listar_livros(request):
    LivrosAtuais = livro.objects.all()
    context = {
        'todos_livros': LivrosAtuais
    }
    return render(request, 'primeirapag.html', context)

def cadastrar_livro(request):
    form = LivroForm(request.POST or None)
    contexto = {
        'form_livro': form
    }
    return render(request,'livro_cadastrar.html',contexto)