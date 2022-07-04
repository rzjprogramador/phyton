# criar tupla :: obs ao inves de colchetes o delimitador sao parenteses ()
# obs: os dados nas tuplas sao imutaveis, nao é possivel adicionar item nem editar os ja existentes

# -----------------------/*    */-----------------------
# 
nomes = ('Reinaldo', 'Renata', 'Gustavo')

# ----------------------------------------------------------------------------
# PRINTS CONSOLE
print('reinaldo' in nomes) 
# vai retornar False porque o item na tupla comeca com letra Maiuscula é case sensitive o operador in tem que passar exatamente a pesquisa

# ----------------------------------------------------------------------------

# acessar item na tupla pelo indice posicao
# print(nomes[1]) # 'Renata'

# ----------------------------------------------------------------------------

# acessando pela posicao intercalada no exemplo abaixo da posicao 1 ao 3 entao seria do 2º ao 3º item
print(nomes[1:3]) # ('Renata', 'Gustavo')


# -----------------------/*    */-----------------------
# 
# obs: quando se acessa pela posicao somente 1 item o py adiciona virgula no final para diferenciar que é uma tupla e nao um type string
# exemplo:
x = ('Bia')
t = ('Bia',)
# -----------------------/*    */-----------------------
# 
print(f'O tipo de pesquisa unica sem virgula é string - confira:: {type(x)}')
print(f'O tipo de pesquisa unica se ADICIONAR virgula apos o item é tuple - confira:: {type(t)}')

# -----------------------/*    */-----------------------
# 
print(type(nomes))
print(nomes)