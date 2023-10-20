from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContatoForm
from django.contrib.auth.decorators import login_required
from .models import Produtos

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage


def sendmail_contact(data):
    message_body = get_template('send.html').render(data)
    
    email = EmailMessage('Formulário de Contato', message_body, settings.DEFAULT_FROM_EMAIL, to =[ 'univespteste1@gmail.com'])
    email.content_subtype = 'html'
    
    return email.send()

def barberHome(request):
    return render(request, 'barberHome.html')

def produtos(request):
    return render(request, 'produtos.html')

def agendamento(request):
    if request.user.is_authenticated:
        return render(request, 'agendamento.html')
    else:
        return redirect('login')

def galeria(request):
    return render(request, 'galeria.html')

def contactMe(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            
            data = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'subject': request.POST.get('subject'),
                'message': request.POST.get('message'),
            }
            
            sendmail_contact(data)
            
            
            return redirect('contato')
    else:
        form = ContatoForm()
            
    return render(request, 'contato.html', {'form': form})

def cadastrar(request):
    return render(request, 'cadastrar.html')

def login(request):
    return render(request, 'login.html')

def salvar_produto(request):
    # Crie uma instância do modelo com os valores desejados
    produto = Produtos(
        prod_nome='Produto A',
        prod_descricao='Descrição do Produto A',
        prod_valor=19.99,
        prod_destaque=True
    )

    # Salve o objeto no banco de dados
    produto.save()

    return HttpResponse("Produto salvo com sucesso!")



def listar_produtos(request):
    produtos = Produtos.objects.all()  # Recupere todos os produtos
    return render(request, 'produtos.html', {'produtos': produtos})

