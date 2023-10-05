from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD
from .models import Usuario, Horarios, Produtos
=======
from .models import Usuario, Horarios
>>>>>>> b0aef24c38fc6d21ed57ca5fd370d42804cf549b


def barberHome(request):
    return render(request, 'barberHome.html')

<<<<<<< HEAD
def produtos(request):
    return render(request, 'produtos.html')

=======
>>>>>>> b0aef24c38fc6d21ed57ca5fd370d42804cf549b
def ambiente(request):
    return render(request, 'ambiente.html')

def galeria(request):
    return render(request, 'galeria.html')

def contato(request):
    return render(request, 'contato.html')

def usuarios(request):
    return render(request, 'usuarios.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def login(request):
    return render(request, 'login.html')

<<<<<<< HEAD
def produtos(request):
    return render(request, 'produtos.html')


=======
>>>>>>> b0aef24c38fc6d21ed57ca5fd370d42804cf549b
def usuarios(request):

    #Salvar os inputs no Banco de Dados
    novo_usuario = Usuario()
    novo_usuario.client_name = request.POST.get('client_name', '')
    novo_usuario.client_email = request.POST.get('client_email', '')
    novo_usuario.client_user = request.POST.get('client_user', '')
    novo_usuario.client_password = request.POST.get('client_password', '')
    novo_usuario.client_phone = request.POST.get('client_phone', '')
    novo_usuario.client_cep = request.POST.get('client_cep', '')
    novo_usuario.client_city = request.POST.get('client_city', '')
    
    novo_usuario.save()
    
    #Exibir os usuarios cadastrados na tela
    usuarios = {
        'usuarios': Usuario.objects.all(),
    }
    
    #Retorna os dados para a página de listagem
    return render(request, 'usuarios.html', usuarios)

<<<<<<< HEAD
=======
def horarios(request):
    novo_horario = Horarios()
    novo_horario.primeiro = request.POST.get('primeiro', '')
    novo_horario.segundo = request.POST.get('segundo', '')
    novo_horario.terceiro = request.POST.get('terceiro', '')
    novo_horario.quarto = request.POST.get('quarto', '')
    novo_horario.quinto = request.POST.get('quinto','')
    novo_horario.sexto = request.POST.get('sexto','')
    novo_horario.setimo = request.POST.get('setimo','')
    novo_horario.oitavo = request.POST.get('oitavo','')
    
    novo_horario.save()
    
    usuarios = {
        'usuarios': Horarios.objects.all(),
    }
>>>>>>> b0aef24c38fc6d21ed57ca5fd370d42804cf549b
