"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_livros, cadastrar_livro, listar_cliente, cadastrar_cliente , listar_editora, cadastrar_editora

urlpatterns = [
    
    path('livro/', listar_livros,name='listar_livros'),
    path('livro-cadastro/', cadastrar_livro, name='cadastrar_livros'),
    path('cliente/', listar_cliente,  name= 'listar_clientes' ),
    path('clientes-cadastro/',cadastrar_cliente,name='cadastrar_clientes'),
    path('editora/', listar_editora, name ='listar_editora'),
    path('cadastrar-editora/', cadastrar_editora,name='cadastrar-editora'),
    path('admin/', admin.site.urls),
]
