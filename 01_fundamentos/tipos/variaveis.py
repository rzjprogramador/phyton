
comentarioEmVariavel = """ 
  atribui um comentario em variavel de valor string
"""

a = 3
b = 4

texto = 'Sua idade é ... '
idade = 44



print(texto + str(idade)) # modo certo concatenar variaeis diferentes é fazendo casting convertendo o tipo

# print(texto + idade) # vai gerar erro: TypeError: can only concatenate str (not "int") to str :: porque ele nao concatena variaveis de tipos diferentes ex: string e numero

# print(a + b)

# print(comentarioEmVariavel)