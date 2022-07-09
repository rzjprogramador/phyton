#!python3

class ContaBanco:
  __saldo = 0
 
  def mostrarSaldo(self):
    if self.__saldo < 0:
      return f'OPS! Voce esta com saldo negativo de {self.__saldo}'
    return self.__saldo

  def depositarSaldo(self, valor: float):
    newSaldo = self.__saldo + valor
    self.__saldo = newSaldo
    return newSaldo

  def sacarSaldo(self, valor: float):
    self.__saldo = self.__saldo - valor
