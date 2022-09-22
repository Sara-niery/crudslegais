
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import listar_musica, cadastrar_musica, atualizar_musica, deletar_musica
from core.views import listar_cliente, cadastrar_cliente , atualizar_cliente, deletar_cliente 
from core.views import listar_gravadora, cadastrar_gravadora, atualizar_gravadora, deletar_gravadora
from core.views import primeirapag

urlpatterns = [
    path('',primeirapag, name='primeirapag'),

    path('musica/', listar_musica,name='listar_musica'),
    path('musica/cadastrar', cadastrar_musica, name='cadastrar_musica'),
    path('musica/atualizar/<int:id>', atualizar_musica, name='atualizar_musica'),
    path('musica/deletar/<int:id>', deletar_musica, name='deletar_musica'),

    path('cliente/', listar_cliente,  name= 'listar_cliente' ),
    path('clientes/cadastrar/',cadastrar_cliente,name='cadastrar_cliente'),
    path('cliente/atualizar/<int:id>',atualizar_cliente, name='atualizar_cliente'),
    path('cliente/deletar/<int:id>', deletar_cliente,name='deletar_cliente'),

    path('gravadora/', listar_gravadora , name ='listar_gravadoras'),
    path('gravadora/cadastrar/', cadastrar_gravadora ,name='cadastrar_gravadoras'),
    path('gravadora/atualizar/<int:id>', atualizar_gravadora, name='atualizar_gravadoras'),
    path('gravadora/deletar/<int:id>',deletar_gravadora, name='deletar_gravadoras'),

    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
