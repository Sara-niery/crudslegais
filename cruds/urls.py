
from django.contrib import admin
from django.urls import path
from core.views import listar_livros, cadastrar_livro, atualizar_livro, deletar_livro
from core.views import listar_cliente, cadastrar_cliente , listar_editora, cadastrar_editora

urlpatterns = [
    
    path('livro/', listar_livros,name='listar_livros'),
    path('livro/cadastrar', cadastrar_livro, name='cadastrar_livro'),
    path('livro/atualizar/<int:id>', atualizar_livro, name='atualizar_livro'),
    path('livro/deletar/<int:id>', deletar_livro, name='deletar_livro'),

    path('cliente/', listar_cliente,  name= 'listar_clientes' ),
    path('clientes-cadastro/',cadastrar_cliente,name='cadastrar_clientes'),
    path('editora/', listar_editora, name ='listar_editora'),
    path('cadastrar-editora/', cadastrar_editora,name='cadastrar-editora'),
    path('admin/', admin.site.urls),
]
