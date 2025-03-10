from os import system
import cadastrando
import validador_cpf
import buscando


print("bem vindo ao sistema de buscas e cadastros")

while True:
    escolha = input("busca    /1/ \ncadastro /2/ \n >>> ")

    system("cls")

    if escolha == "1":
        escolha_busca = input("busca por cpf  /1/ \n busca por telefone /2/ \n>>> ")
        system("cls")
        
        if escolha_busca == "1":
            cpf_para_busca = input("digite o cpf: \n>>> ")
            system("cls")
            
            buscando.procurando_cpf(cpf_para_busca)
            
        elif escolha_busca == "2":
            telefone = input("digite o telefone: \n>>>  ")
            system("cls")
            
            buscando.procurando_por_telefone(telefone)

    elif escolha == "2":
        nome = input("cadastre o nome: \n>>> ")
        
        system("cls")
        
        while True:
            cpf = validador_cpf.confirmacao_cpf_padrao()
            
            if not  validador_cpf.verificacao(cpf):
                print("cpf inválido! digite um cpf válido!")
                
            elif not cadastrando.coferindo_cpf_existentes(cpf):
                print("o cpf digitado já está cadastrado no sistema!")
                
            else:   
                system("cls")
                break    
            
        while True:  
            
            telefone = input("cadastre o telefone: \n>>> ")
            if not cadastrando.verificando_telefone(telefone):
                print("Telefone inválido!")
                
            elif not cadastrando.coferindo_telefone_existentes(telefone):
                print("o número digitado já está cadastrado no sistema!") 
            
            else:
                system("cls")
                break
        
        lista = [nome , cpf, telefone]
        
        cadastrando.cadastro(lista)


    
    
     