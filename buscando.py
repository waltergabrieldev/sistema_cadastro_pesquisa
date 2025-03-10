import json
def procurando_cpf(cpf):
        
    with open("dados.json", "r+") as file:
            file.seek(0)
            dicionario_de_cadastrados = json.loads(file.read())
            
    id_busca_cpf = [id for id, info in dicionario_de_cadastrados.items() if info["cpf"] == cpf]
    try:       
        for chaves, valores in dicionario_de_cadastrados[id_busca_cpf[0]].items():
                print(f"{chaves} : {valores}")
    except IndexError:
            print("Esse cpf não está cadastrado no sistema!")    
        
        
def procurando_por_telefone(telefone):
        
    with open("dados.json", "r+") as file:
            file.seek(0)
            dicionario_de_cadastrados = json.loads(file.read())
      
    id_busca_telefone = [id for id, info in dicionario_de_cadastrados.items() if info["telefone"] == telefone]   
    try:
        for chaves, valores in dicionario_de_cadastrados[id_busca_telefone[0]].items():
                print(f"{chaves} : {valores}")
        print("-" * 24)
    except IndexError:
            print("Telefone não encontrado!\n", "-" * 24)
            
        

     