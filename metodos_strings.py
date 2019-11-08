#Metodos de string

# capitalize() Converts the first character to upper case.
# capitalize() Converte o primeiro caractere para maiusculo.
palavra = "supressor"
print(palavra.capitalize()) # Supressor

# casefold() Converts string into lower case.
# casefold() Converte a string para minusculo, de maneira a encontrar mais correspondências ao 
# comparar duas strings e ambas são convertidas usando o casefold().
palavra = "PÃo"
print(palavra.casefold()) # pão

# center() Returns a centered string.
# center(<comprimento total>,<caractere preenchedor>) Retorna um string centralizada junto a caracteres.
palavra = "centro"
print(palavra.center(10,"=")) # ==centro==

# count()	Returns the number of times a specified value occurs in a string.
# count(<string>, inicio, fim) Retorna o numero de vezes que um valor especificado ocorreu na string.
palavra = "banana"
print(palavra.count("a",0)) # 3

# encode() Returns an encoded version of the string.
# encode(encoding: Text=..., errors: Text=...) Retorna uma vesao codificada da string.
# 'backslashreplace'	- uses a backslash instead of the character that could not be encoded.
# 'ignore'	- ignores the characters that cannot be encoded.
# 'namereplace'	- replaces the character with a text explaining the character.
# 'strict'	- Default, raises an error on failure.
# 'replace'	- replaces the character with a questionmark.
# 'xmlcharrefreplace'	- replaces the character with an xml character.
txt = "O 1º é o vencedor."
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# endswith() Returns true if the string ends with the specified value.
# endswith(suffix: Union[Text, Tuple[Text, ...]], start: Optional[int]=..., end: Optional[int]=...) 
# Retorna True se a string termina com o valor especificado.
palavra = "macaco"
print(palavra.endswith("o")) # True

# expandtabs() Sets the tab size of the string.
# expandtabs() Define o tamanho da tabulacao em um string.
palavra = "casa:\tR$352.112,00"
print(palavra.expandtabs(0)) #casa:R$352.112,00
print(palavra.expandtabs(2)) #casa: R$352.112,00"
print(palavra.expandtabs(4)) #casa:   R$352.112,00"

# find() Searches the string for a specified value and returns the position of where it was found.
# find(sub: Text, start: Optional[int]=..., end: Optional[int]=...) 
# Pesquisa a string com o valor especificado e retorna o indice da primeira ocorrencia.
# Retorna -1 se nada for encontrado.
palavra = "hamburguer"
print(palavra.find("a")) # 1
print(palavra.find("u")) # 4

# format() Formats specified values in a string.
# format(*args: Any, **kwargs: Any) Formata valores especificos na string.
print("{0} + {1}.5 = {2:.1f}".format(1,2,3.5))
print("{0} + {1}.5 = {2:.1f}".format(*[1,2,3.5]))
print("{um} + {dois}.5 = {trespontocinco:.1f}".format(**{"um":1,"dois":2,"trespontocinco":3.5}))

# format_map() Formats specified values in a string.
# format_map(map: Mapping[str, Any]) Formata valores especificos na string.
print("{um}".format_map({"um":1})) # 1

# index()	Searches the string for a specified value and returns the position of where it was found.
# index() Pesquisa a string com o valor especificado e retorna o indice da primeira ocorrencia. 
# Retorna um erro se nada for encontrado. 
palavra = "hamburguer"
print(palavra.index("a")) # 1
print(palavra.index("u")) # 4

# isalnum()	Returns True if all characters in the string are alphanumeric.
# isalnum() Retorna True se todos os caracteres da string sao alfanumericos (a-z e 0-9).
print("iso9001".isalnum()) # True
print("ISO9001".isalnum()) # True

# isalpha()	Returns True if all characters in the string are in the alphabet.
# isalpha() retorna True se todos os caracteres na string sao do alfabeto (a-z).
print("python".isalpha()) # True
print("Python3".isalpha()) # False

# isdecimal()	Returns True if all characters in the string are decimals.
# isdecimal() retorna True se todos os caracteres na string sao decimais (0-9).
print("5".isdecimal()) # True

# isdigit()	Returns True if all characters in the string are digits.
# isdigit() Retorna True se todos os caracteres na string sao digitos (0-9 e outros).
print("²".isdigit()) # True

# isidentifier() Returns True if the string is an identifier.
# isidentifier() Uma cadeia é considerada um identificador válido se contiver apenas letras alfanuméricas (a-z) e (0-9) ou sublinhados (_). 
# Um identificador válido não pode começar com um número ou conter espaços.
print("bolinha".isidentifier()) # True

# islower()	Returns True if all characters in the string are lower case.

# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning