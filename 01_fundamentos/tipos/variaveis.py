
comentarioEmVariavel = """ 
  atribui um comentario em variavel de valor string
"""

a = 3
b = 4

texto = 'Sua idade é ... '
idade = 44

raio = input('Informe o raio da circuferencia: ')

# print(3 * 'bom dia...') # multiplicando valores de variaveis
# print(4 * texto) # repetindo valores de variaveis com operacao matematica

# print(f'{texto} {idade}') # melhor forma usar FString : para fazer interpolacao mostrar variaveis na string
# print(texto + str(idade)) # concatenar variaeis diferentes é fazendo casting convertendo o tipo

# print(texto + idade) # vai gerar erro: TypeError: can only concatenate str (not "int") to str :: porque ele nao concatena variaveis de tipos diferentes ex: string e numero

# print(a + b)

# print(comentarioEmVariavel)