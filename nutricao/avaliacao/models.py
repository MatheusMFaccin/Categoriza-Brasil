from django.db import models
from django import forms
from datetime import datetime
from empresa.models import Empresa
from usuario.models import User
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe




class Formulario(models.Model):
    
    valor_questoes = ["eliminatorio","eliminatorio","eliminatorio",1,1,2,1,12,2,12,12,3,6,3,3,2,4,2,3,9,3,6,2,2,4,8,16,2,12,9,8,12,8,12,16,12,12,12,6,16,8,8,12,8,12,16,6,6,4,"classificatorio","classificatorio"]
    lista_requisitos = [
    "1. Utiliza-se exclusivamente água potável para manipulação de alimentos (água de abastecimento público ou solução alternativa com potabilidade atestada semestralmente por meio de laudos laboratoriais).",
    "2. Instalações abastecidas de água corrente.",
    "3. Instalações dispõem de conexões com rede de esgoto ou fossa séptica.",
    "4. Reservatório devidamente tampado e conservado (livre de rachaduras, vazamentos, infiltrações, descascamentos, dentre outros defeitos).",
    "5. Reservatório em adequado estado de higiene.",
    "6. Reservatório de água higienizado em intervalo máximo de seis meses, sendo mantidos registros da operação.",
    "7. Material que reveste internamente o reservatório de água não compromete a qualidade da água.",
    "8. Instalações sanitárias possuem lavatórios de mãos e os produtos destinados à higiene pessoal (papel higiênico, sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e antisséptico, coletores com tampa e acionados sem contato manual e toalhas de papel não reciclado ou outro sistema higiênico e seguro para secagem das mãos).",
    "9. Existe separação entre as diferentes atividades por meios físicos ou por outros meios eficazes de forma a evitar a contaminação cruzada.",
    "10. Instalações, equipamentos, móveis e utensílios mantidos em condições higiênico-sanitárias apropriadas.",
    "11. Frequência adequada de higienização dos equipamentos, móveis e utensílios.",
    "12. Utensílios utilizados na higienização de instalações distintos daqueles usados para higienização das partes dos equipamentos e utensílios que entrem em contato com o alimento.",
    "13. Diluição, tempo de contato e modo de uso ou aplicação dos produtos saneantes obedece às instruções recomendadas pelo fabricante.",
    "14. Produtos saneantes regularizados pelo Ministério da Saúde.",
    "15. Áreas de preparação higienizadas quantas vezes forem necessárias e imediatamente após o término do trabalho.",
    "16. Controle de vetores e pragas urbanas executados por empresa especializada devidamente regularizada.",
    "17. Existência de um conjunto de ações eficazes e contínuas com o objetivo de impedir a atração, o abrigo, o acesso e ou proliferação de vetores e pragas urbanas.",
    "18. Edificações, instalações, equipamentos, móveis e utensílios livres da presença de animais, incluindo vetores e pragas urbanas.",
    "19. Os manipuladores são afastados da preparação de alimentos quando apresentam lesões e ou sintomas de enfermidades.",
    "20. Lavam cuidadosamente as mãos ao chegar ao trabalho, antes e após manipular o alimento, após qualquer interrupção do serviço, após tocar materiais contaminados, após usar os sanitários e sempre que se fizer necessário.",
    "21. Não fumam e falam quando desnecessário, cantam, assobiam, espirram, cospem, tossem, comem, manipulam dinheiro ou praticam outros atos que possam contaminar o alimento durante o desempenho das atividades.",
    "22. Submetidos à inspeção e aprovação na recepção.",
    "23. Matérias-primas, ingredientes e embalagens utilizados para preparação em condições higiênico sanitárias adequadas.",
    "24. Embalagens primárias das matérias-primas e dos ingredientes íntegras.",
    "25. Utilização das matérias primas e ingredientes respeita o prazo de validade ou se observa a ordem de entrada.",
    "26. Matérias-primas fracionadas adequadamente acondicionadas e identificadas com, no mínimo, as seguintes informações: designação do produto, data de fracionamento e prazo de validade após abertura ou retirada da embalagem original.",
    "27. Temperatura das matérias-primas e ingredientes perecíveis verificada na recepção e no armazenamento.",
    "28. Gelo utilizado em alimentos fabricado a partir de água potável e mantido em condição higiênico sanitária.",
    "29. Lavatórios da área de preparação dotados dos produtos destinados à higiene das mãos (sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e produto antisséptico, toalhas de papel não reciclado ou outro sistema higiênico e seguro de secagem das mãos).",
    "30. Durante o preparo, aqueles que manipulam alimentos crus realizam a lavagem e a antissepsia das mãos antes de manusear alimentos preparados.",
    "31. Produtos perecíveis expostos à temperatura ambiente somente pelo tempo mínimo necessário para preparação do alimento.",
    "32. Descongelamento conduzido conforme orientação do fabricante e utilizando uma das seguintes técnicas: refrigeração à temperatura inferior a 5ºC ou em forno de micro-ondas quando o alimento for submetido imediatamente à cocção.",
    "33. Alimentos submetidos ao descongelamento mantidos sob refrigeração se não forem imediatamente utilizados e não se recongela.",
    "34. Tratamento térmico garante que todas as partes do alimento atinjam a temperatura de, no mínimo, 70ºC, ou outra combinação de tempo e temperatura desde que assegure a qualidade higiênico-sanitária dos alimentos.",
    "35. Avalia-se a eficácia do tratamento térmico.",
    "36. Temperatura do alimento preparado no resfriamento reduzida de 60ºC a 10ºC em até 2 horas.",
    "37. Após o resfriamento, alimento preparado conservado sob refrigeração a temperaturas inferiores a 5ºC, ou congelado à temperatura igual ou inferior a - 18ºC.",
    "38. Alimentos consumidos crus, quando aplicável, submetidos a processo de higienização com produtos regularizados e aplicados de forma a evitar a presença de resíduos.",
    "39. Evita-se o contato direto ou indireto entre alimentos crus, semi-prontos e prontos para o consumo.",
    "40. Possuem termômetro comprovadamente calibrado para a aferição da temperatura dos alimentos.",
    "41. Alimento preparado armazenado sob refrigeração ou congelamento identificado com no mínimo as seguintes informações: designação, data de preparo e prazo de validade.",
    "42. Prazo máximo de consumo do alimento preparado e conservado sob refrigeração é de 5 dias, caso a temperatura de conservação seja igual ou inferior a 4ºC. Quando forem utilizadas temperaturas superiores a 4°C e inferiores a 5°C, o prazo máximo de consumo é reduzido.",
    "43. Alimento preparado e conservado sob refrigeração mantido à temperatura igual a 5ºC ou inferior.",
    "44. Alimentos conservados a quente mantidos a temperatura superior a 60ºC e o tempo ao longo da cadeia de preparo até exposição não excede a 6 horas.",
    "45. Alimentos preparados mantidos à temperatura superior a 60ºC.",
    "46. Temperatura dos equipamentos de exposição regularmente monitorada.",
    "47. Na exposição, manipuladores adotam procedimentos que minimizem o risco de contaminação dos alimentos preparados, por meio da antissepsia das mãos e pelo uso de utensílios ou luvas descartáveis (quando aplicável).",
    "48. Alimentos preparados, mantidos na área de armazenamento ou aguardando o transporte, identificados (designação do produto, data de preparo e o prazo de validade) e protegidos contra contaminantes.",
    "49. Armazenamento e transporte ocorrem em condições de tempo e temperatura que não comprometam a qualidade higiênico-sanitária do alimento preparado.",
    "50. Possui um responsável pelas atividades de manipulação de alimentos (responsável técnico, proprietário ou funcionário designado) comprovadamente capacitado.",
    "51 Possui implementado o Manual de Boas Práticas e os Procedimentos Operacionais Padronizados."
    ]
        
    pode_gerar_relatorio = False
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    Usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,blank=False)
    total_pontuacao = models.TextField()
    pt_abastecimento_agua = models.TextField(default="")
    pt_estrutura = models.TextField(default="")
    pt_higienizacao = models.TextField(default="")
    pt_controle_integrado = models.TextField(default="")
    pt_manipuladores = models.TextField(default="")
    pt_materias_primas = models.TextField(default="")
    pt_preparo_alimento = models.TextField(default="")
    pt_armazenamento = models.TextField(default="")

        


    CHOICES=[
                ("AD", "Adequado"),
                ("IN", "Inadequado"),
                ("NA", "Não se Aplica")
            ]
    descricao = 'Justifique sua escolha'

    questao1_descricao = models.TextField(blank=True, null=True)
    questao2_descricao  = models.TextField(blank=True, null=True)
    questao3_descricao = models.TextField(blank=True, null=True)
    questao4_descricao  = models.TextField(blank=True, null=True)
    questao5_descricao = models.TextField(blank=True, null=True)
    questao6_descricao  = models.TextField(blank=True, null=True)
    questao7_descricao = models.TextField(blank=True, null=True)
    questao8_descricao  = models.TextField(blank=True, null=True)
    questao9_descricao = models.TextField(blank=True, null=True)
    questao10_descricao  = models.TextField(blank=True, null=True)
    questao11_descricao = models.TextField(blank=True, null=True)
    questao12_descricao  = models.TextField(blank=True, null=True)
    questao13_descricao = models.TextField(blank=True, null=True)
    questao14_descricao  = models.TextField(blank=True, null=True)
    questao15_descricao = models.TextField(blank=True, null=True)
    questao16_descricao  = models.TextField(blank=True, null=True)
    questao17_descricao = models.TextField(blank=True, null=True)
    questao18_descricao  = models.TextField(blank=True, null=True)
    questao19_descricao = models.TextField(blank=True, null=True)
    questao20_descricao  = models.TextField(blank=True, null=True)
    questao21_descricao = models.TextField(blank=True, null=True)
    questao22_descricao  = models.TextField(blank=True, null=True)
    questao23_descricao = models.TextField(blank=True, null=True)
    questao24_descricao  = models.TextField(blank=True, null=True)
    questao25_descricao = models.TextField(blank=True, null=True)
    questao26_descricao  = models.TextField(blank=True, null=True)
    questao27_descricao = models.TextField(blank=True, null=True)
    questao28_descricao  = models.TextField(blank=True, null=True)
    questao29_descricao = models.TextField(blank=True, null=True)
    questao30_descricao  = models.TextField(blank=True, null=True)
    questao31_descricao = models.TextField(blank=True, null=True)
    questao32_descricao  = models.TextField(blank=True, null=True)
    questao33_descricao = models.TextField(blank=True, null=True)
    questao34_descricao  = models.TextField(blank=True, null=True)
    questao35_descricao = models.TextField(blank=True, null=True)
    questao36_descricao  = models.TextField(blank=True, null=True)
    questao37_descricao = models.TextField(blank=True, null=True)
    questao38_descricao  = models.TextField(blank=True, null=True)
    questao39_descricao = models.TextField(blank=True, null=True)
    questao40_descricao  = models.TextField(blank=True, null=True)
    questao41_descricao = models.TextField(blank=True, null=True)
    questao42_descricao  = models.TextField(blank=True, null=True)
    questao43_descricao = models.TextField(blank=True, null=True)
    questao44_descricao  = models.TextField(blank=True, null=True)
    questao45_descricao = models.TextField(blank=True, null=True)
    questao46_descricao  = models.TextField(blank=True, null=True)
    questao47_descricao = models.TextField(blank=True, null=True)
    questao48_descricao  = models.TextField(blank=True, null=True)
    questao49_descricao  = models.TextField(blank=True, null=True)
    questao50_descricao = models.TextField(blank=True, null=True)
    questao51_descricao  = models.TextField(blank=True, null=True)


    questao1 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="1. Utiliza-se exclusivamente água potável para manipulação de alimentos (água de abastecimento público ou solução alternativa com potabilidade atestada semestralmente por meio de laudos laboratoriais)."
    )
    questao2 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="2.  Instalações abastecidas de água corrente."

    )
    questao3 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="3. Instalações dispõem de conexões com rede de esgoto ou fossa séptica."
    )
    questao4 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="4.Reservatório devidamente tampado e conservado (livre de rachaduras, vazamentos, infiltrações, descascamentos, dentre outros defeitos)."
    )
    questao5 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="5. Reservatório em adequado estado de higiene."
    )
    questao6 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="6. Reservatório de água higienizado em intervalo máximo de seis meses, sendo mantidos registros da operação."
    )
    questao7 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="7. Material que reveste internamente o reservatório de água não compromete a qualidade da água."
    )
    questao8 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="8. Instalações sanitárias possuem lavatórios de mãos e os produtos destinados à higiene pessoal (papel higiênico, sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e antisséptico, coletores com tampa e acionados sem contato manual e toalhas de papel não reciclado ou outro sistema higiênico e seguro para secagem das mãos)."
    )
    questao9 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="9.Existe separação entre as diferentes atividades por meios físicos ou por outros meios eficazes de forma a evitar a contaminação cruzada."
    )
    questao10 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="10.Instalações, equipamentos, móveis e utensílios mantidos em condições higiênico-sanitárias apropriadas."
    )
    questao11 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="11.Frequência adequada de higienização dos equipamentos, móveis e utensílios."
    )
    questao12 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="12.Utensílios utilizados na higienização de instalações distintos daqueles usados para higienização das partes dos equipamentos e utensílios que entrem em contato com o alimento."
    )
    questao13 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="13.Diluição, tempo de contato e modo de uso ou aplicação dos produtos saneantes obedece às instruções recomendadas pelo fabricante."
    )
    questao14 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="14.Produtos saneantes regularizados pelo Ministério da Saúde."
    )
    questao15 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="15. Áreas de preparação higienizadas quantas vezes forem necessárias e imediatamente após o término do trabalho."
    )
    questao16 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="16.Controle de vetores e pragas urbanas executados por empresa especializada devidamente regularizada"
    )
    questao17 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="17. Existência de um conjunto de ações eficazes e contínuas com o objetivo de impedir a atração, o abrigo, o acesso e ou proliferação de vetores e pragas urbanas."
    )
    questao18 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="18.Edificações, instalações, equipamentos, móveis e utensílios livres da presença de animais, incluindo vetores e pragas urbanas."
    )
    questao19 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="19. Os manipuladores são afastados da preparação de alimentos quando apresentam lesões e ou sintomas de enfermidades."
    )
    questao20 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="20. Lavam cuidadosamente as mãos ao chegar ao trabalho, antes e após manipular o alimento, após qualquer interrupção do serviço, após tocar materiais contaminados, após usar os sanitários e sempre que se fizer necessário."
    )
    questao21 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="21.Não fumam e falam quando desnecessário, cantam, assobiam, espirram, cospem, tossem, comem, manipulam dinheiro ou praticam outros atos que possam contaminar o alimento durante o desempenho das atividades."
    )
    questao22 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="22.Submetidos à inspeção e aprovação na recepção."
    )
    questao23 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="23.Matérias-primas, ingredientes e embalagens utilizados para preparação em condições higiênico sanitárias adequadas."
    )
    questao24 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="24.Embalagens primárias das matérias-primas e dos ingredientes íntegras."
    )
    questao25 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="25.Utilização das matérias primas e ingredientes respeita o prazo de validade ou se observa a ordem de entrada."
    )
    questao26 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="26.Matérias-primas fracionadas adequadamente acondicionadas e identificadas com, no mínimo, as seguintes informações: designação do produto, data de fracionamento e prazo de validade após abertura ou retirada da embalagem original."
    )
    questao27 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="27.Temperatura das matérias-primas e ingredientes perecíveis verificada na recepção e no armazenamento."
    )
    questao28 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="28. Gelo utilizado em alimentos fabricado a partir de água potável e mantido em condição higiênico sanitária."
    )
    questao29 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="29.Lavatórios da área de preparação dotados dos produtos destinados à higiene das mãos (sabonete líquido inodoro antisséptico ou sabonete líquido inodoro e produto antisséptico, toalhas de papel não reciclado ou outro sistema higiênico e seguro de secagem das mãos)."
    )
    questao30 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="30.Durante o preparo, aqueles que manipulam alimentos crus realizam a lavagem e a antissepsia das mãos antes de manusear alimentos preparados."
    )
    questao31 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="31.Produtos perecíveis expostos à temperatura ambiente somente pelo tempo mínimo necessário para preparação do alimento."
    )
    questao32 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="32. Descongelamento conduzido conforme orientação do fabricante e utilizando uma das seguintes técnicas: refrigeração à temperatura inferior a 5ºC ou em forno de micro-ondas quando o alimento for submetido imediatamente à cocção."
    )
    questao33 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="33.Alimentos submetidos ao descongelamento mantidos sob refrigeração se não forem imediatamente utilizados e não se recongela."
    )
    questao34 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="34.Tratamento térmico garante que todas as partes do alimento atinjam a temperatura de, no mínimo, 70ºC, ou outra combinação de tempo e temperatura desde que assegure a qualidade higiênico-sanitária dos alimentos."
    )
    questao35 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="35.Avalia-se a eficácia do tratamento térmico."
    )
    questao36 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="36.Temperatura do alimento preparado no resfriamento reduzida de 60ºC a 10ºC em até 2 horas."
    )
    questao37 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="37.Após o resfriamento, alimento preparado conservado sob refrigeração a temperaturas inferiores a 5ºC, ou congelado à temperatura igual ou inferior a - 18ºC."
    )
    questao38 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="38.Alimentos consumidos crus, quando aplicável, submetidos a processo de higienização com produtos regularizados e aplicados de forma a evitar a presença de resíduos."
    )
    questao39 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="39.Evita-se o contato direto ou indireto entre alimentos crus, semi-prontos e prontos para o consumo."
    )
    questao40 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="40.Possuem termômetro comprovadamente calibrado para a aferição da temperatura dos alimentos."
    )
    questao41 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="41.Alimento preparado armazenado sob refrigeração ou congelamento identificado com no mínimo as seguintes informações: designação, data de preparo e prazo de validade."
    )
    questao42 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="42.Prazo máximo de consumo do alimento preparado e conservado sob refrigeração é de 5 dias, caso a temperatura de conservação seja igual ou inferior a 4ºC. Quando forem utilizadas temperaturas superiores a 4°C e inferiores a 5°C, o prazo máximo de consumo é reduzido."
    )
    questao43 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="43.Alimento preparado e conservado sob refrigeração mantido à temperatura igual a 5ºC ou inferior."
    )
    questao44 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="44.Alimentos conservados a quente mantidos a temperatura superior a 60ºC e o tempo ao longo da cadeia de preparo até exposição não excede a 6 horas."
    )
    questao45 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="45.Alimentos preparados mantidos à temperatura superior a 60ºC."
    )
    questao46 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="46.Temperatura dos equipamentos de exposição regularmente monitorada.."
    )
    questao47 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="47.Na exposição, manipuladores adotam procedimentos que minimizem o risco de contaminação dos alimentos preparados, por meio da antissepsia das mãos e pelo uso de utensílios ou luvas descartáveis (quando aplicável)."
    )
    questao48 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="48. Alimentos preparados, mantidos na área de armazenamento ou aguardando o transporte, identificados (designação do produto, data de preparo e o prazo de validade) e protegidos contra contaminantes."
    )
    questao49 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="49.Armazenamento e transporte ocorrem em condições de tempo e temperatura que não comprometam a qualidade higiênico-sanitária do alimento preparado."
    )
    questao50 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="50.Possui um responsável pelas atividades de manipulação de alimentos (responsável técnico, proprietário ou funcionário designado) comprovadamente capacitado. "
    )
    questao51 = models.CharField(
        max_length=10,
        choices=CHOICES,  # Valor padrão, caso queira
        verbose_name="51.Possui implementado o Manual de Boas Práticas e os Procedimentos Operacionais Padronizados"
    )

    
   


    
        

    

    


        








