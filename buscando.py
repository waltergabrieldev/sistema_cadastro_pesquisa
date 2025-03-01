import json
def procurando_cpf(cpf):
    cpf = (cpf.replace('.','').replace('-',''))
    with open("banco_de_dados.json", "r+") as file:
            file.seek(0)
            dicionario_de_cadastrados = json.loads(file.read())
    cpf_procurado = cpf
    id_busca_cpf = [id for id, info in dicionario_de_cadastrados.items() if info["cpf"] == cpf_procurado]       
    for chaves, valores in dicionario_de_cadastrados[id_busca_cpf[0]].items():
        print(f"{chaves} : {valores}")
        
        
def procurando_por_id(id):
    with open("banco_de_dados.json", "r+") as file:
            file.seek(0)
            dicionario_de_cadastrados = json.loads(file.read())
    for chaves, valores in dicionario_de_cadastrados[id].items():
        print(f"{chaves} : {valores}")
            
    