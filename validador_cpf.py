def verificacao(cpf):
    
    cpf = (cpf.replace('.','').replace('-',''))
    
    if cpf == cpf[0]*11:
        
        cpf_valido = False
    else:   
        
        cpf_verificador = cpf[0:9]
        calculo_multiplicacao = 0
        
        for contagem_regressiva, numeros in zip(range(10,1,-1), cpf_verificador) :
            calculo_multiplicacao += int(numeros) * contagem_regressiva
            
        calculo_divisao = (calculo_multiplicacao % 11)
        
        if calculo_divisao < 2:
            numeros_finais_1 = 0
        else:
            numeros_finais_1 = 11 - calculo_divisao
            
        cpf_verificador += str(numeros_finais_1)
        calculo_multiplicacao = 0
        calculo_divisao = 0
        
        for contagem_regressiva, numeros in zip(range(11,1,-1), cpf_verificador) :
            calculo_multiplicacao += int(numeros) * contagem_regressiva
            
        calculo_divisao = (calculo_multiplicacao % 11)
        
        if calculo_divisao < 2:
            numeros_finais_2 = 0
        else:
            numeros_finais_2 = 11 - calculo_divisao
        cpf_verificador += str(numeros_finais_2)
        
        if cpf_verificador == cpf:
            cpf_valido = True
        else:
            cpf_valido = False
    
    return cpf_valido

def confirmacao_cpf_padrao():
    indice_cpf = 0
    while indice_cpf < 14:
        cpf = input('cadastre um cpf(***.***.***-**): \n>>> ')
        if len(cpf) != 14:
            print("Erro: O CPF deve ter exatamente 14 caracteres no formato ***.***.***-**")
            continue
        for char in cpf:
            if indice_cpf == 3 or indice_cpf == 7:
                if char != '.':
                    print('digite o cpf dentro do padrao indicado!')
                    break
            elif indice_cpf == 11:
                if char != '-':
                    print('digite o cpf dentro do padrao indicado!')
                    break      
            else:
                if not char.isnumeric():
                    print('digite o cpf dentro do padrao indicado!')
                    break
            indice_cpf += 1
    return(cpf)