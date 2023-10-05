from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
  avaible_permissons = {
    'cadastrar_produtos': True,
    'liberar_descontos': True,
    'cadastrar_vendedores': True,
  }
  
  class Vendedor(AbstractUserRole):
    avaible_permissons = {
      'realizar_venda': True,
      'visualizar_comissoes': True,
    }