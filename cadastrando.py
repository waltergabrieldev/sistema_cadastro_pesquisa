import json

def cadastro(lista):
    dicionario_de_cadastrados = {}
    with open("banco_de_dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())
        id = int(list(dicionario_de_cadastrados.keys())[-1])
        id = str(id + 1).zfill(6)
    dicionario_de_cadastrados[id] = {"nome" : lista[0] , "cpf" : lista[1], "telefone" : lista[2]}
    dicionario_de_cadastrados = json.dumps(dicionario_de_cadastrados, indent = 3)
    with open("banco_de_dados.json", 'w+') as file:
        file.write(dicionario_de_cadastrados)
    print("cadastro finalizado com sucesso!")

def coferindo_cpf_existentes(cpf):
    with open("banco_de_dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())

    verifica_cpf = [id for id, info in dicionario_de_cadastrados.items() if info["cpf"] == cpf]    
    if verifica_cpf:
        existente_no_sistema = False
    elif not verifica_cpf :
        existente_no_sistema = True
    return existente_no_sistema
    
def coferindo_telefone_existentes(telefone):
    with open("banco_de_dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())

    verifica_telefone = [id for id, info in dicionario_de_cadastrados.items() if info["telefone"] == telefone]    
    if verifica_telefone:
        existente_no_sistema = False
    elif not verifica_telefone :
        existente_no_sistema = True
    return existente_no_sistema
    
