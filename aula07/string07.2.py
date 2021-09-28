#Metodo Format substitui as variáveis passadas
# \' aspas simples
# \"" aspas duplas
# \n quebra de linha
# \r retorno de carga = ENTER
# \t tabulação
# \b backspace apaga o caractere anterior
cidade = "Sao Paulo"
dia = 15
mes = "Setembro"
ano = 2021
canal = "CFB Cursos"

data = "{}, {} de {} de {} \n \"{}\""  #formato de exibição <\n quebra linha> | <\"{}\" coloca entre aspas>
print(data.format(cidade,dia,mes,ano,canal))#forma de impressão

