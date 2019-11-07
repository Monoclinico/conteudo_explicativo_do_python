# The key function for working with files in Python is the open() function.
# A funcao chave para trabalhar com arquivos no Python e open().

# The open() function takes two parameters; filename, and mode.
# A funcao open() tem dois parametros: nome do arquivo e modo.  

# There are four different methods (modes) for opening a file:
# Ha quatro diferentes metodos (modos) para abrir um aquivo:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# "r" - Ler - Valor padrao. Abre um arquivo  para leitura, retorna um erro se o arquivo nao existir.

# "a" - Append - Opens a file for appending, creates the file if it does not exist.
# "a" - Acrescentar - Abre um arquivo para acrescentar algo no final, cria o arquivo se ele nao existtir.

# "w" - Write - Opens a file for writing, creates the file if it does not exist.
# "w" - Escrever - Abre um arquivo para escrever, cria o arquivo se ele nao existir. 

# "x" - Create - Creates the specified file, returns an error if the file exists.
# "x" - Criar - Cria o arquivo especifico, retorna um erro se o arquivo existir.

# "+" - open for updating (reading and writing)
# "+" - aberto para atualização (leitura e escrita)

# In addition you can specify if the file should be handled as binary or text mode.

# "t" - Text - Default value. Text mode.
# "t" - Texto - Valor padrao. Modo texto.

# "b" - Binary - Binary mode (e.g. images).
# "b" - Binario - Modo binario (e.g. imagens).

# file = "arquivo.txt" 
# arquivo = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# com escopo anonimo
# with open(file, mode="r") as arquivo:
#   arquivo.close()