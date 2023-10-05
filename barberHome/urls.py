from django.urls import path, include
from .views import barberHome, ambiente, galeria, contato, cadastrar, login, usuarios

urlpatterns = [
    path('', barberHome, name='barberHome'),
    path('ambiente/', ambiente, name='ambiente'),
    path('galeria/', galeria, name='galeria'),
    path('contato/', contato, name='contato'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('login/', login, name='login'),
    path('usuarios/', usuarios, name='usuarios'),
]
