# Requests e uma biblioteca HTTP para Python simples e elegante, feita para seres humanos. 

import requests

# =================== METODOS ====================================

# GET ----------------------------------------
# O metodo HTTP GET solicita uma representacao do recurso especificado. Solicitacoes usando GET so devem recuperar dados
# requests.get
# get(url, params=None, headers: Optional[MutableMapping[Text, Text]]=..., cookies: Union[None, RequestsCookieJar, 
# MutableMapping[Text, Text]]=..., files: Optional[MutableMapping[Text, IO]]=..., auth: Union[None, Tuple[Text, Text], 
# _auth.AuthBase, Callable[[Request], Request]]=..., timeout: Union[None, float, Tuple[float, float]]=..., 
# allow_redirects: Optional[bool]=..., proxies: Optional[MutableMapping[Text, Text]]=..., 
# hooks: Optional[_HooksInput]=..., stream: Optional[bool]=..., verify: Union[None, bool, Text]=..., 
# cert: Union[Text, Tuple[Text, Text], None]=...)

#Exemplo:
r_get = requests.get('http://github.com/timeline.json',params={"texto":"ola"},timeout=1,allow_redirects=True)

# POST ----------------------------------------
# O metodo POST e utilizado para submeter uma entidade a um recurso especifico, frequentemente causando uma mudanca no estado do recurso ou efeitos colaterais no servidor.
# requests.post
# post(url, data=None, json=None, headers: Optional[MutableMapping[Text, Text]]=..., 
# cookies: Union[None, RequestsCookieJar, MutableMapping[Text, Text]]=..., files: Optional[MutableMapping[Text, IO]]=..., 
# auth: Union[None, Tuple[Text, Text], _auth.AuthBase, Callable[[Request], Request]]=..., 
# timeout: Union[None, float, Tuple[float, float]]=..., allow_redirects: Optional[bool]=..., 
# proxies: Optional[MutableMapping[Text, Text]]=..., hooks: Optional[_HooksInput]=..., stream: Optional[bool]=..., 
# verify: Union[None, bool, Text]=..., cert: Union[Text, Tuple[Text, Text], None]=...)

# PUT ----------------------------------------
# O metodo PUT substitui todas as atuais representacoes do recurso de destino pela carga de dados da requisicao.
# requests.put()

# PATCH ----------------------------------------
# O metodo PATCH e utilizado para aplicar modificacoes parciais em um recurso.
# requests.patch()

# DELETE ----------------------------------------
# O metodo DELETE remove um recurso especifico.
# requests.delete()

# HEAD ----------------------------------------
# O metodo HEAD solicita uma resposta de forma identica ao metodo GET, porem sem conter o corpo da resposta.
# requests.head()

# OPTIONS ----------------------------------------
# O metodo OPTIONS e usado para descrever as opcoes de comunicacao com o recurso de destino.
# requests.options()

#Exemplo:
r_options = requests.options('http://github.com/timeline.json')

# ============================= API ======================================== 
# requests.request(method, url, **kwargs)[source]

#     Constructs and sends a Request.
#     Parameters:	

#         method – method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE.
#         url – URL for the new Request object.
#         params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
#         data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
#         json – (optional) A JSON serializable Python object to send in the body of the Request.
#         headers – (optional) Dictionary of HTTP Headers to send with the Request.
#         cookies – (optional) Dict or CookieJar object to send with the Request.
#         files – (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file.
#         auth – (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
#         timeout (float or tuple) – (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
#         allow_redirects (bool) – (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
#         proxies – (optional) Dictionary mapping protocol to the URL of the proxy.
#         verify – (optional) Either a boolean, in which case it controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
#         stream – (optional) if False, the response content will be immediately downloaded.
#         cert – (optional) if String, path to ssl client cert file (.pem). If Tuple, (‘cert’, ‘key’) pair.

#     Returns:	Response object
#     Return type:	requests.Response

#     Usage:
#     >>> import requests
#     >>> req = requests.request('GET', 'https://httpbin.org/get')
#     >>> req
#     >>> <Response [200]>

# requests.head(url, **kwargs)[source]
#     Sends a HEAD request.
#     Parameters:	
#         url – URL for the new Request object.
#         **kwargs – Optional arguments that request takes. If allow_redirects is not provided, it will be set to False (as opposed to the default request behavior).

# requests.get(url, params=None, **kwargs)[source]
#     Sends a GET request.
#     Parameters:	
#         url – URL for the new Request object.
#         params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
#         **kwargs – Optional arguments that request takes.

# requests.post(url, data=None, json=None, **kwargs)[source]
#     Sends a POST request.
#     Parameters:	
#         url – URL for the new Request object.
#         data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
#         json – (optional) json data to send in the body of the Request.
#         **kwargs – Optional arguments that request takes.

# requests.put(url, data=None, **kwargs)[source]
#     Sends a PUT request.
#     Parameters:	
#         url – URL for the new Request object.
#         data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
#         json – (optional) json data to send in the body of the Request.
#         **kwargs – Optional arguments that request takes.

# requests.patch(url, data=None, **kwargs)[source]
#     Sends a PATCH request.
#     Parameters:	
#         url – URL for the new Request object.
#         data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
#         json – (optional) json data to send in the body of the Request.
#         **kwargs – Optional arguments that request takes.

# requests.delete(url, **kwargs)[source]
#     Sends a DELETE request.
#     Parameters:	
#         url – URL for the new Request object.
#         **kwargs – Optional arguments that request takes.

# requests.options(url, **kwargs)[source]
#     Sends a OPTIONS request.
#     Parameters:	
#         url – URL for the new Request object.
#         **kwargs – Optional arguments that request takes.


# =========================== EXCEPTIONS ===========================

# exception requests.RequestException(*args, **kwargs)[source]
#     Ocorreu uma excecao ambigua ao lidar com sua solicitacao.

# exception requests.ConnectionError(*args, **kwargs)[source]
#     Ocorreu um erro de conexao.

# exception requests.HTTPError(*args, **kwargs)[source]
#     Ocorreu um erro HTTP.

# exception requests.URLRequired(*args, **kwargs)[source]
#     e necessario um URL valido para fazer uma solicitacao.

# exception requests.TooManyRedirects(*args, **kwargs)[source]
#     Muitos redirecionamentos.

# exception requests.ConnectTimeout(*args, **kwargs)[source]
#     A solicitacao expirou ao tentar conectar-se ao servidor remoto.
#     e possivel tentar novamente as solicitacoes que produziram esse erro.

# exception requests.ReadTimeout(*args, **kwargs)[source]
#     O servidor nao enviou nenhum dado no periodo alocado.

# exception requests.Timeout(*args, **kwargs)[source]
#     O pedido excedeu o tempo limite.
#     A captura desse erro captura os erros ConnectTimeout e ReadTimeout.

# ========================== RESPONSE =================================
# class requests.Response[source]
# O objeto Response, que contem a resposta de um servidor a uma solicitacao HTTP.

#Exemplo:
resposta = requests.get("https://github.com/timeline.json")

#A codificacao aparente, fornecida pela biblioteca chardet.
print(resposta.apparent_encoding) # utf-8

# Conteudo da resposta, em bytes.
print(resposta.content) # b'abcd...'

# Um pote de cookies que o servidor enviou de volta.
cookie_da_resposta = resposta.cookies
print(cookie_da_resposta.items())

# A quantidade de tempo decorrido entre o envio da solicitacao e a chegada da resposta (como um intervalo de tempo). 
# Essa propriedade mede especificamente o tempo gasto entre o envio do primeiro byte da solicitacao e 
# o termino da analise dos cabecalhos. Portanto, nao e afetado pelo consumo do conteudo da resposta ou 
# do valor do argumento da palavra-chave stream.
print(resposta.elapsed)

# Codificacao para decodificar ao acessar r.text.
print(resposta.encoding) # utf-8

# Dicionario que diferencia maiusculas de minusculas de cabecalhos de resposta.
#  Por exemplo, os cabecalhos ['content-encoding'] retornarao o valor de um cabecalho de resposta 'Content-Encoding'.
print(resposta.headers)

# Uma lista de objetos de resposta do historico da solicitacao. Qualquer resposta de redirecionamento terminara aqui. 
# A lista e classificada da solicitacao mais antiga a mais recente.
print(resposta.history)

# Verdadeiro se esta resposta for uma das versoes permanentes do redirecionamento.
print(resposta.is_permanent_redirect)

# Verdadeiro se esta resposta for um redirecionamento HTTP bem formado que poderia ter sido processado automaticamente 
# (por Session.resolve_redirects).
print(resposta.is_redirect)

# Repete os dados da resposta. Quando stream = True e definido na solicitacao, isso evita a leitura do conteudo de uma vez na memoria para respostas grandes.
# O tamanho do pedaco e o numero de bytes que ele deve ler na memoria. Esse nao e necessariamente o comprimento de cada item retornado, pois a decodificacao pode ocorrer.
# chunk_size deve ser do tipo int ou None. Um valor Nenhum funcionara de maneira diferente, dependendo do valor do fluxo. 
# stream = True lera os dados conforme eles chegarem em qualquer tamanho que os pedacos forem recebidos. Se stream = False, os dados sao retornados como um unico pedaco.
# Se decode_unicode for True, o conteudo sera decodificado usando a melhor codificacao disponivel com base na resposta.
dados_resposta = resposta.iter_content(chunk_size=20,decode_unicode=True)
print(next(dados_resposta))
print(next(dados_resposta))

# Repete os dados da resposta, uma linha de cada vez. Quando stream = True e definido na solicitacao, isso evita a leitura do conteudo de uma vez na memoria para respostas grandes.
# Nota:Este metodo nao e seguro para reentrada.
dados_linhas_resposta = resposta.iter_lines(chunk_size=512,decode_unicode=True,delimiter="|")
print(next(dados_linhas_resposta))

# Retorna o conteudo codificado por json de uma resposta, se houver.
# Parametros: ** kwargs - argumentos opcionais que o json.loads utiliza.
# Gera: ValueError - Se o corpo da resposta nao contiver json valido.
print(resposta.json())

# Retorna os links de cabecalho analisados da resposta, se houver.
print(resposta.links)

# Retorna um PreparedRequest para a proxima solicitacao em uma cadeia de redirecionamento, se houver uma.
proxima_resposta = resposta.next
print(proxima_resposta)

# Retorna True se status_code for menor que 400; False, se nao.

# Este atributo verifica se o codigo de status da resposta esta entre 400 e 600 para ver se houve um erro do 
# cliente ou um erro do servidor. Se o codigo de status estiver entre 200 e 400, isso retornara True. 
# Esta nao e uma verificacao para ver se o codigo de resposta esta 200 OK.
print(resposta.ok)

# Representacao de resposta de objeto semelhante a arquivo (para uso avancado).
# O uso de raw requer que stream = True seja definido na solicitacao. 
# Este requisito nao se aplica para uso interno em Solicitacoes.
print(resposta.raw)

# Motivo textual do status HTTP respondido, p. "Nao encontrado" ou "OK".
print(resposta.reason)

# O objeto PreparedRequest ao qual esta e uma resposta.
print(resposta.request)

# Codigo inteiro do status HTTP respondido, por exemplo 404 ou 200.
print(resposta.status_code)

# Conteudo da resposta, em unicode.
# Se Response.encoding for None, a codificacao sera adivinhada usando chardet.
# A codificacao do conteudo da resposta e determinada com base apenas nos cabecalhos HTTP, seguindo a RFC 2616 a letra. 
# Se voce puder tirar proveito do conhecimento nao HTTP para adivinhar melhor a codificacao, 
# defina r.encoding apropriadamente antes de acessar esta propriedade.
print(resposta.text)

# Local final do URL da resposta.
print(resposta.url)

# Libera a conexao de volta ao pool. Depois que esse metodo for chamado, 
# o objeto bruto subjacente nao devera ser acessado novamente.
# Nota: Normalmente, nao precisa ser chamado explicitamente.
resposta.close()

# Gera HTTPError armazenado, se um ocorreu.
try:
  resposta.raise_for_status()
except:
  pass

# ==================== CODIGOS DO STATUS DA REQUISICAO ======================

# requests.codes

# O objeto codes define um mapeamento de nomes comuns para status HTTP para seus codigos numericos, 
# acessiveis como atributos ou como itens de dicionario.


    # 100: continue
    # 101: switching_protocols
    # 102: processing
    # 103: checkpoint
    # 122: uri_too_long, request_uri_too_long
    # 200: ok, okay, all_ok, all_okay, all_good, \o/, ✓
    # 201: created
    # 202: accepted
    # 203: non_authoritative_info, non_authoritative_information
    # 204: no_content
    # 205: reset_content, reset
    # 206: partial_content, partial
    # 207: multi_status, multiple_status, multi_stati, multiple_stati
    # 208: already_reported
    # 226: im_used
    # 300: multiple_choices
    # 301: moved_permanently, moved, \o-
    # 302: found
    # 303: see_other, other
    # 304: not_modified
    # 305: use_proxy
    # 306: switch_proxy
    # 307: temporary_redirect, temporary_moved, temporary
    # 308: permanent_redirect, resume_incomplete, resume
    # 400: bad_request, bad
    # 401: unauthorized
    # 402: payment_required, payment
    # 403: forbidden
    # 404: not_found, -o-
    # 405: method_not_allowed, not_allowed
    # 406: not_acceptable
    # 407: proxy_authentication_required, proxy_auth, proxy_authentication
    # 408: request_timeout, timeout
    # 409: conflict
    # 410: gone
    # 411: length_required
    # 412: precondition_failed, precondition
    # 413: request_entity_too_large
    # 414: request_uri_too_large
    # 415: unsupported_media_type, unsupported_media, media_type
    # 416: requested_range_not_satisfiable, requested_range, range_not_satisfiable
    # 417: expectation_failed
    # 418: im_a_teapot, teapot, i_am_a_teapot
    # 421: misdirected_request
    # 422: unprocessable_entity, unprocessable
    # 423: locked
    # 424: failed_dependency, dependency
    # 425: unordered_collection, unordered
    # 426: upgrade_required, upgrade
    # 428: precondition_required, precondition
    # 429: too_many_requests, too_many
    # 431: header_fields_too_large, fields_too_large
    # 444: no_response, none
    # 449: retry_with, retry
    # 450: blocked_by_windows_parental_controls, parental_controls
    # 451: unavailable_for_legal_reasons, legal_reasons
    # 499: client_closed_request
    # 500: internal_server_error, server_error, /o\, ✗
    # 501: not_implemented
    # 502: bad_gateway
    # 503: service_unavailable, unavailable
    # 504: gateway_timeout
    # 505: http_version_not_supported, http_version
    # 506: variant_also_negotiates
    # 507: insufficient_storage
    # 509: bandwidth_limit_exceeded, bandwidth
    # 510: not_extended
    # 511: network_authentication_required, network_auth, network_authentication

#Exemplo:
print(requests.codes['gone']) # 410
