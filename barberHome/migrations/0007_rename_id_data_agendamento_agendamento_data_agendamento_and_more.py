# Generated by Django 4.2.6 on 2023-11-25 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barberHome', '0006_rename_data_agendamento_agendamento_id_data_agendamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='id_data_agendamento',
            new_name='data_agendamento',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='id_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='id_horario',
            new_name='horario_agendamento',
        ),
        migrations.RenameField(
            model_name='agendamento',
            old_name='id_nome',
            new_name='nome_cliente',
        ),
    ]
