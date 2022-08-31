from django.shortcuts import render, redirect
from .models import cliente, editora, livro
from .forms import ClienteForm, LivroForm, EditoraForm

def listar_livros(request):
    livros = livro.objects.all()
    context = {
        'livros': livros
    }
    return render(request, 'livros_listar.html', context)


def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
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


def atualizar_livro(request, id):
    meu_livro = livro.objects.get(id=id)
    
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=meu_livro)
        if form.is_valid():
            form.save()
            print("salvou form")
            return redirect('listar_livros')
    else:
        form = LivroForm(instance=meu_livro)

    context = {
        "livro": meu_livro,
        "form": form
    }
    return render(request, 'livro_editar.html', context)
        


def deletar_livro(request, id):
    meu_livro = livro.objects.get(id=id)
    meu_livro.delete()
    return redirect('listar_livros')


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
