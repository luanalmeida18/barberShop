from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils.dateparse import parse_time

from datetime import datetime, date, time

from .forms import ContatoForm, AgendamentoForm
from .models import Produtos, Agendamento, Horarios


def parse_custom_time(value):
    """Tenta converter um valor para um objeto time."""
    try:
        return parse_time(value).replace(tzinfo=None)
    except Exception as e:
        print(f"Erro ao converter tempo: {e}")
        return None


def sucesso_agendamento(request):
    """Exibe a página de sucesso após um agendamento."""
    return render(request, 'sucesso_agendamento.html')


@login_required
def agendamento_autenticado(request):
    """Exibe a página de agendamento para usuários autenticados."""
    return render(request, 'agendamento.html')


def horario_disponivel(data_agendamento, horario_agendamento):
    """Verifica se um horário de agendamento está disponível."""
    try:
        if not isinstance(data_agendamento, date):
            raise TypeError("data_agendamento deve ser um objeto datetime.date")
        if not isinstance(horario_agendamento, time):
            raise TypeError("horario_agendamento deve ser um objeto datetime.time")

        if data_agendamento.weekday() in range(0, 5):  # Segunda a sexta
            horario_comercial_inicio = time(9, 0)
            horario_comercial_fim = time(17, 0)

            if horario_comercial_inicio <= horario_agendamento < horario_comercial_fim:
                if Agendamento.objects.filter(data_agendamento=data_agendamento, horario_agendamento=horario_agendamento).exists():
                    return False
                return True
        return False
    except TypeError as e:
        print(f"Erro: {e}")
        return False


def agendamento(request):
    """Processa o formulário de agendamento."""
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            data_agendamento = form.cleaned_data['data_agendamento']
            horario_agendamento = form.cleaned_data['horario_agendamento']

            if horario_disponivel(data_agendamento, horario_agendamento):
                form.save()
                messages.success(request, 'Agendamento realizado com sucesso!')
                return redirect('agendamento')
            else:
                messages.error(request, 'Horário indisponível. Por favor, escolha outro horário.')
        else:
            messages.error(request, 'Erro no formulário. Por favor, verifique os dados.')
    else:
        form = AgendamentoForm()

    return render(request, 'agendamento.html', {'form': form})


def obter_horarios_disponiveis(request):
    """Retorna os horários disponíveis para uma data específica."""
    data_selecionada = request.GET.get('data', None)

    if not data_selecionada:
        return JsonResponse({"error": "Data não fornecida"}, status=400)

    try:
        data_obj = datetime.strptime(data_selecionada, '%Y-%m-%d').date()

        horarios_disponiveis = Horarios.objects.filter(data=data_obj)
        agendamentos_na_data = Agendamento.objects.filter(data_agendamento=data_obj, agendado=True)
        horarios_ocupados = {agendamento.horario_agendamento.hora for agendamento in agendamentos_na_data}

        horarios_disponiveis_str = [horario.hora.strftime('%H:%M') for horario in horarios_disponiveis if horario.hora not in horarios_ocupados]

        print(f"Data Selecionada: {data_selecionada}")
        print(f"Horários Disponíveis: {horarios_disponiveis_str}")

        return JsonResponse(horarios_disponiveis_str, safe=False)

    except ValueError:
        return JsonResponse({"error": "Formato de data inválido. Use AAAA-MM-DD."}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Erro ao obter horários disponíveis: {str(e)}"}, status=500)


def verificar_disponibilidade(request):
    """Verifica se um horário está disponível para agendamento."""
    data_selecionada = request.GET.get('data', None)
    horario_selecionado = request.GET.get('horario', None)

    if not data_selecionada or not horario_selecionado:
        return JsonResponse({"disponivel": False, "error": "Data ou horário não fornecidos"}, status=400)

    try:
        data_obj = datetime.strptime(data_selecionada, '%Y-%m-%d').date()
        horario_obj = datetime.strptime(horario_selecionado + ':00', '%H:%M:%S').time()

        horario_disponivel_db = Horarios.objects.filter(data=data_obj, hora=horario_obj).exists()
        horario_agendado = Agendamento.objects.filter(data_agendamento=data_obj, horario_agendamento=horario_obj, agendado=True).exists()

        disponivel = horario_disponivel_db and not horario_agendado
        return JsonResponse({"disponivel": disponivel})

    except ValueError:
        return JsonResponse({"disponivel": False, "error": "Formato de data ou horário inválido"}, status=400)
    except Exception as e:
        return JsonResponse({"disponivel": False, "error": f"Erro ao verificar disponibilidade: {str(e)}"}, status=500)


def sendmail_contact(data):
    """Envia um email de contato."""
    message_body = get_template('send.html').render(data)
    email = EmailMessage('Formulário de Contato', message_body, settings.DEFAULT_FROM_EMAIL, to=['univespteste1@gmail.com'])
    email.content_subtype = 'html'
    return email.send()


def barberHome(request):
    """Exibe a página inicial da barbearia."""
    return render(request, 'barberHome.html')


def produtos(request):
    """Exibe a página de produtos."""
    return render(request, 'produtos.html')


def galeria(request):
    """Exibe a página da galeria."""
    return render(request, 'galeria.html')


def contactMe(request):
    """Processa o formulário de contato."""
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            sendmail_contact(data)
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'contato.html', {'form': form})


def login_view(request):
    """Exibe a página de login."""
    return render(request, 'login.html')


def salvar_produto(request):
    """Salva um produto no banco de dados."""
    produto = Produtos(
        prod_nome='Produto A',
        prod_descricao='Descrição do Produto A',
        prod_valor=19.99,
        prod_destaque=True
    )
    produto.save()
    return HttpResponse("Produto salvo com sucesso!")


def lista_produtos(request):
    """Exibe a lista de produtos."""
    produtos = Produtos.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})