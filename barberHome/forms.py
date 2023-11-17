from django import forms
from .models import Contato, Agendamento

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # Correção aqui
            field.widget.attrs['class'] = 'form-control'
    
class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_cliente', 'email', 'data_agendamento', 'horario_agendamento']
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'data_agendamento': forms.DateInput(attrs={'class': 'form-control'}),
            'horario_agendamento': forms.TimeInput(attrs={'class': 'form-control'}),
        }
    

