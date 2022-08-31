from multiprocessing import context
from django.shortcuts import render, redirect
from .models import cliente, editora, livro
from .forms import ClienteForm, LivroForm, EditoraForm

def listar_livros(request):
    LivrosAtuais = livro.objects.all()
    context = {
        'todos_livros': LivrosAtuais
    }
    return render(request, 'primeirapag.html', context)

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_livros')
            except:
                pass
    else:
        form = LivroForm()
        
    contexto = {
        'form_livro': form
    }
    return render(request,'livro_cadastrar.html',contexto)

def listar_cliente(request):
    ClientesAtuais = cliente.objects.all()
    context = {
        'todos_clientes': ClientesAtuais
    }
    return render(request, 'primeirapag.html', context)

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_livros')
            except:
                pass
    else:
        form = ClienteForm()
        
    contexto = {
        'form_cliente': formC
    }
    return render(request,'livro_cadastrar.html',contexto)

def listar_editora(request):
    EditorasAtuais = editora.objects.all()
    context = {
        'todas_editoras': EditorasAtuais
    }
    return render(request, 'primeirapag.html', context)

def cadastrar_editora(request):
    formE = LivroForm(request.POST or None)
    contexto = {
        'form_editoras': formE
            }
    return render(request,'livro_cadastrar.html',contexto)
