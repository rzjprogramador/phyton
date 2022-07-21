from odmantic import AIOEngine
from instancias import instances

# CONEXAO COM O BANCO
engine = AIOEngine()

# PERSISTIR AS INSTANCIAS ### EXECUTAR ESTE ARQUIVO
async def save_instances(instances):
  await engine.save_all(instances) 

save_instances(instances)