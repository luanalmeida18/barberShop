from django.urls import path, include
from .views import barberHome, agendamento, galeria, contactMe, login_view, produtos, lista_produtos, obter_horarios_disponiveis, sucesso_agendamento
from barberHome import views
from . import views

urlpatterns = [
    path('', barberHome, name='barberHome'),
    path('agendamento/', agendamento, name='agendamento'),
    path('galeria/', galeria, name='galeria'),
    path('contato/', views.contactMe, name='contato'),
    path('login/', login_view, name='login_view'),
    path('produtos/', lista_produtos, name='lista_produtos'),
    path('lista-produtos/', lista_produtos, name='lista_produtos'),
    path('obter_horarios_disponiveis/', obter_horarios_disponiveis, name='obter_horarios_disponiveis'),
    path('sucesso_agendamento/', sucesso_agendamento, name='sucesso_agendamento'),
]
