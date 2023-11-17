from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContatoForm, AgendamentoForm
from django.contrib.auth.decorators import login_required
from .models import Produtos, Agendamento
from django.contrib import messages
from django.http import JsonResponse
from .utils import horario_disponivel 

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils import timezone

from datetime import timedelta, time, datetime

from django.utils.dateparse import parse_time


def parse_custom_time(value):
    try:
        return parse_time(value).replace(tzinfo=None)
    except Exception as e:
        print(f"Erro ao converter tempo: {e}")
        return None


def sucesso_agendamento(request):
    return HttpResponse('Agendamento realizado com sucesso!')


@login_required
def agendamento_autenticado(request):
    return render(request, 'agendamento.html')

def agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            nome_cliente = form.cleaned_data['nome_cliente']
            email = form.cleaned_data['email']
            data_agendamento = form.cleaned_data['data_agendamento']
            horario_agendamento = form.cleaned_data['horario_agendamento']

            if horario_disponivel(data_agendamento, horario_agendamento):
                agendamento = form.save()
                return redirect('sucesso_agendamento')  # Certifique-se de que 'sucesso_agendamento' está definido em suas urls
            else:
                return HttpResponse('Horário não disponível. Escolha outro horário.')
    else:
        form = AgendamentoForm()

    context = {
            'form': form,
            'horario_disponivel': horario_disponivel,
        }

    return render(request, 'barberHome/agendamento.html', context)

def horario_disponivel(data_agendamento, horario_agendamento):
    # Verifique se o horário está dentro do período de segunda a sexta-feira e horário comercial
    if data_agendamento.weekday() in range(0, 5):  # Verifica se é de segunda a sexta-feira
        horario_comercial_inicio = time(9, 0)  # Horário de abertura
        horario_comercial_fim = time(17, 0)    # Horário de fechamento

        if horario_comercial_inicio <= data_agendamento.time() < horario_comercial_fim:
            # Verifique se o horário já foi agendado
            if Agendamento.objects.filter(data_agendamento=data_agendamento, agendado=True).exists():
                return False
            else:
                return True

    return False


from django.http import JsonResponse
from .models import Agendamento

def obter_horarios_disponiveis(request):
    data_selecionada = request.GET.get('data', None)

    # Verificar se a data foi fornecida
    if not data_selecionada:
        return JsonResponse({"error": "Data não fornecida"}, status=400)

    try:
        # Consultar os horários já agendados para a data selecionada
        agendamentos_na_data = Agendamento.objects.filter(data_agendamento=data_selecionada, agendado=True)
        horarios_ocupados = [agendamento.horario_agendamento for agendamento in agendamentos_na_data]

        # Subtrair horários ocupados de todos os horários para obter os disponíveis
        horarios_disponiveis = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]

        for horario_ocupado in horarios_ocupados:
            if horario_ocupado in horarios_disponiveis:
                horarios_disponiveis.remove(horario_ocupado)

        print(f"Data Selecionada: {data_selecionada}")
        print(f"Horários Disponíveis: {horarios_disponiveis}")

        return JsonResponse(horarios_disponiveis, safe=False)

    except Exception as e:
        return JsonResponse({"error": f"Erro ao obter horários disponíveis: {str(e)}"}, status=500)



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
            
            messages.success(request, 'Mensagem enviada com sucesso!')  # Adicione esta linha
            return redirect('contato')
    else:
        form = ContatoForm()
        
    return render(request, 'contato.html', {'form': form})



def login_view(request):
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


def lista_produtos(request):
    produtos = Produtos.objects.all()  # Recupere todos os produtos
    return render(request, 'produtos.html', {'produtos': produtos})



