

menu = print("""
|=========MENU=========|
|[1] Depositar         |
|[2] Sacar             |
|[3] Extrato           |
|[4] Sair              |
|======================|      
      """)



Saldo = 0
Limite = 500
Extrato = ""
Numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deposito = float(input("Digite o quanto você gostaria de depositar: "))
        if deposito > 0:
            Saldo += deposito
            Extrato += f"deposito de R$ {deposito:.2f}\n"
            print(f"Você depositou {deposito:.2f} o seu saldo final é {Saldo:.2f}")
        else:
            print("O deposito tem que ser maior que 0")

        
    elif opcao == "2":
        Saque = float(input("Quanto você gostaria de Sacar? "))
        if Saque > Saldo:
            print("Desculpe, valor insuficiente.")

        elif Saque > Limite:
            print(f"O Saque não pode ser maior que o limite de R${Limite:.2f}")

        elif Numero_saques >= LIMITE_SAQUES:
            print("Numero maximo de saque atingido.")
        else:
            Saldo -= Saque
            Numero_saques +=1
            Extrato += f"Saque de R$ {Saque:.2f}\n"
            print(f"Voce sacou R$ {Saque:.2f}. Seu saldo final é R${Saldo}")
        
    elif opcao == "3":
        print("\n==========EXTRATO==========")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"Saldo atual: R$ {Saldo:.2f}")
        print("===========================")


    elif opcao =="4":
        print("Saindo...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operacão desejada.")