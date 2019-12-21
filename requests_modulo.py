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
