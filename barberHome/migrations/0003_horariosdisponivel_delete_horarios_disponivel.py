# Generated by Django 4.2.4 on 2023-11-16 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barberHome', '0002_agendamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorariosDisponivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barberHome.horarios')),
            ],
        ),
        migrations.DeleteModel(
            name='horarios_disponivel',
        ),
    ]