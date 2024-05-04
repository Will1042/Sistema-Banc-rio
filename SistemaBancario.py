menu = { """ [d] Depositar / [s] sacar / [e] extrato / [q] Sair => """}

saldo = 1000
limite_saque_diario = 500
extrato_saques = []
extrato_depositos = []
numero_saques = 0
limite_saque_diario = 3
saques_feitos = 0

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("deposito")
        
        deposito = int(input("Insira o valor para deposito: "))
        
        saldo += deposito
        
        deposito_extrato = str(deposito)
        extrato_depositos.append(deposito_extrato)
    
    elif opcao == "s":
        print("sacar")
        
        saque = int(input("Insira o valor desejado para saque: "))
        saque_extrato = str(saque)
        
        if saques_feitos < limite_saque_diario:
            if saque > 500:
                print("Valor ultrapassa limite de saque estipulado em R$500!")
            elif saque > saldo:
                print(f"Valor ultrapassa limite disponível em conta. Saldo da conta atual é: R${saldo}")
            else:
                saldo -= saque
                saques_feitos += 1

                extrato_saques.append(saque_extrato)
                print(saques_feitos)
        else: 
            print("Você atingiu o limite de 3 saques diarios!!!")
        
    elif opcao == "e":
        print(f"Saques realizados: {extrato_saques}")
        print(f"Depositos realizados: {extrato_depositos}")
        print(f"Seu saldo atual é: R${saldo}")
    
    elif opcao == "q":
        print("sair")
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada novamente!")
    