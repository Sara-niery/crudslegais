from django.shortcuts import render, redirect
from .models import cliente, gravadora, musica
from .forms import ClienteForm, GravadoraForm ,MusicaForm


def primeirapag(request):
    return render(request, 'primeirapag.html')

def listar_musica(request):
    musicas = musica.objects.all()
    context = {
        'todas_musicas': musicas
    }
    return render(request, 'musica_listar.html', context)

def cadastrar_musica(request):
    form = MusicaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_musica')

    contexto = {
        'form_musica': form
    }
    return render(request,'musica_cadastrar.html',contexto)

def atualizar_musica(request, id):
    minha_musica = musica.objects.get(id=id)
    
    form = MusicaForm(request.POST or None, request.FILES or None, instance = minha_musica)
    
    if form.is_valid():
        form.save()
        return redirect('listar_musica')
   
    contexto = {
        "form_musica": form
    }
    return render(request, 'musica_cadastrar.html', contexto )      

def deletar_musica(request, id):
    minha_musica = musica.objects.get(id=id)
    minha_musica.delete()
    return redirect('listar_musica')


def listar_cliente(request):
    ClientesAtuais = cliente.objects.all()
    context = {
        'todos_clientes': ClientesAtuais
    }
    return render(request, 'cliente_listar.html', context)

def cadastrar_cliente(request):
    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
            
    contexto = {
        'form_cliente': form
    }
    return render(request,'cliente_cadastrar.html',contexto)

def atualizar_cliente(request, id):
    meu_cliente = cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=meu_cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')

    context = {
        "cliente": meu_cliente, 
        "form_cliente": form
    }
    return render(request, 'cliente_editar.html', context)

def deletar_cliente(request, id):
    meu_cliente = cliente.objects.get(id=id)
    meu_cliente.delete()
    return redirect('listar_cliente')


def listar_gravadora(request):
    Gravadoras = gravadora.objects.all()
    contexto = {
        'todas_gravadoras': Gravadoras
    }
    return render(request,'gravadora_listar.html', contexto)

def cadastrar_gravadora(request):
    form = GravadoraForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_gravadoras')

    contexto = {
        'form_gravadora': form
    }
    return render(request,'gravadora_cadastrar.html',contexto)

def atualizar_gravadora(request, id):
    minha_gravadora = gravadora.objects.get(id=id)
    
    form = GravadoraForm(request.POST or None, request.FILES or None, instance=minha_gravadora)

    if form.is_valid():
        form.save()
        return redirect('listar_gravadoras')

    contexto = {
        "gravadora": minha_gravadora.id,
        "form_gravadora": form
    }
    return render(request, 'gravadoraEditar.html', contexto)
        

def atualizar_musica(request, id):
    minha_musica = musica.objects.get(id=id)
    
    form = MusicaForm(request.POST or None, request.FILES or None, instance = minha_musica)
    
    if form.is_valid():
        form.save()
        return redirect('listar_musica')
   
    contexto = {
        "form_musica": form
    }
    return render(request, 'musica_cadastrar.html', contexto )      



def deletar_gravadora(request, id):
    minha_gravadora = gravadora.objects.get(id=id)
    minha_gravadora.delete()
    return redirect('listar_gravadoras')