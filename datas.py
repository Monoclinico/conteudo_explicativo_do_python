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
# Representa uma data, com ano, mes e dia, assumindo que o atual calendario gregoriano sempre foi
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
data2 = datetime.date(2020,11,13)
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

#Operacoes
print(data == data2) # False
print(data > data2) # False
print(data < data2) # True
data3 = data2 - data
print(data3) # 366 days, 0:00:00

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
# Retorne uma data correspondente a data do calendario ISO especificada por ano, semana e dia.
# Este e o inverso da funcao date.isocalendar ().
# print(datetime.date.fromisocalendar())

# datetime.date.min
# A primeira data representavel, data (MINYEAR, 1, 1).
print(datetime.date.min) # 0001-01-01

# datetime.date.max
# A ultima data representavel, data (MINYEAR, 1, 1).
print(datetime.date.max) # 9999-12-31

# datetime.date.resolution
# A menor diferenca possivel entre objetos de data nao iguais, timedelta (dias = 1).
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
# Representa um horario, com horas, minutos, segundos e microsegundos,
# independente de qualquer dia em particular,
# assumindo que todos os dias tenham exatamente 24 * 60 * 60 segundos.
# (Nao ha nocao de "segundos bissextos" aqui.) Atributos: hora, minuto, segundo, microssegundo e tzinfo.
# Um objeto de hora representa uma hora do dia (local), independente de qualquer dia em particular,
# e sujeito a ajustes por meio de um objeto tzinfo.
# classe datetime.time (hora = 0, minuto = 0, segundo = 0, microssegundo = 0, tzinfo = Nenhum, *, dobra = 0)
# Todos os argumentos sao opcionais. tzinfo pode ser None ou uma instância de uma subclasse tzinfo.
# Os argumentos restantes devem ser numeros inteiros nos seguintes intervalos:
#         0 <= hora <24,
#         0 <= minuto <60,
#         0 <= segundo <60,
#         0 <= microssegundo <1000000,
#         dobre em [0, 1].
# Se um argumento fora desses intervalos for fornecido, ValueError sera gerado.
# Todos assumem como padrao 0, exceto tzinfo, cujo padrao e Nenhum.
horario = datetime.time(17,18,50,60)
print(horario) # 17:18:50

# datetime.time.min
# A primeira hora representavel, hora (0, 0, 0, 0).
print(horario.min) # 00:00:00

# datetime.time.max
# A ultima hora representavel, hora (23,59,59.999999)
print(horario.max) # 23:59:59.999999

# datetime.time.resolution
# A menor diferenca possivel entre objetos de tempo nao iguais, timedelta (microssegundos = 1),
# embora observe que a aritmetica nos objetos de tempo nao e suportada.
print(horario.resolution) #0:00:00.000001

# datetime.time.hour.
# Mostra a hora.
print(horario.hour) # 17

# datetime.time.minute.
# Mostra o minuto.
print(horario.minute) # 18

# datetime.time.second.
# Mostra o segundo.
print(horario.second) # 50

# datetime.time.microsecond.
# Mostra o microsegundo.
print(horario.microsecond) # 60

# datetime.time.tzinfo
# O objeto passou como argumento tzinfo para o construtor de tempo, ou Nenhum se nenhum foi passado.
print(horario.tzinfo) # None

#datetime.time.fold
#Em [0, 1]. Usado para desambiguar os tempos da parede durante um intervalo repetido.
# (Um intervalo repetido ocorre quando os relogios sao revertidos no final do horario de verao
# ou quando o deslocamento UTC da zona atual e diminuido por motivos politicos.)
# O valor 0 (1) representa o anterior (mais tarde) dos dois momentos com a mesma representacao de tempo da parede.
#Novo na versao 3.6.
print(horario.fold) # 0


#==================================================================================================
# class datetime.datetime
# Uma combinacao de uma data e uma horario. Atributos: ano, mes, dia, hora, minuto, segundo,
# microssegundo e tzinfo.
# Um objeto de data e hora e um unico objeto que contem todas as informacoes de um objeto
# de data e um objeto de hora.
# classe datetime.datetime (ano, mes, dia, hora = 0, minuto = 0, segundo = 0, microssegundo = 0,
# tzinfo = Nenhum, *, dobra = 0)

# Os argumentos de ano, mes e dia sao obrigatorios. tzinfo pode ser None ou
# uma instancia de uma subclasse tzinfo. Os argumentos restantes devem ser numeros inteiros
# nos seguintes intervalos:
#          MINYEAR <= ano <= MAXYEAR,
#          1 <= mes <= 12,
#          1 <= dia <= numero de dias no mes e ano indicados,
#          0 <= hora < 24,
#          0 <= minuto < 60,
#          0 <= segundo < 60,
#          0 <= microssegundo < 1000000,
#          dobre em [0, 1].
# Se um argumento fora desses intervalos for fornecido, ValueError sera gerado.

# datetime.datetime.today()
# Retorna a data e horario local.
print(datetime.datetime.today()) # Exemplo: 2019-11-22 15:08:00.948034

# datetime.now(tz=None)
# Retorna a data e horario local
print(datetime.datetime.now()) # Exemplo: 2019-11-22 15:11:03.292463

# datetime.datetime.utcnow()
# Retorna a data e o horario UTC atual, com tzinfo = None.
print(datetime.datetime.utcnow()) # Exemplo: 2019-11-22 18:51:01.638695

# datetime.datetime.fromtimestamp(timestamp(segundos), tz=None)
# Retorne a data e hora locais correspondentes ao registro de data e hora do POSIX,
# como é retornado por time.time (). Se o argumento opcional tz for Nenhum ou não for especificado,
# o registro de data e hora será convertido na data e hora locais da plataforma
# e o objeto datetime retornado será ingênuo.
print(datetime.datetime.fromtimestamp(86400)) # 1970-01-01 21:00:00

# datetime.datetime.utcfromtimestamp(timestamp)
# Retorne a data e hora locais UTC correspondentes ao registro de data e hora do POSIX.
print(datetime.datetime.utcfromtimestamp(0)) # 1970-01-01 00:00:00

# datetime.datetime.fromordinal(ordinal)
# Retorne um novo objeto de data e hora cujos componentes de data sejam iguais aos do objeto de data especificado
# e cujos componentes de hora sejam iguais aos do objeto de data especificado.
# Se o argumento tzinfo for fornecido, seu valor será usado para configurar o atributo tzinfo do resultado,
# caso contrário, o atributo tzinfo do argumento time será usado.
# Para qualquer objeto datetime d, d == datetime.combine (d.date (), d.time (), d.tzinfo).
# Se date for um objeto datetime, seus componentes de tempo e atributos tzinfo serão ignorados.
print(datetime.datetime.fromordinal(365)) # 0001-12-31 00:00:00

# datetime.datetime.combine(date, time, tzinfo=self.tzinfo)
# Retorne um novo objeto de data e hora cujos componentes de data sejam iguais aos do objeto
# de data especificado e cujos componentes de hora sejam iguais aos do objeto de data especificado.
# Se o argumento tzinfo for fornecido, seu valor será usado para configurar o atributo tzinfo do resultado,
# caso contrário, o atributo tzinfo do argumento time será usado.
# Para qualquer objeto datetime d, d == datetime.combine (d.date (), d.time (), d.tzinfo).
# Se date for um objeto datetime, seus componentes de tempo e atributos tzinfo serão ignorados.
# Alterado na versão 3.6: adicionado o argumento tzinfo.
print(datetime.datetime.combine(datetime.date(2010,12,3),datetime.time(12,30,0))) # 2010-12-03 12:30:00

# datetime.datetime.fromisoformat(date_string)
# Retorne um datetime correspondente a um date_string em um dos formatos emitidos por date.isoformat ()
# e datetime.isoformat ().
# Especificamente, esta função suporta seqüências de caracteres no formato:
# AAAA-MM-DD [* HH [: MM [: SS [.fff [fff]]]] [+ HH: MM [: SS [.ffffff]]]]
# onde * pode corresponder a qualquer caractere único.
print(datetime.datetime.fromisoformat("2019-11-22 17:14:00")) # 2019-11-22 17:14:00

# datetime.datetime.fromisocalendar(year, week, day)
# Retorne uma data e hora correspondentes à data do calendário ISO especificada por ano, semana e dia.
# Os componentes não datados da data e hora são preenchidos com seus valores padrão normais.
# Este é o inverso da função datetime.isocalendar ().
# Novo na versão 3.8.

# datetime.datetime.strptime(date_string, format)
# Retorne um datetime correspondente a date_string, analisado de acordo com o formato.
# Isso é equivalente a:
# datetime (* (time.strptime (date_string, formato) [0: 6]))
# O ValueError é gerado se o date_string e o formato não puderem ser analisados por time.strptime ()
# ou se ele retornar um valor que não seja uma tupla de tempo.
# Para obter uma lista completa das diretivas de formatação, consulte Comportamento strftime () e strptime ().
datetime_str = '09/19/19 13:55:26'
datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print(datetime_object)  # 2019-09-19 13:55:26

# datetime.datetime.min
# O mais antigo datetime representável, datetime (MINYEAR, 1, 1, tzinfo = None).
print(datetime.datetime.min) # 0001-01-01 00:00:00

# datetime.datetime.max
# O mais recente datetime representável, datetime (MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo = Nenhum).
print(datetime.datetime.max) # 9999-12-31 23:59:59.999999

# datetime.datetime.resolution
# A menor diferença possível entre objetos de data e hora diferentes, timedelta (microssegundos = 1).
print(datetime.datetime.resolution)

data_tempo = datetime.datetime(2019,11,22,17,11,52,1020)
# datetime.datetime.year
# Entre MINYEAR e MAXYEAR inclusive.
print(data_tempo.year) # 2019

# datetime.datetime.month
# Entre 1 e 12 inclusive.
print(data_tempo.month) # 11

# datetime.datetime.day
# Entre 1 e o número de dias no mês especificado do ano especificado.
print(data_tempo.day) # 22

# datetime.datetime.hour
# No intervalo (24).
print(data_tempo.hour) # 17

# datetime.datetime.minute
# No intervalo (60).
print(data_tempo.minute) # 11

# datetime.datetime.second
# No intervalo (60).
print(data_tempo.second) # 52

# datetime.datetime.microsecond
# No intervalo (1000000).
print(data_tempo.microsecond) # 1020

# datetime.datetime.tzinfo
# O objeto passou como o argumento tzinfo para o construtor datetime, ou None se nenhum foi passado.
print(data_tempo.tzinfo) # None

# datetime.fold
# Em [0, 1]. Usado para desambiguar os tempos da parede durante um intervalo repetido.
# (Um intervalo repetido ocorre quando os relógios são revertidos no final do horário
# de verão ou quando o deslocamento UTC da zona atual é diminuído por motivos políticos.)
# O valor 0 (1) representa o anterior (mais tarde) dos dois momentos com a
# mesma representação de tempo da parede.
# Novo na versão 3.6.

# Operacoes:
# datetime2 = datetime1 + timedelta
# datetime2 = datetime1 - timedelta
# timedelta = datetime1 - datetime2
# datetime1 < datetime2

#datetime.datetime.date()
# Retorna a data
print(data_tempo.date()) # 2019-11-22

#datetime.datetime.time()
# Retorna o tempo
print(data_tempo.time()) # 17:11:52.001020

# datetime.timetz()
# Retorne o objeto de tempo com os mesmos atributos de hora, minuto, segundo, microssegundo, dobra e tzinfo.
# Veja também método time ().

# datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour,
# minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, * fold=0)
# Retorne um datetime com os mesmos atributos, exceto para aqueles atributos que recebem novos valores,
# independentemente dos argumentos da palavra-chave especificados.
# Observe que tzinfo = None pode ser especificado para criar um data / hora ingênuo
# a partir de um data / hora consciente, sem conversão de dados de data e hora.
# Novo na versão 3.6: adicionado o argumento de dobra.


# datetime.astimezone(tz=None)

# datetime.utcoffset()

# datetime.dst()

# datetime.tzname()

# datetime.timetuple()

# datetime.utctimetuple()

# datetime.toordinal()

# datetime.timestamp()

# datetime.weekday()

# datetime.isoweekday()

# datetime.isocalendar()

# datetime.isoformat(sep='T', timespec='auto')

# datetime.__str__()

# datetime.ctime()

# datetime.strftime(formatdatetime.__format__(format)

#==================================================================================================
# class datetime.timedelta
# Uma duracao que expressa a diferenca entre duas instancias de data, hora ou data e hora
# em resolucao de microssegundos.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# Todos os argumentos são opcionais e o padrão é 0. Os argumentos podem ser números inteiros ou flutuantes 
# e podem ser positivos ou negativos.
# Apenas dias, segundos e microssegundos são armazenados internamente. Os argumentos são convertidos 
# nessas unidades:
#          Um milissegundo é convertido em 1000 microssegundos.
#          Um minuto é convertido em 60 segundos.
#          Uma hora é convertida em 3600 segundos.
#          Uma semana é convertida em 7 dias.
#      dias, segundos e microssegundos são normalizados para que a representação seja única, com
#          0 <= microssegundos <1000000
#          0 <= segundos <3600 * 24 (o número de segundos em um dia)
#          -999999999 <= dias <= 999999999

# datetime.timedelta.min
# O objeto timedelta mais negativo, timedelta (-999999999).

# datetime.timedelta.max
# O objeto timedelta mais positivo, timedelta (dias = 999999999, horas = 23, minutos = 59, segundos = 59, 
# microssegundos = 999999).

# datetime.timedelta.resolution
# A menor diferença possível entre objetos timedelta não iguais, timedelta (microssegundos = 1).

# Observe que, devido à normalização, timedelta.max> -timedelta.min. -timedelta.max não é representável 
# como um objeto timedelta.

# Operacoes:
# t1 = t2 + t3
# t1 = t2 - t3
# t1 = t2 * i or t1 = i * t2
# t1 = t2 * f or t1 = f * t2
# f = t2 / t3
# t1 = t2 / f or t1 = t2 / i
# t1 = t2 // i or t1 = t2 // t3
# t1 = t2 % t3
# q, r = divmod(t1, t2)
# +t1
# -t1
# abs(t)
# str(t)
# repr(t)
	
# datetime.timedelta.total_seconds()
# Retorne o número total de segundos contidos na duração. 
# Equivalente a td / timedelta (segundos = 1). 
# Para unidades de intervalo diferentes de segundos, 
# use o formulário de divisão diretamente (por exemplo, td / timedelta (microssegundos = 1)).
# Observe que, por intervalos de tempo muito grandes (mais de 270 anos na maioria das plataformas), 
# esse método perde a precisão de microssegundos.

#==================================================================================================
# class datetime.tzinfo
# Uma classe base abstrata para objetos de informacoes de fuso horario. Eles sao usados
# pelas classes de data e hora para fornecer uma nocao personalizavel de ajuste de horario
# (por exemplo, para considerar o fuso horario e / ou o horario de verao).

#==================================================================================================
# class datetime.timezone
# Uma classe que implementa a classe base abstrata tzinfo como um deslocamento fixo do UTC.
