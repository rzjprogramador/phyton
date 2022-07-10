from model.cliente import Cliente
from connect.connect import inserir, mostrarTodos


# USAR ### OBS: TUDO QUE FOR FEITO NA FUNCAO MAIN É SÓ UMA PREVIA --> SERA FEITO NO FRONT VIEW 

def main():
  # print(c1.CPF)

  # CRIAR OBJETO
  # admin = Cliente(111, 'admin', '22091977')
  # reinaldo = Cliente(222, 'REINALDO', '22091977')
  # especial = Cliente(333, 'irãêí', '22091977')

  # USAR FUNCOES PARA O OBJETO
  # inserir(admin)
  # inserir(reinaldo)
  # inserir(especial)

  # MOSTRAR 
  # print(mostrarTodos()) # PARA MOSTRAR NO CONSOLE DA UM PRINT()

  # MOSTRAR LINHA A LINHA
  todos = mostrarTodos()
  for i in todos:
    print(i)

main()

"""
#  OBS: AO RODAR ESTE ARQUIVO MAIN - 
# VAI RODAR TODO PROJETO >> GERAR E EDITAR O JSON COM DADOS GERADO NA RAIZ DO PROJETO
# OBS: A BASE DE DADOS JSON GRAVA DIFERENCIADO OS CARACTERES ESPECIAIS ..MAS MOSTRA NORMAL
"""