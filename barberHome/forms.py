from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = ['name', 'email', 'subject', 'message']
    
  def __init__ (self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in kwargs.items():
      field.widget.attrs['class'] = 'form control'
  