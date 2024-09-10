import re

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        
class ContaCorrente:
    numero_conta_sequencial = 1

    def __init__(self, cliente):
        self.agencia = "0001"
        self.numero = ContaCorrente.numero_conta_sequencial
        self.cliente = cliente
        
        ContaCorrente.numero_conta_sequencial += 1

    def exibir_detalhes(self):
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero}")
        print(f"Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}")

clientes_cadastrados = {}

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_data_nascimento(data_nascimento):
    padrao_data = re.compile(r"\d{2}/\d{2}/\d{4}")
    return bool(padrao_data.fullmatch(data_nascimento))

def validar_endereco(endereco):
    padrao_endereco = re.compile(r".+\s-\s\d+\s-\s.+\s-\s.+/.{2}")
    return bool(padrao_endereco.fullmatch(endereco))

def cadastrar_cliente():
    nome = input("Digite o nome: ").strip()
    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return
    
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
    if not validar_data_nascimento(data_nascimento):
        print("Erro: Data de nascimento inválida. Use o formato DD/MM/AAAA.")
        return
    
    cpf = input("Digite o CPF (somente números): ").strip()
    if not validar_cpf(cpf):
        print("Erro: CPF inválido. O CPF deve conter exatamente 11 dígitos.")
        return
    
    if cpf in clientes_cadastrados:
        print("Erro: CPF já cadastrado.")
        return
    
    endereco = input("Digite o endereço (logradouro - número - bairro - cidade/sigla estado): ").strip()
    if not validar_endereco(endereco):
        print("Erro: Endereço inválido. Use o formato 'logradouro - número - bairro - cidade/sigla estado'.")
        return

    novo_cliente = Cliente(nome, data_nascimento, cpf, endereco)
    clientes_cadastrados[cpf] = novo_cliente
    print(f"Cliente {nome} cadastrado com sucesso!")

def exibir_clientes():
    if not clientes_cadastrados:
        print("Nenhum cliente cadastrado.")
        return
    print("\n===== Clientes Cadastrados =====")
    for cpf, cliente in clientes_cadastrados.items():
        print(f"Nome: {cliente.nome}")
        print(f"Data de Nascimento: {cliente.data_nascimento}")
        print(f"CPF: {cliente.cpf}")
        print(f"Endereço: {cliente.endereco}")
        print("===============================")

def exibir_menu():
    print("\nSistema Bancário")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Exibir Extrato")
    print("[4] Cadastrar Cliente")
    print("[5] Exibir Clientes")
    print("[6] Sair")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
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
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def cadastrar_conta_corrente():
    cpf = input("Digite o CPF do cliente: ").strip()
    
    if cpf not in clientes_cadastrados:
        print("Erro: Cliente não encontrado.")
        return
    
    cliente = clientes_cadastrados[cpf]
    nova_conta = ContaCorrente(cliente)

    if not hasattr(cliente, "contas"):
        cliente.contas = []
    
    cliente.contas.append(nova_conta)
    print(f"Conta corrente criada com sucesso para {cliente.nome}!")
    nova_conta.exibir_detalhes()

def exibir_contas_cliente():
    cpf = input("Digite o CPF do cliente: ").strip()

    if cpf not in clientes_cadastrados:
        print("Erro: Cliente não encontrado.")
        return

    cliente = clientes_cadastrados[cpf]
    
    if not hasattr(cliente, "contas") or len(cliente.contas) == 0:
        print(f"O cliente {cliente.nome} não possui contas cadastradas.")
        return

    print(f"\n===== Contas do Cliente {cliente.nome} =====")
    for conta in cliente.contas:
        conta.exibir_detalhes()
        print("===============================")

def exibir_menu():
    print("\nSistema Bancário")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Exibir Extrato")
    print("[4] Cadastrar Cliente")
    print("[5] Exibir Clientes")
    print("[6] Cadastrar Conta Corrente")
    print("[7] Exibir Contas do Cliente")
    print("[8] Sair")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("Entrada inválida. Digite um valor numérico.")
        
        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
            except ValueError:
                print("Entrada inválida. Digite um valor numérico.")
        
        elif opcao == "3":
            exibir_extrato(extrato, saldo)
        
        elif opcao == "4":
            cadastrar_cliente()

        elif opcao == "5":
            exibir_clientes()

        elif opcao == "6":
            cadastrar_conta_corrente()

        elif opcao == "7":
            exibir_contas_cliente()

        elif opcao == "8":
            print("Saindo do sistema...")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()