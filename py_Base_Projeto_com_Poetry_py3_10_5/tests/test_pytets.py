from projeto_base_poetry.brincadeira import brincadeira

def test_meu_primeiro_test():
  assert True

def quando_brincadeira_receber_1_retorna_1():
  entrada = 1
  esperado = 1
  resultado = brincadeira(entrada)

  assert resultado == esperado
