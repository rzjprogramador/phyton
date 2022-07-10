from model.cliente import Cliente
from connect.connect import inserir, mostrarTodos, deletarCliente, atualizarCliente


# USAR ### OBS: TUDO QUE FOR FEITO NA FUNCAO MAIN É SÓ UMA PREVIA --> SERA FEITO NO FRONT VIEW 

def main():
  # print(c1.CPF)

  # CRIAR OBJETO
  admin = Cliente(111, 'adminATUALLLL1', '22091977')
  reinaldo = Cliente(222, 'REINALDOatualllll1', '22091977')
  especial = Cliente(333, 'irãêí', '22091977')

  # USAR FUNCOES PARA O OBJETO
  # inserir(admin)
  # inserir(reinaldo)
  # inserir(especial)

  # DELETAR CLIENTE
  # deletarCliente(111)
  # deletarCliente(1112) # TEST DE FALHA CPF NAO EXISTENTE
  # deletarCliente(222)
  # deletarCliente(333)

  # ATUALIZAR CLIENTE
  # atualizarCliente(admin.CPF, admin)
  # atualizarCliente(222, reinaldo)
  # atualizarCliente(999, reinaldo)  # CASO DE FALHA - CPF NAO EXISTIR

  # MOSTRAR 
  # print(mostrarTodos()) # PARA MOSTRAR NO CONSOLE DA UM PRINT()

  # MOSTRAR LINHA A LINHA
  todos = mostrarTodos()
  # for i in todos:
  #   print(i)

  # mostrar = [x lambda x in todos]
  #   print(mostrar)

main()

"""
#  OBS: AO RODAR ESTE ARQUIVO MAIN - 
# VAI RODAR TODO PROJETO >> GERAR E EDITAR O JSON COM DADOS GERADO NA RAIZ DO PROJETO
# OBS: A BASE DE DADOS JSON GRAVA DIFERENCIADO OS CARACTERES ESPECIAIS ..MAS MOSTRA NORMAL
"""