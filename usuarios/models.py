from django.db import models
from django.contrib.auth.models import AbstractUser #Importar AbstractBaseUser de django.contrib.auth.models

class Users(AbstractUser): #criar uma nova classe que erde de AbstractBaseUser e adicione um novo campo "Cargo", sendo 2 opções (Vendedor e Gerente), choices = escolha das opções
  choices_cargo = (('V', 'Vendedor'),
                  ('G', 'Gerente'))
  cargo = models.CharField(max_length=1, choices = choices_cargo)