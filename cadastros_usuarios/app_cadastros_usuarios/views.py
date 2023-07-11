from django.shortcuts import render
from .models import Usuario
# request é um comando embutido em django, permite acessar os dados dentro da pagina


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos os usuarios já cadastrados em uma nova pasta
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados par a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)

    

    