#!python3
from modules.conta import ContaBanco

# USO DA CLASSE - INVOCACAO INSTANCIAMENTO
c1 = ContaBanco()

# USO DA INSTANCIA - ACOES DA INSTANCIA
# print(c1.saldo)
# c1.__saldo = 1000 # ERRO TENTANDO MANIPULAR DIRETAMENTE A PROP
#  COMO A PROP É PRIVADA NAO CONSIGO MANIPULA-LA DIRETAMENTE SÓ POR METODO
c1.depositarSaldo(200)
c1.sacarSaldo(20000)

# VER SALDO FINAL
print(c1.mostrarSaldo())