from django.urls import path, include
from .views import barberHome, agendamento, galeria, contactMe, cadastrar, login, produtos
from barberHome import views

urlpatterns = [
    path('', barberHome, name='barberHome'),
    path('agendamento/', agendamento, name='agendamento'),
    path('galeria/', galeria, name='galeria'),
    path('contato/', views.contactMe, name='contato'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('login/', login, name='login'),
    path('produtos/', produtos, name='produtos'),
]
