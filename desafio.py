import sys

usuarios = []
contador_contas = 1 

def formatar_cpf(cpf):
    return "".join(filter(str.isdigit, cpf))

def buscar_usuario(cpf):

    cpf_buscar = formatar_cpf(cpf)
    for usuario in usuarios:
        if usuario["cpf"] == cpf_buscar:
            return usuario
    return None

def cadastrar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    endereco = input("Endereço (logradouro, nro, bairro, cidade/UF): ")

    if buscar_usuario(cpf):
        print("Erro: Usuário com esse CPF já está cadastrado!\n")
        return None
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": formatar_cpf(cpf),
        "endereco": endereco,
        "contas": []
    }
    criar_conta(usuario)
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!\n")
    return usuario

def login():
    print("\n=== LOGIN ===")
    cpf = input("Informe seu CPF: ")
    usuario = buscar_usuario(cpf)
    if usuario:
        print(f"Login realizado com sucesso! Bem-vindo(a), {usuario['nome']}\n")
        return usuario
    else:
        print("CPF não encontrado. Cadastre-se primeiro.\n")
        return None

def criar_conta(usuario):
    global contador_contas
    conta = {
        "agencia": "0001",
        "numero_conta": f"{contador_contas:04d}",
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0,
        "limite": 500,
        "limite_saques": 3

    }
    usuario["contas"].append(conta)
    contador_contas += 1
    print(f"Conta criada com sucesso! Agência: {conta['agencia']}, Conta: {conta['numero_conta']}\n")
    return conta

def selecionar_conta(usuario):
    if len(usuario["contas"]) == 0:
        print("Usuário não possui contas!")
        return None
    elif len(usuario["contas"]) == 1:
        return usuario["contas"][0]
    else:
        print("Selecione a conta desejada:")
        for conta in usuario["contas"]:
            print(f"{conta['numero_conta']} - Agência {conta['agencia']} | Saldo: R$ {conta['saldo']:.2f}")
        numero = (input("Número da conta: "))
        for conta in usuario["contas"]:
            if conta["numero_conta"] == numero:
                return conta
        print("Conta não encontrada!")
        return None

def menu_login():

    menu_login = """
[1] Login
[2] Cadastrar Usuário
[3] Sair

=> """

    return menu_login

def menu_conta():

  menu_conta = """
  [c] Criar Conta
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

  => """
  return menu_conta

def saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return



def main():
    
    while True:
        
        opcao = input(menu_login())

        if opcao == "1":
            usuario = login()
            if not usuario:
                continue
       
        elif opcao == "2":
            usuario = cadastrar_usuario()
            if not usuario:
                continue
       
        elif opcao == "3":
            sys.exit("Obrigado por utilizar nosso sistema.")
       
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            continue
        
        conta = selecionar_conta(usuario)
        if not conta:
            continue
    
        while True:

            opcao = input(menu_conta())

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                conta["saldo"], conta["extrato"] = deposito(conta["saldo"], valor, conta["extrato"])

            elif opcao == "c":
                criar_conta(usuario)
                conta = selecionar_conta(usuario)
                if not conta:
                    continue

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                conta["saldo"], conta["extrato"], conta["numero_saques"] = saque(
                    saldo=conta["saldo"],
                    valor=valor,
                    extrato=conta["extrato"],
                    limite=conta["limite"],
                    numero_saques=conta["numero_saques"],
                    limite_saques=conta["limite_saques"]
                )

            elif opcao == "e":
                extrato(conta["saldo"], extrato=conta["extrato"])

            elif opcao == "q":
                print("Saindo da conta...\n")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")




if __name__ == "__main__":
    main()