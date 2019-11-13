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
# metodos: timetuple() toordinal() weekday() isoweekday(), isocalendar(), isoformat() ctime() strftime()
# atributos: year, month, day
data = datetime.date(2019,11,13)
print(data) #2019-11-13
print(data.day) #13
print(data.month) #11
print(data.year) #2019
print(data.weekday()) #2 == Wednesday
print(data.isoweekday()) #3 == Wednesday
print(data.resolution) # 1 day, 0:00:00
print(data.ctime()) # Wed Nov 13 00:00:00 2019
print(data.replace(2019,11,14)) # 2019-11-14
print(data.strftime("%B, %A %Y ")) # November, Wednesday 2019
print(data.timetuple()) #time.struct_time(tm_year=2019, tm_mon=11, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=317, tm_isdst=-1)
print(data.toordinal()) #737376

# datetime.date.today()
# Retorna a data local atual.
print(datetime.date.today()) # 2019-11-12

# datetime.date.fromtimestamp(segundos)
# Retorna a data que representa os segundos especificados. Inicio: 1969-12-31
print(datetime.date.fromtimestamp(1_573_600_000)) # 2019-11-12

# datetime.date.fromordinal(ordinal)
# Retorne a data correspondente ao ordinal proleptico gregoriano, 
# onde 1 de janeiro do ano 1 tem o ordinal 1.
# ValueError e gerado, a menos que 1 <= ordinal <= date.max.toordinal (). 
# Para qualquer data d, date.fromordinal (d.toordinal ()) == d.
# Retorna a data de acordo com a quantidade de dias.
print(datetime.date.fromordinal(365)) # 0001-12-31

# datetime.date.fromisoformat(date_string) -Apartir da versao 3.7
# Retorne uma data correspondente a uma date_string fornecida no formato AAAA-MM-DD:
print(datetime.date.fromisoformat("2019-11-13")) #2019-11-13

# datetime.date.fromisocalendar(ano,semana,dia) -Apartir da versao 3.8
# Retorne uma data correspondente à data do calendário ISO especificada por ano, semana e dia. 
# Este é o inverso da função date.isocalendar ().
# print(datetime.date.fromisocalendar())

# datetime.date.min
# A primeira data representável, data (MINYEAR, 1, 1).
print(datetime.date.min) # 0001-01-01

# datetime.date.max
# A ultima data representável, data (MINYEAR, 1, 1).
print(datetime.date.max) # 9999-12-31

# datetime.date.resolution
# A menor diferença possível entre objetos de data não iguais, timedelta (dias = 1).
print(datetime.date.resolution) # 1 day, 0:00:00

# datetime.date.year
# Retorna o ano entre MINYEAR e MAXYEAR.
print(datetime.date.year)
print(data.year)

# datetime.date.month
# Retorna o mes entre 1 e 12.
print(datetime.date.month)
print(data.month)

# datetime.date.day
# Retorna o dia entre os dias do mes referente.
print(datetime.date.day)
print(data.day)

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