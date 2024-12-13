# Generated by Django 4.2.14 on 2024-08-05 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao1', models.CharField(max_length=100, verbose_name='razão social: ')),
                ('questao2', models.CharField(max_length=100, verbose_name='Nome Fantasia: ')),
                ('questao3', models.CharField(max_length=50, verbose_name='Alvara/licença sanitaria ')),
                ('questao4', models.CharField(max_length=20, verbose_name='Inscrição Estadual / Municipal ')),
                ('questao5', models.CharField(max_length=14, unique=True, verbose_name='CNPJ/CPF ')),
                ('questao6', models.CharField(max_length=20, verbose_name='Fone: ')),
                ('questao7', models.CharField(max_length=100, unique=True, verbose_name='E-MAIL: ')),
                ('questao8', models.CharField(max_length=100, verbose_name='Endereço(Rua/Av): ')),
                ('questao9', models.CharField(max_length=50, verbose_name='Complemento: ')),
                ('questao10', models.CharField(max_length=50, verbose_name='Bairro: ')),
                ('questao11', models.CharField(max_length=50, verbose_name='Município: ')),
                ('questao12', models.CharField(max_length=2, verbose_name='-UF: ')),
                ('questao13', models.CharField(max_length=8, verbose_name='CEP: ')),
                ('questao14', models.CharField(choices=[('refeições', '5611-2/01 - restaurantes e similares'), ('bebidas', '5611-2/02 - bares e outros estabelecimentos especializados  em   servir bebidas'), ('lanches', '5611-2/03- lanchonetes, casas de chá, de sucos e similares')], default='', max_length=10, verbose_name='Classificação Nacional da Atividade Econômica (CNAE)')),
                ('questao15', models.CharField(choices=[('100', 'até 100'), ('101 A 300', '101 a 300'), ('301 A 1000', '301 a 1000'), ('1001 A 2500', '1001 a 2500'), ('mais de 2500', 'acima de 2500')], default='', max_length=12, verbose_name='Número de refeições servidas diariamente')),
                ('questao16', models.CharField(choices=[('1 A 4', 'de 1 a 4'), ('5 A 9', '5 a 9'), ('10 A 19', '10 a 19'), ('mais de 20', '20 ou mais')], default='', max_length=10, verbose_name='Pessoal ocupado (número de pessoas envolvidas nesta atividade econômica/ n° funcionários):')),
                ('questao17', models.CharField(choices=[('SIM', 'sim'), ('NAO', 'não')], default='', max_length=10, verbose_name='Tem responsável pelas Boas Práticas?')),
                ('questao18', models.CharField(choices=[('CA', 'Curso de Capacitação'), ('NT', 'Nível Técnico'), ('NS', 'Nível Superior')], default='', max_length=10, verbose_name='Formação Acadêmica')),
                ('questao19', models.CharField(max_length=100, verbose_name='Responsável Legal/ Responsável legal do Estabelecimento:')),
                ('questao20', models.CharField(choices=[('SIM', 'sim'), ('NÃO', 'NÃO'), ('EP', 'em processo'), ('NA', 'não se aplica')], default='', max_length=10, verbose_name='Possui Alvará Sanitário*?')),
            ],
        ),
    ]