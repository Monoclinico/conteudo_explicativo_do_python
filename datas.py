#Uma data no Python não é um tipo de dado próprio, 
# mas podemos importar um módulo chamado datetime 
# para trabalhar com datas como objetos de data.

#MODULO DATETIME

import datetime

# O maior número de ano permitido em um objeto de data ou data e hora.
print(datetime.MAXYEAR) 

# O menor número de ano permitido em um objeto de data ou data e hora.
print(datetime.MINYEAR)

# CLASSES:

# class datetime.date
# Uma data ingênua idealizada, assumindo que o atual calendário gregoriano sempre foi 
# e sempre estará em vigor. Atributos: ano, mês e dia.

# class datetime.time
# Um horário ideal, independente de qualquer dia em particular, assumindo que todos os 
# dias tenham exatamente 24 * 60 * 60 segundos. (Não há noção de "segundos bissextos" aqui.) 
# Atributos: hora, minuto, segundo, microssegundo e tzinfo.

# class datetime.datetime
# Uma combinação de uma data e uma hora. Atributos: ano, mês, dia, hora, minuto, segundo,
# microssegundo e tzinfo.

# class datetime.timedelta
# Uma duração que expressa a diferença entre duas instâncias de data, hora ou data e hora
# em resolução de microssegundos.

# class datetime.tzinfo
# Uma classe base abstrata para objetos de informações de fuso horário. Eles são usados 
# pelas classes de data e hora para fornecer uma noção personalizável de ajuste de horário 
# (por exemplo, para considerar o fuso horário e / ou o horário de verão).

# class datetime.timezone
# Uma classe que implementa a classe base abstrata tzinfo como um deslocamento fixo do UTC.
