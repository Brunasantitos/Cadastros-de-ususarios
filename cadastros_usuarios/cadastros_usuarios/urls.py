from django.urls import path
# importar views
from app_cadastros_usuarios import views

urlpatterns = [

    # rota, view responsável, nome de referência
    # se vc quiser somente o link do site (facebook.com)
    path('',views.home,name='home'), #somente pagina inicial
    # link mais detalhado
    #path('devaprender/')
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
