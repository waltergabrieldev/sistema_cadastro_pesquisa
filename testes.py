import cadastrando
import validar_cpf
import buscando


print("bem vindo ao sistema de buscas e cadastros")
escolha = input("busca    /1/ \ncadastro /2/ \n>>> ")


if escolha == "1":
    escolha_busca = input("busca por cpf  /1/ \n busca por id /2/ \n>>> ")
    if escolha_busca == "1":
        cpf_para_busca = input("digite o cpf: \n>>> ")
        buscando.procurando_cpf(cpf_para_busca)
    elif escolha_busca == "2":
        id_para_busca = input('digite o id: \n>>>  ')
        buscando.procurando_por_id(id_para_busca)

elif escolha == "2":
    nome = input("cadastre o nome: \n>>> ")
    while True:
        cpf = validar_cpf.confirmacao_cpf_padrao()
        if not validar_cpf.verificacao(cpf):
            print("cpf inválido! digite um cpf válido!")
        elif not cadastrando.coferindo_cpf_existentes(cpf):
            print("o cpf digitado já está cadastrado no sistema!")
        else:   
            break    
        
    while True:  
        telefone = input("cadastre o telefone: \n>>> ")
        if not cadastrando.coferindo_telefone_existentes(telefone):
            print("o número digitado já está cadastrado no sistema!") 
        else:
            break
    
    lista = [nome , cpf, telefone]
    cadastrando.cadastro(lista)


    
    
     