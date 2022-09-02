from django.shortcuts import render, redirect
from .models import cliente, gravadora, musica
from .forms import ClienteForm, GravadoraForm ,MusicaForm


def primeirapag(request):
    return render(request, 'primeirapag.html')

def listar_musica(request):
    musicas = musica.objects.all()
    context = {
        'musicas': musicas
    }
    return render(request, 'musica_listar.html', context)

def cadastrar_musica(request):
    if request.method == "POST":
        form = MusicaForm(request.POST or None, request.FILES or None, instance= musica)
        if form.is_valid():
           form.save()
           return redirect('listar_musica')
           
    else:
        form = MusicaForm(instance= musica)
        return render (request, )
        
    contexto = {
        'form_musica': form
    }
    return render(request,'musica_cadastrar.html',contexto)


def atualizar_musica(request, id):
    minha_musica = musica.objects.get(id=id)
    
    if request.method == "POST":
        form = MusicaForm(request.POST, request.FILES, instance=minha_musica)
        if form.is_valid():
            form.save()
            print("salvou form")
            return redirect('listar_musica')
    else:
        form = MusicaForm(instance=minha_musica)

    context = {
        "musica": minha_musica,
        "form": form
    }
    return render(request, 'musica_editar.html', context)
        


def deletar_musica(request, id):
    minha_musica = musica.objects.get(id=id)
    minha_musica.delete()
    return redirect('listar_musica')



def listar_cliente(request):
    ClientesAtuais = cliente.objects.all()
    context = {
        'todos_clientes': ClientesAtuais
    }
    return render(request, 'primeirapag.html', context)


def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
            
    else:
        form = ClienteForm()
        
    contexto = {
        'form_cliente': form
    }
    return render(request,'cliente_cadastrar.html',contexto)


def atualizar_cliente(request, id):
    meu_cliente = cliente.objects.get(id=id)
    
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES, instance=meu_cliente)
        if form.is_valid():
            form.save()
            print("salvou form")
            return redirect('listar_cliente')
    else:
        form = ClienteForm(instance=meu_cliente)
    context = {
        "cliente": meu_cliente,
        "form": form
    }
    return render(request, 'cliente_editar.html', context)

def deletar_cliente(request, id):
    meu_cliente = cliente.objects.get(id=id)
    meu_cliente.delete()
    return redirect('listar_cliente')


def listar_gravadora(request):
    GravadorasAtuais = gravadora.objects.all()
    context = {
        'todas_gravadoras': GravadorasAtuais
    }
    return render(request, 'gravadora_listar.html', context)

def cadastrar_gravadora(request):
    form = GravadoraForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('listar_gravadora')
    else:
        form = GravadoraForm()
    contexto = {
        'form_gravadora': form
            }
    return render(request,'gravadora_cadastrar.html',contexto)

def atualizar_gravadora(request, id):
    minha_gravadora = gravadora.objects.get(id=id)
    
    if request.method == "POST":
        form = GravadoraForm(request.POST, request.FILES, instance=minha_gravadora)
        if form.is_valid():
            form.save()
            print("salvou form")
            return redirect('listar_gravadora')
    else:
        form = GravadoraForm(instance=minha_gravadora)

    context = {
        "gravadora": minha_gravadora,
        "form": form
    }
    return render(request, 'gravadora_editar.html', context)
        
def deletar_gravadora(request, id):
    minha_gravadora = cliente.objects.get(id=id)
    minha_gravadora.delete()
    return redirect('listar_gravadora')