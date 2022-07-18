from pydantic import validate_arguments
from typing import union

@validate_arguments
def soma(a: int, b: int) -> int:
  return a + b

StrInt = union[str, int]

def uni(a: StrInt, b: StrInt):
  return a + b


# print(soma(10, 20))
print(uni('aaaa', 'aa'))