# Generated by Django 4.2.16 on 2024-12-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.CharField(choices=[('VIGILANCIA', 'Vigilância'), ('PREFEITURA', 'Prefeitura'), ('EMPRESA', 'Empresa'), ('OUTRO', 'Outro')], max_length=13),
        ),
    ]