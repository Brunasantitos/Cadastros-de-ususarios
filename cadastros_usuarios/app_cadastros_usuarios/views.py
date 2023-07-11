from django.shortcuts import render

# request é um comando embutido em django, permite acessar os dados dentro da pagina


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    pass