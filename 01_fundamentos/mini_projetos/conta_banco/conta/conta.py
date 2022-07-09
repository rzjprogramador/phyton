from helpers.messages import StaticMSG

class ContaBanco:
  __saldo = 0

  def stateSaldo(self, valor: float) -> str:
    if valor < 0:
      return f'{StaticMSG.FAIL} seu saldo esta NEGATIVO com {self.__saldo}'
    return f'{StaticMSG.OK} seu saldo esta POSITIVO com {self.__saldo}'

  def mostrarSaldo(self):
    return self.stateSaldo(self.__saldo)

  def depositarSaldo(self, valor: float):
    newSaldo = self.__saldo + valor
    self.__saldo = newSaldo
    return newSaldo

  def sacarSaldo(self, valor: float):
    self.__saldo = self.__saldo - valor

  
