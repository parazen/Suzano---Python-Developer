
def depositar(saldo):
    valor = float(input("Digite o valor a ser depositado: "))
    saldo = saldo + valor
    print("Depósito realizado com sucesso!")
    print("Saldo atual: R$", saldo)
    return saldo

numsaques = 0

def sacar(saldo):
    global numsaques
    saquemax = 500

    valor = float(input("Digite o valor a ser sacado: "))
    if valor > saquemax:
        print("Valor acima do limite de saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo = saldo - valor
        numsaques += 1
        if numsaques >= 3:
            print("Limite de saques diários atingido.")
        if numsaques == 3:
            print("Limite de saques diários atingido.")
    return saldo

def extrato(saldo):
    print("Extrato")
    print("Saldo: R$", saldo)

saldo = 0
while True:
    print("Bem Vindo(a) ao Banco Python")
    print("Escolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Extrato")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        saldo = depositar(saldo)
    elif opcao == 2:
        saldo = sacar(saldo)
    elif opcao == 3:
        extrato(saldo)
    elif opcao == 4:
        print("Obrigado(a) por utilizar o Banco Python")
        break
    else:
        print("Opção inválida.")