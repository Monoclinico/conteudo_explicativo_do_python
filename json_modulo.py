# JSON significa JavaScript Object Notation

# ======================== Metodos ========================

# ------------ json.dump ------------------
# escreve um objeto JSON em um arquivo

# json.dump(
#   obj, -> ojeto em formato de json ou dicionario.
#   fp, -> arquivo de escrita ou destino
#   *, -> outros destinos
#   skipkeys=False, -> Se skipkeys for true (padrao: False), as teclas dict que nao sao de um tipo basico 
#     (str, int, float, bool, None) serao ignoradas em vez de gerar um TypeError.
#   ensure_ascii=True, -> Se sure_ascii for true (o padrao), e garantido que a saída tenha todos os 
#     caracteres nao ASCII de entrada escapados. Se sure_ascii for false, 
#     esses caracteres serao exibidos como estao.
#   check_circular=True, -> Se check_circular for false (padrao: True), a verificacao de referencia 
#     circular para tipos de conteiner sera ignorada e uma referencia circular resultara 
#     em um OverflowError (ou pior).
#   allow_nan=True, -> Se allow_nan for false (padrao: True), sera um ValueError serializar valores 
#     flutuantes fora do intervalo (nan, inf, -inf) em estrita conformidade com a especificacao JSON. 
#     Se allow_nan for true, seus equivalentes JavaScript (NaN, Infinity, -Infinity) serao usados.
#   cls=None, -> 
#   indent=None, -> Se o recuo for um numero inteiro ou sequencia nao negativa, 
#     os elementos da matriz JSON e os membros do objeto serao impressos com esse nível de recuo. 
#     Um nível de recuo de 0, negativo ou "" inserira apenas novas linhas. 
#     Nenhum (o padrao) seleciona a representacao mais compacta. 
#     O uso de um recuo inteiro positivo indenta muitos espacos por nível. 
#     Se recuar for uma sequencia (como "\ t"), essa sequencia sera usada para recuar cada nível.
#   separators=None, ->  Se especificado, os separadores devem ser uma tupla 
#     (item_separator, key_separator). O padrao e (',', ':') se o indent for None e (',', ':') 
#     caso contrario. Para obter a representacao JSON mais compacta, voce deve especificar (',', ':') 
#     para eliminar o espaco em branco.
#   default=None, -> Se especificado, o padrao deve ser uma funcao que e chamada para objetos que nao 
#     poderiam ser serializados. Ele deve retornar uma versao codificada em JSON do objeto ou gerar
#     um TypeError. Se nao especificado, TypeError e gerado.
#   sort_keys=False, -> Se sort_keys for true (padrao: False), a saída dos dicionarios sera classificada por chave.
#     Para usar uma subclasse JSONEncoder customizada (por exemplo, uma que substitui o metodo default () para serializar tipos adicionais),
#     especifique-a com o cls kwarg; caso contrario, JSONEncoder e usado.
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
#   object_hook=None, -> object_hook e uma funcao opcional que sera chamada com o resultado de qualquer 
#     objeto literal decodificado (um ditado). O valor de retorno de object_hook sera usado em vez do 
#     dict. Esse recurso pode ser usado para implementar decodificadores personalizados (por exemplo, 
#     dicas de classe JSON-RPC).
#   parse_float=None, -> parse_float, se especificado, sera chamado com a sequencia de todos os flutuadores
#      JSON a serem decodificados. Por padrao, isso e equivalente a float (num_str). 
#      Isso pode ser usado para usar outro tipo de dados ou analisador para flutuadores JSON 
#      (por exemplo, decimal.Decimal).
#   parse_int=None, -> parse_int, se especificado, sera chamado com a cadeia de caracteres de cada 
#     JSON int a ser decodificado. Por padrao, isso e equivalente a int (num_str). 
#     Isso pode ser usado para usar outro tipo de dados ou analisador para numeros inteiros JSON 
#     (por exemplo, float).
#   parse_constant=None, -> parse_constant, se especificado, sera chamado com uma das seguintes 
#     cadeias de caracteres: '-Infinity', 'Infinity', 'NaN'. Isso pode ser usado para gerar uma 
#     excecao se forem encontrados numeros JSON invalidos.
#   object_pairs_hook=None, -> object_pairs_hook e uma funcao opcional que sera chamada com o 
#     resultado de qualquer objeto literal decodificado com uma lista ordenada de pares. 
#     O valor de retorno de object_pairs_hook sera usado em vez do dict. 
#     Esse recurso pode ser usado para implementar decodificadores personalizados. 
#     Se object_hook tambem estiver definido, o object_pairs_hook tera prioridade.
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