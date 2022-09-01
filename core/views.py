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
        form = MusicaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_musica')
            except:
                pass
    else:
        form = MusicaForm()
        
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
        formC = ClienteForm(request.POST, request.FILES)
        if formC.is_valid():
            try:
                formC.save()
                return redirect('listar_clientes')
            except:
                pass
    else:
        formC = ClienteForm()
        
    contexto = {
        'form_cliente': formC
    }
    return render(request,'cliente_cadastrar.html',contexto)


def atualizar_cliente(request, id):
    meu_cliente = cliente.objects.get(id=id)
    
    if request.method == "POST":
        formC = ClienteForm(request.POST, request.FILES, instance=meu_cliente)
        if formC.is_valid():
            formC.save()
            print("salvou form")
            return redirect('listar_cliente')
    else:
        formC = ClienteForm(instance=meu_cliente)
    context = {
        "cliente": meu_cliente,
        "formC": formC
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
    formG = GravadoraForm(request.POST, request.FILES)
    if formG.is_valid():
        try:
            formG.save()
            return redirect('listar_gravadora')
        except:
            pass
    else:
        formG = GravadoraForm()
    contexto = {
        'form_gravadora': formG
            }
    return render(request,'gravadora_cadastrar.html',contexto)

def atualizar_gravadora(request, id):
    minha_gravadora = gravadora.objects.get(id=id)
    
    if request.method == "POST":
        formG = GravadoraForm(request.POST, request.FILES, instance=minha_gravadora)
        if formG.is_valid():
            formG.save()
            print("salvou form")
            return redirect('listar_gravadora')
    else:
        formG = GravadoraForm(instance=minha_gravadora)

    context = {
        "gravadora": minha_gravadora,
        "formG": formG
    }
    return render(request, 'gravadora_editar.html', context)
        
def deletar_gravadora(request, id):
    minha_gravadora = cliente.objects.get(id=id)
    minha_gravadora.delete()
    return redirect('listar_gravadora')