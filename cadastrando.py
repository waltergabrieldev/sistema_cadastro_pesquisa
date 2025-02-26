import json
import random
def cadastro(dados):
    dicionario_de_cadastrados = {}
    id = random.randint(100000, 999999)
    with open("banco_de_dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())
    dicionario_de_cadastrados[id] = dados
    dicionario_de_cadastrados = json.dumps(dicionario_de_cadastrados)
    with open("banco_de_dados.json", 'w+') as file:
        file.write(dicionario_de_cadastrados)



