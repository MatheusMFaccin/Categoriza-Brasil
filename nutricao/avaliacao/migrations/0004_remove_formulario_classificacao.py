# Generated by Django 4.2.16 on 2024-11-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0003_formulario_classificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='classificacao',
        ),
    ]
