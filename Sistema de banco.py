# Variáveis que PRECISAM ser mantidas fora do código para evitar bugs
saldo = 0.0
qtde_de_saques = 3
LIMITE = 500
extrato = ""

print("Olá, seja bem vindo! Escolha a opção a seguir:\n"
          "1 - Depósito\n"
          "2 - Saque\n"
          "3 - Extrato\n"
          "0 - Sair\n")
while True:

    opc = int(input("\nDigite a opção escolhida: "))

    if opc == 1:
        valor = float(input("\nDigite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}"
        else:
            print(f"Valor inválido!\n Saldo: R${saldo:.2f}")

    elif opc == 2:
        saque = float(input("\nDigite quanto quer sacar: "))
        if saque > saldo or saque > LIMITE:
            print("Saque inválido!")
        elif qtde_de_saques == 0:
            print("Limite de saques atingido!\n")
        else:
            saldo -= saque
            qtde_de_saques -= 1
            if qtde_de_saques > 0:
                print(f"Você ainda tem direito a {qtde_de_saques} saques por hoje.")
                extrato += f"Saque no valor de R${saque:.2f}"
            else:
                print(f"Saldo: R${saldo:.2f}\nVocê está sem direito a mais saques por hoje.")

    elif opc == 3:
        print("=" * 10)
        print("Não foram feitas operações recentemente" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("=" * 10)

    elif opc == 0:
        break

    else:
        print("Opção inválida, favor tentar novamente.")
print("Obrigado pela preferência!")
