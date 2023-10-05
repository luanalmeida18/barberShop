import hashlib

from django.db import models

class Usuario(models.Model):
  id_client = models.AutoField(primary_key = True)
  client_name = models.CharField(max_length = 255)
  client_email = models.EmailField()
  client_user = models.CharField(max_length = 255)
  client_password = models.CharField(max_length = 128)
  client_phone = models.CharField(max_length = 13)
  client_cep = models.CharField(max_length = 255)
  client_city = models.CharField(max_length = 255)
  created_at = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
        return self.client_user
      
  def set_password(self, password):
        # Gere o hash da senha
        client_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.client_password = client_password

  def save(self, *args, **kwargs):
        if self.client_password:
            self.set_password(self.client_password)
        super(Usuario, self).save(*args, **kwargs)

<<<<<<< HEAD
class Horarios(models.Model):
      hora_inicio = models.TimeField(max_length=255)
      hora_fim = models.TimeField(max_length=255)
      
class Produtos(models.Model):
      nome = models.CharField(max_length = 255)
      descricao = models.CharField(max_length = 255)
      valor = models.FloatField(max_length = 255)     
      destaque = models.BooleanField(default=True)
      
=======
class Valores(models.Model):
  corte_name = models.TextField(max_length = 255)
  corte_valor = models.FloatField(max_length = 255)

class Horarios(models.Model):
      primeiro = models.TimeField(max_length=255),
      segundo = models.TimeField(max_length=255),
      terceiro = models.TimeField(max_length=255),
      quarto = models.TimeField(max_length=255),
      quinto = models.TimeField(max_length=255),
      sexto = models.TimeField(max_length=255),
      setimo = models.TimeField(max_length=255),
      oitavo = models.TimeField(max_length=255),
>>>>>>> b0aef24c38fc6d21ed57ca5fd370d42804cf549b
