from django.db import models

class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=255, default='')
    email = models.EmailField()
    data_agendamento = models.DateField()
    horario_agendamento = models.TimeField(default='00:00:00')  # Adicione esta linha
    agendado = models.BooleanField(default=False)

class Usuario(models.Model):
    id_client = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_user = models.CharField(max_length=255)
    client_password = models.CharField(max_length=128)
    client_phone = models.CharField(max_length=13)
    client_cep = models.CharField(max_length=255)
    client_city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

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

class Produtos(models.Model):
    prod_nome = models.CharField(max_length=255)
    prod_descricao = models.CharField(max_length=255)
    prod_valor = models.DecimalField(max_digits=10, decimal_places=2)
    prod_destaque = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='static/img/produtos/', null=True, blank=False)

    def __str__(self):
        return self.prod_nome

class Valores(models.Model):
    corte_name = models.TextField(max_length=255)
    corte_valor = models.FloatField(max_length=255)

class Contato(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Horarios(models.Model):
    data = models.TextField(max_length=30)
    hora = models.TextField(max_length=10)

class HorariosDisponivel(models.Model):
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
