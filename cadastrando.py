import json

def cadastro(lista):
    dicionario_de_cadastrados = {}
    with open("dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())
        id = int(list(dicionario_de_cadastrados.keys())[-1])
        id = str(id + 1).zfill(6)
    dicionario_de_cadastrados[id] = {"nome" : lista[0] , "cpf" : lista[1], "telefone" : lista[2]}
    dicionario_de_cadastrados = json.dumps(dicionario_de_cadastrados, indent = 3)
    with open("dados.json", 'w+') as file:
        file.write(dicionario_de_cadastrados)
    print("cadastro finalizado com sucesso!")


def coferindo_cpf_existentes(cpf):
    with open("dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())

    verifica_cpf = [id for id, info in dicionario_de_cadastrados.items() if info["cpf"] == cpf]    
    if verifica_cpf:
        existente_no_sistema = False
    elif not verifica_cpf :
        existente_no_sistema = True
    return existente_no_sistema
    
    
def coferindo_telefone_existentes(telefone):
    with open("dados.json", "r+") as file:
        file.seek(0)
        dicionario_de_cadastrados = json.loads(file.read())

    verifica_telefone = [id for id, info in dicionario_de_cadastrados.items() if info["telefone"] == telefone]    
    if verifica_telefone:
        existente_no_sistema = False
    elif not verifica_telefone :
        existente_no_sistema = True
    return existente_no_sistema
    
    
def verificando_telefone(telefone):
    ddds_brasil = [
    "11", "12", "13", "14", "15", "16", "17", "18", "19","21", "22", "24", "27", "28",  "31", "32", "33", "34", "35", "37", "38",  "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55",  "61",  "62", "64",  "63", "65", "66", "67", "68", "69",  "71", "73", "74", "75", "77", "79", "81", "87", "82", "83", "84", "85", "88", "86", "89","91", "93", "94", "92", "97", "95", "96", "98", "99"] 
    ddd_telefone_cliente = telefone[:2]
    
    if ddd_telefone_cliente not in ddds_brasil:
        return False
    else:
        if len(telefone) != 11 :
            return False
        else:
            return True
    