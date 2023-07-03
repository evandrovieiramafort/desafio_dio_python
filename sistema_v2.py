"""Um adendo neste código:
    Para diferenciar um pouco do que foi pedido - mas ainda fazendo o solicitado, optei por utilizar uma
    nova funcionalidade em python, que foi introduzida na versão 3.11: O Match Case. Ela elimina a necessiade de
    montar um menu que se utiliza de ifs, elifs e elses para funcionar - melhorando a legibilidade do código."""


def main():
    saldo = 0.0
    QTDE_SAQUES = 3
    LIMITE = 500
    extrato = ""
    contas = []
    usuarios = []

    while True:
        print("\nSelecione uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Criar Usuário")
        print("5. Criar Conta")
        print("6. Listar Contas")
        print("7. Sair")

        opcao = input("Opção: ")

        match opcao:
            case "1":
                deposito = float(input("Digite o valor do depósito: "))
                saldo, extrato = depositar(deposito, saldo, extrato)
            case "2":
                saque = float(input("Digite o valor do saque: "))
                saldo, extrato = sacar(
                    saque=saque,
                    saldo=saldo,
                    extrato=extrato,
                    limite_saques=LIMITE, qtde_saques=QTDE_SAQUES, )
            case "3":
                mostrar_extrato(saldo, extrato=extrato)
            case "4":
                criar_usuario(usuarios)
            case "5":
                agencia = input("Digite a agência: ")
                numero_conta = input("Digite o número da conta: ")
                conta = criar_conta(agencia, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            case "6":
                listar_contas(contas)
            case "7":
                print("Encerrando por aqui\nObrigado pela preferência")
                break
            case _:
                print("Opção inválida! Digite um número válido.")


def depositar(deposito, saldo, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito de R${deposito:.2f}"
    else:
        print(f"Valor inválido!\n Saldo: R${saldo:.2f}")
    return saldo, extrato


def sacar(*, saque, saldo, extrato, limite_saques, qtde_saques):
    if saque > saldo or saque > limite_saques:
        print("Saque inválido!")
    elif qtde_saques == 0:
        print("Limite de saques atingido!\n")
    else:
        saldo -= saque
        qtde_saques -= 1
        if qtde_saques > 0:
            print(f"Você ainda tem direito a {qtde_saques} saques por hoje.")
            extrato += f"Saque no valor de R${saque:.2f}"
        else:
            print(f"Saldo: R${saldo:.2f}\nVocê está sem direito a mais saques por hoje.")
    return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
    print("=" * 10)
    print("Não foram feitas operações recentemente" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("=" * 10)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nExistem usuários com este mesmo CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"Nome": nome, "Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})

    print("Usuário criado com sucesso")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else print("Não há usuários com este CPF.")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, encerrando procedimento")


def listar_contas(contas):
    for conta in contas:
        linha = (
            f"Agência:\t{conta['agencia']}\n"
            f"C/C:\t\t{conta['numero_conta']}\n"
            f"Titular:\t{conta['usuario']['nome']}\n"
        )
        print("=" * 100)
        print(linha)


main()
