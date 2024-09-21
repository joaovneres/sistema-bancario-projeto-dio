from abc import ABC, abstractmethod
from datetime import datetime


class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Cliente(PessoaFisica):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(nome, cpf, data_nascimento)
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)


class Conta:
    numero_sequencial = 1

    def __init__(self, cliente):
        self.saldo = 0
        self.numero = Conta.numero_sequencial
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
        Conta.numero_sequencial += 1

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, cliente, limite=500, limite_saques=3):
        super().__init__(cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques < self.limite_saques and valor <= self.limite and super().sacar(valor):
            self.numero_saques += 1
            return True
        return False

    def exibir_detalhes(self):
        print(f"Agência: {self.agencia}")
        print(f"Número da Conta: {self.numero}")
        print(f"Cliente: {self.cliente.nome} - CPF: {self.cliente.cpf}")


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        print(f"Depósito de R${self.valor:.2f} realizado com sucesso.")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            print(f"Saque de R${self.valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! Saldo insuficiente ou limite excedido.")


def exibir_menu():
    print("\n==== Sistema Bancário ====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Exibir Extrato")
    print("[4] Cadastrar Cliente")
    print("[5] Exibir Clientes")
    print("[6] Cadastrar Conta Corrente")
    print("[7] Exibir Contas do Cliente")
    print("[8] Sair")
    print("==========================")


def cadastrar_cliente(clientes_cadastrados):
    nome = input("Digite o nome: ").strip()
    cpf = input("Digite o CPF (somente números): ").strip()
    data_nascimento = input(
        "Digite a data de nascimento (DD/MM/AAAA): ").strip()
    endereco = input(
        "Digite o endereço (logradouro - número - bairro - cidade/sigla estado): ").strip()
    
    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    clientes_cadastrados[cpf] = cliente

    print(f"Cliente {nome} cadastrado com sucesso!")
    return cliente


def cadastrar_conta_corrente(clientes_cadastrados):
    cpf = input("Digite o CPF do cliente: ").strip()

    if cpf not in clientes_cadastrados:
        print("Erro: Cliente não encontrado.")
        return

    cliente = clientes_cadastrados[cpf]
    nova_conta = ContaCorrente(cliente)
    cliente.adicionar_conta(nova_conta)

    print(f"Conta corrente criada com sucesso para {cpf}!")
    nova_conta.exibir_detalhes()


def exibir_extrato(conta_corrente):
    print("\n========== EXTRATO ==========")
    if not conta_corrente.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta_corrente.historico.transacoes:
            print(f"{type(transacao).__name__}: R$ {transacao.valor:.2f}")
    print(f"\nSaldo atual: R$ {conta_corrente.saldo:.2f}")
    print("==============================")


def main():
    clientes_cadastrados = {}
    saldo = 0

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":  # Depositar
            cpf = input("Informe o CPF do cliente para depósito: ").strip()
            if cpf in clientes_cadastrados and clientes_cadastrados[cpf].contas:
                # Considerando a primeira conta do cliente
                conta = clientes_cadastrados[cpf].contas[0]
                try:
                    valor = float(input("Informe o valor do depósito: R$ "))
                    clientes_cadastrados[cpf].realizar_transacao(
                        conta, Deposito(valor))
                except ValueError:
                    print("Entrada inválida. Digite um valor numérico.")
            else:
                print("Cliente não encontrado ou sem conta cadastrada.")

        elif opcao == "2":  # Sacar
            cpf = input("Informe o CPF do cliente para saque: ").strip()
            if cpf in clientes_cadastrados and clientes_cadastrados[cpf].contas:
                # Considerando a primeira conta do cliente
                conta = clientes_cadastrados[cpf].contas[0]
                try:
                    valor = float(input("Informe o valor do saque: R$ "))
                    clientes_cadastrados[cpf].realizar_transacao(
                        conta, Saque(valor))
                except ValueError:
                    print("Entrada inválida. Digite um valor numérico.")
            else:
                print("Cliente não encontrado ou sem conta cadastrada.")

        elif opcao == "3":  # Exibir Extrato
            cpf = input(
                "Informe o CPF do cliente para exibir o extrato: ").strip()
            if cpf in clientes_cadastrados and clientes_cadastrados[cpf].contas:
                conta = clientes_cadastrados[cpf].contas[0]
                exibir_extrato(conta)
            else:
                print("Cliente não encontrado ou sem conta cadastrada.")

        elif opcao == "4":  # Cadastrar Cliente
            cadastrar_cliente(clientes_cadastrados)

        elif opcao == "5":  # Exibir Clientes
            if not clientes_cadastrados:
                print("Nenhum cliente cadastrado.")
            else:
                for cpf, cliente in clientes_cadastrados.items():
                    print(f"Cliente: CPF {cpf}, Nome: {cliente.nome}, Endereço: {cliente.endereco}")

        elif opcao == "6":  # Cadastrar Conta Corrente
            cadastrar_conta_corrente(clientes_cadastrados)

        elif opcao == "7":  # Exibir Contas do Cliente
            cpf = input("Informe o CPF do cliente: ").strip()
            if cpf in clientes_cadastrados and clientes_cadastrados[cpf].contas:
                for conta in clientes_cadastrados[cpf].contas:
                    conta.exibir_detalhes()
            else:
                print("Cliente não encontrado ou sem conta cadastrada.")

        elif opcao == "8":  # Sair
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, por favor tente novamente.")


if __name__ == "__main__":
    main()
