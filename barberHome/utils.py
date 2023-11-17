# utils.py

from .models import Agendamento
from datetime import time

def horario_disponivel(data_agendamento):
    # Verifique se o horário está dentro do período de segunda a sábado e horário comercial
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
