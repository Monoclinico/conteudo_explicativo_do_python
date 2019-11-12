#Uma data no Python nao e um tipo de dado proprio, 
# mas podemos importar um modulo chamado datetime 
# para trabalhar com datas como objetos de data.

#MODULO DATETIME

import datetime

# O maior numero de ano permitido em um objeto de data ou data e hora.
print(datetime.MAXYEAR) 

# O menor numero de ano permitido em um objeto de data ou data e hora.
print(datetime.MINYEAR)

# CLASSES:

# Relacao das classes:
# datatime
#     .timedelta
#     .tzinfo
#         .timezone
#     .time
#     .date
#         .datetime

#==================================================================================================
# class datetime.date
# Uma data ingenua idealizada, assumindo que o atual calendario gregoriano sempre foi 
# e sempre estara em vigor. Atributos: ano, mes e dia.


# datetime.date(ano,mes,dia)
# Todos os argumentos sao obrigatorios. Os argumentos devem ser numeros inteiros, nos seguintes intervalos:
#          MINYEAR <= ano <= MAXYEAR
#          1 <= mes <= 12
#          1 <= dia <= numero de dias no mes e ano indicados
#      Se um argumento fora desses intervalos for fornecido, ValueError sera gerado.

# datetime.date.today()
# Retorna a data local atual.
print(datetime.date.today()) # 2019-11-12

# datetime.date.fromtimestamp(segundos)
# Retorna a data que representa os segundos especificados. Inicio: 1969-12-31
print(datetime.date.fromtimestamp(1_573_600_000)) # 2019-11-12

# date.fromordinal(ordinal)
# Retorne a data correspondente ao ordinal proleptico gregoriano, 
# onde 1 de janeiro do ano 1 tem o ordinal 1.
# ValueError e gerado, a menos que 1 <= ordinal <= date.max.toordinal (). 
# Para qualquer data d, date.fromordinal (d.toordinal ()) == d.
print(datetime.date.fromordinal(365)) # 0001-12-31

#==================================================================================================

# class datetime.time
# Um horario ideal, independente de qualquer dia em particular, assumindo que todos os 
# dias tenham exatamente 24 * 60 * 60 segundos. (Nao ha nocao de "segundos bissextos" aqui.) 
# Atributos: hora, minuto, segundo, microssegundo e tzinfo.

# class datetime.datetime
# Uma combinaçao de uma data e uma hora. Atributos: ano, mes, dia, hora, minuto, segundo,
# microssegundo e tzinfo.

# class datetime.timedelta
# Uma duraçao que expressa a diferença entre duas instancias de data, hora ou data e hora
# em resoluçao de microssegundos.

# class datetime.tzinfo
# Uma classe base abstrata para objetos de informações de fuso horario. Eles sao usados 
# pelas classes de data e hora para fornecer uma noçao personalizavel de ajuste de horario 
# (por exemplo, para considerar o fuso horario e / ou o horario de verao).

# class datetime.timezone
# Uma classe que implementa a classe base abstrata tzinfo como um deslocamento fixo do UTC.
