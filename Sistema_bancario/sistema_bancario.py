menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
valor = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nSeu saldo agora é de: R$ {saldo:.2f}")
            print("==========================================")

        else:
            print("Operação falhou! O valor informado é inválido.")
            print("==========================================")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print("==========================================")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            print("==========================================")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print("==========================================")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            qtd_saques_restantes = LIMITE_SAQUES - numero_saques
            print(f"\nSeu saldo agora é de: R$ {saldo:.2f}\nVocê agora tem apenas {qtd_saques_restantes} saque(s) permitido(s) ")
            print("==========================================")
            extrato += f"Saque: R$ {valor:.2f}\n"
            
            

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")