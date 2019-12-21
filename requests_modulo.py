# Requests é uma biblioteca HTTP para Python simples e elegante, feita para seres humanos. 

import requests

# =================== METODOS ====================================

# GET ----------------------------------------
# O método HTTP GET solicita uma representação do recurso especificado. Solicitações usando GET só devem recuperar dados
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
# O método POST é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.
# requests.post
# post(url, data=None, json=None, headers: Optional[MutableMapping[Text, Text]]=..., 
# cookies: Union[None, RequestsCookieJar, MutableMapping[Text, Text]]=..., files: Optional[MutableMapping[Text, IO]]=..., 
# auth: Union[None, Tuple[Text, Text], _auth.AuthBase, Callable[[Request], Request]]=..., 
# timeout: Union[None, float, Tuple[float, float]]=..., allow_redirects: Optional[bool]=..., 
# proxies: Optional[MutableMapping[Text, Text]]=..., hooks: Optional[_HooksInput]=..., stream: Optional[bool]=..., 
# verify: Union[None, bool, Text]=..., cert: Union[Text, Tuple[Text, Text], None]=...)

# PUT ----------------------------------------
# O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.
# requests.put()

# PATCH ----------------------------------------
# O método PATCH é utilizado para aplicar modificações parciais em um recurso.
# requests.patch()

# DELETE ----------------------------------------
# O método DELETE remove um recurso específico.
# requests.delete()

# HEAD ----------------------------------------
# O método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.
# requests.head()

# OPTIONS ----------------------------------------
# O método OPTIONS é usado para descrever as opções de comunicação com o recurso de destino.
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
#     Ocorreu uma exceção ambígua ao lidar com sua solicitação.

# exception requests.ConnectionError(*args, **kwargs)[source]
#     Ocorreu um erro de conexão.

# exception requests.HTTPError(*args, **kwargs)[source]
#     Ocorreu um erro HTTP.

# exception requests.URLRequired(*args, **kwargs)[source]
#     É necessário um URL válido para fazer uma solicitação.

# exception requests.TooManyRedirects(*args, **kwargs)[source]
#     Muitos redirecionamentos.

# exception requests.ConnectTimeout(*args, **kwargs)[source]
#     A solicitação expirou ao tentar conectar-se ao servidor remoto.
#     É possível tentar novamente as solicitações que produziram esse erro.

# exception requests.ReadTimeout(*args, **kwargs)[source]
#     O servidor não enviou nenhum dado no período alocado.

# exception requests.Timeout(*args, **kwargs)[source]
#     O pedido excedeu o tempo limite.
#     A captura desse erro captura os erros ConnectTimeout e ReadTimeout.

# ========================== RESPONSE =================================
# class requests.Response[source]
# O objeto Response, que contém a resposta de um servidor a uma solicitação HTTP.

#Exemplo:
resposta = requests.get("https://github.com/timeline.json")

#A codificação aparente, fornecida pela biblioteca chardet.
print(resposta.apparent_encoding) # utf-8

# Conteúdo da resposta, em bytes.
print(resposta.content) # b'abcd...'

# Um pote de cookies que o servidor enviou de volta.
cookie_da_resposta = resposta.cookies
print(cookie_da_resposta.items())

# A quantidade de tempo decorrido entre o envio da solicitação e a chegada da resposta (como um intervalo de tempo). 
# Essa propriedade mede especificamente o tempo gasto entre o envio do primeiro byte da solicitação e 
# o término da análise dos cabeçalhos. Portanto, não é afetado pelo consumo do conteúdo da resposta ou 
# do valor do argumento da palavra-chave stream.
print(resposta.elapsed)

# Codificação para decodificar ao acessar r.text.
print(resposta.encoding) # utf-8

# Dicionário que diferencia maiúsculas de minúsculas de cabeçalhos de resposta.
#  Por exemplo, os cabeçalhos ['content-encoding'] retornarão o valor de um cabeçalho de resposta 'Content-Encoding'.
print(resposta.headers)

# Uma lista de objetos de resposta do histórico da solicitação. Qualquer resposta de redirecionamento terminará aqui. 
# A lista é classificada da solicitação mais antiga à mais recente.
print(resposta.history)

# Verdadeiro se esta resposta for uma das versões permanentes do redirecionamento.
print(resposta.is_permanent_redirect)

# Verdadeiro se esta resposta for um redirecionamento HTTP bem formado que poderia ter sido processado automaticamente 
# (por Session.resolve_redirects).
print(resposta.is_redirect)

# Repete os dados da resposta. Quando stream = True é definido na solicitação, isso evita a leitura do conteúdo de uma vez na memória para respostas grandes.
# O tamanho do pedaço é o número de bytes que ele deve ler na memória. Esse não é necessariamente o comprimento de cada item retornado, pois a decodificação pode ocorrer.
# chunk_size deve ser do tipo int ou None. Um valor Nenhum funcionará de maneira diferente, dependendo do valor do fluxo. 
# stream = True lerá os dados conforme eles chegarem em qualquer tamanho que os pedaços forem recebidos. Se stream = False, os dados são retornados como um único pedaço.
# Se decode_unicode for True, o conteúdo será decodificado usando a melhor codificação disponível com base na resposta.
dados_resposta = resposta.iter_content(chunk_size=20,decode_unicode=True)
print(next(dados_resposta))
print(next(dados_resposta))

# Repete os dados da resposta, uma linha de cada vez. Quando stream = True é definido na solicitação, isso evita a leitura do conteúdo de uma vez na memória para respostas grandes.
# Nota:Este método não é seguro para reentrada.
dados_linhas_resposta = resposta.iter_lines(chunk_size=512,decode_unicode=True,delimiter="|")
print(next(dados_linhas_resposta))

# Retorna o conteúdo codificado por json de uma resposta, se houver.
# Parâmetros: ** kwargs - argumentos opcionais que o json.loads utiliza.
# Gera: ValueError - Se o corpo da resposta não contiver json válido.
print(resposta.json())

# Retorna os links de cabeçalho analisados da resposta, se houver.
print(resposta.links)

# Retorna um PreparedRequest para a próxima solicitação em uma cadeia de redirecionamento, se houver uma.
proxima_resposta = resposta.next
print(proxima_resposta)

# Retorna True se status_code for menor que 400; False, se não.

# Este atributo verifica se o código de status da resposta está entre 400 e 600 para ver se houve um erro do 
# cliente ou um erro do servidor. Se o código de status estiver entre 200 e 400, isso retornará True. 
# Esta não é uma verificação para ver se o código de resposta está 200 OK.
print(resposta.ok)

# Representação de resposta de objeto semelhante a arquivo (para uso avançado).
# O uso de raw requer que stream = True seja definido na solicitação. 
# Este requisito não se aplica para uso interno em Solicitações.
print(resposta.raw)

# Motivo textual do status HTTP respondido, p. "Não encontrado" ou "OK".
print(resposta.reason)

# O objeto PreparedRequest ao qual esta é uma resposta.
print(resposta.request)

# Código inteiro do status HTTP respondido, por exemplo 404 ou 200.
print(resposta.status_code)

# Conteúdo da resposta, em unicode.
# Se Response.encoding for None, a codificação será adivinhada usando chardet.
# A codificação do conteúdo da resposta é determinada com base apenas nos cabeçalhos HTTP, seguindo a RFC 2616 à letra. 
# Se você puder tirar proveito do conhecimento não HTTP para adivinhar melhor a codificação, 
# defina r.encoding apropriadamente antes de acessar esta propriedade.
print(resposta.text)

# Local final do URL da resposta.
print(resposta.url)

# Libera a conexão de volta ao pool. Depois que esse método for chamado, 
# o objeto bruto subjacente não deverá ser acessado novamente.
# Nota: Normalmente, não precisa ser chamado explicitamente.
resposta.close()

# Gera HTTPError armazenado, se um ocorreu.
resposta.raise_for_status()
