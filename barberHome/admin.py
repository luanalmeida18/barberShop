from .models import Produtos
from django.contrib import admin


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('prod_nome', 'prod_descricao', 'prod_valor', 'prod_destaque')
