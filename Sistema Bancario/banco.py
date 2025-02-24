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
    return saldo

def extrato(saldo):
    print("Extrato")
    print("Saldo: R$", saldo)

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ")
    if cpf in usuarios:
        print("Usuário já existente!")
        return usuarios

    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço: ")

    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    print("Usuário criado com sucesso!")
    return usuarios

def criar_conta_corrente(contas, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return contas

    numero_conta = len(contas) + 1
    contas[numero_conta] = {
        "cpf": cpf,
        "saldo": 0
    }
    print("Conta corrente criada com sucesso! Número da conta:", numero_conta)
    return contas

usuarios = {}
contas = {}
saldo = 0

while True:
    print("Bem Vindo(a) ao Banco Python")
    print("Escolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Extrato")
    print("4 - Criar Usuário")
    print("5 - Criar Conta Corrente")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        saldo = depositar(saldo)
    elif opcao == 2:
        saldo = sacar(saldo)
    elif opcao == 3:
        extrato(saldo)
    elif opcao == 4:
        usuarios = criar_usuario(usuarios)
    elif opcao == 5:
        contas = criar_conta_corrente(contas, usuarios)
    elif opcao == 6:
        print("Obrigado(a) por utilizar o Banco Python")
        break
    else:
        print("Opção inválida.")