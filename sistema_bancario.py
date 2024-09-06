def exibir_menu():
    print("\nSistema Bancário")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Exibir Extrato")
    print("[4] Sair")

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
            print("Saindo do sistema...")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
