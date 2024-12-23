# Generated by Django 4.2.16 on 2024-11-23 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0005_alter_formulario_empresa_alter_formulario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='pt_abastecimento_agua',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_armazenamento',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_controle_integrado',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_estrutura',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_higienizacao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_manipuladores',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_materias_primas',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='formulario',
            name='pt_preparo_alimento',
            field=models.TextField(default=''),
        ),
    ]
