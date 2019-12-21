# JSON significa JavaScript Object Notation

# ======================== Metodos ========================

# ------------ json.dump ------------------
# escreve um objeto JSON em um arquivo

# json.dump(
#   obj, -> ojeto em formato de json ou dicionario.
#   fp, -> arquivo de escrita ou destino
#   *, -> outros destinos
#   skipkeys=False, -> Se skipkeys for true (padrão: False), as teclas dict que não são de um tipo básico 
#     (str, int, float, bool, None) serão ignoradas em vez de gerar um TypeError.
#   ensure_ascii=True, -> Se sure_ascii for true (o padrão), é garantido que a saída tenha todos os 
#     caracteres não ASCII de entrada escapados. Se sure_ascii for false, 
#     esses caracteres serão exibidos como estão.
#   check_circular=True, -> Se check_circular for false (padrão: True), a verificação de referência 
#     circular para tipos de contêiner será ignorada e uma referência circular resultará 
#     em um OverflowError (ou pior).
#   allow_nan=True, -> Se allow_nan for false (padrão: True), será um ValueError serializar valores 
#     flutuantes fora do intervalo (nan, inf, -inf) em estrita conformidade com a especificação JSON. 
#     Se allow_nan for true, seus equivalentes JavaScript (NaN, Infinity, -Infinity) serão usados.
#   cls=None, -> 
#   indent=None, -> Se o recuo for um número inteiro ou sequência não negativa, 
#     os elementos da matriz JSON e os membros do objeto serão impressos com esse nível de recuo. 
#     Um nível de recuo de 0, negativo ou "" inserirá apenas novas linhas. 
#     Nenhum (o padrão) seleciona a representação mais compacta. 
#     O uso de um recuo inteiro positivo indenta muitos espaços por nível. 
#     Se recuar for uma sequência (como "\ t"), essa sequência será usada para recuar cada nível.
#   separators=None, ->  Se especificado, os separadores devem ser uma tupla 
#     (item_separator, key_separator). O padrão é (',', ':') se o indent for None e (',', ':') 
#     caso contrário. Para obter a representação JSON mais compacta, você deve especificar (',', ':') 
#     para eliminar o espaço em branco.
#   default=None, -> Se especificado, o padrão deve ser uma função que é chamada para objetos que não 
#     poderiam ser serializados. Ele deve retornar uma versão codificada em JSON do objeto ou gerar
#     um TypeError. Se não especificado, TypeError é gerado.
#   sort_keys=False, -> Se sort_keys for true (padrão: False), a saída dos dicionários será classificada por chave.
#     Para usar uma subclasse JSONEncoder customizada (por exemplo, uma que substitui o método default () para serializar tipos adicionais),
#     especifique-a com o cls kwarg; caso contrário, JSONEncoder é usado.
#   **kw ->
# )

#Exemplo:
import json
arquivo_json = open("arquivo_json.json","w")
dispositivo = {"tipo":"notebook","SO":{"SO":True,"windows":10,"linux":"ubuntu"},"HD":"1TB","ram":"8GB","cor":"preto","CD-DVD":None}
json.dump(dispositivo,arquivo_json,skipkeys=True,allow_nan=True,indent=2,separators=(",",":"))

#----------- json.dumps -------------
# Faz o mesmo que json.dump, mas retorna uma string

#Exemplo:
notebook = json.dumps(dispositivo,skipkeys=True,allow_nan=True,indent=2,separators=(",",":"))
print(notebook)
arquivo_json.close()

#------------- json.load ------------------
# retorna um objeto JSON/dicionario de um arquivo que tem algum JSON
#  json.load(
#   fp, -> Arquivo ou origem do objeto JSON
#   *, 
#   cls=None, ->
#   object_hook=None, -> object_hook é uma função opcional que será chamada com o resultado de qualquer 
#     objeto literal decodificado (um ditado). O valor de retorno de object_hook será usado em vez do 
#     dict. Esse recurso pode ser usado para implementar decodificadores personalizados (por exemplo, 
#     dicas de classe JSON-RPC).
#   parse_float=None, -> parse_float, se especificado, será chamado com a sequência de todos os flutuadores
#      JSON a serem decodificados. Por padrão, isso é equivalente a float (num_str). 
#      Isso pode ser usado para usar outro tipo de dados ou analisador para flutuadores JSON 
#      (por exemplo, decimal.Decimal).
#   parse_int=None, -> parse_int, se especificado, será chamado com a cadeia de caracteres de cada 
#     JSON int a ser decodificado. Por padrão, isso é equivalente a int (num_str). 
#     Isso pode ser usado para usar outro tipo de dados ou analisador para números inteiros JSON 
#     (por exemplo, float).
#   parse_constant=None, -> parse_constant, se especificado, será chamado com uma das seguintes 
#     cadeias de caracteres: '-Infinity', 'Infinity', 'NaN'. Isso pode ser usado para gerar uma 
#     exceção se forem encontrados números JSON inválidos.
#   object_pairs_hook=None, -> object_pairs_hook é uma função opcional que será chamada com o 
#     resultado de qualquer objeto literal decodificado com uma lista ordenada de pares. 
#     O valor de retorno de object_pairs_hook será usado em vez do dict. 
#     Esse recurso pode ser usado para implementar decodificadores personalizados. 
#     Se object_hook também estiver definido, o object_pairs_hook terá prioridade.
#   **kw ->
# )

#Exemplo:
arquivo_json = open("arquivo_json.json","r")
objeto_notebook = json.load(arquivo_json)
print(objeto_notebook["SO"]) # {'SO': True, 'windows': 10, 'linux': 'ubuntu'}
arquivo_json.close()

#--------------- json.loads --------------
# Transforma uma string em um objeto JSON/dicionario 
# Tem os mesmos parametros que json.load, mas muda o primeiro

#Exemplo:
arvore = '{"nome":"mangueira","fruto":"manga"}'
arvore_json = json.loads(arvore)
print(arvore_json["fruto"]) #manga