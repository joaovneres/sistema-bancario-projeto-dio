# Sistema Bancário Simples

Este projeto é um sistema bancário simples desenvolvido para o bootcamp da DIO de Engenharia de Dados com Python. O sistema permite realizar operações básicas como depósitos, saques e visualizar o extrato da conta. Foi projetado para fornecer uma compreensão fundamental de operações bancárias e tratamento de exceções em Python.

## Funcionalidades

- **Depositar**: Permite adicionar valores à conta.
- **Sacar**: Permite retirar valores da conta, respeitando limites de saque e saldo disponível.
- **Exibir Extrato**: Mostra todas as operações realizadas e o saldo atual.
- **Limites**: Configura um limite de saque e um número máximo de saques permitidos.

## Requisitos do Sistema

- Python 3.6 ou superior

## Como Executar o Projeto

1. **Clone o Repositório**

   Clone este repositório para o seu ambiente local usando o comando:

   ```bash
   git clone https://github.com/seuusuario/sistema-bancario-python.git
   ```

2. **Navegue para o Diretório do Projeto**

    Acesse o diretório onde o projeto foi clonado:

    ```bash
    cd sistema-bancario-python
    ```

3. **Executar o Programa**

    Execute o programa com o Python:

    ```bash
    python sistema_bancario.py
    ```

4. **Interaja com o Sistema**

    Após iniciar o programa, siga as instruções exibidas no menu para realizar depósitos, saques e visualizar o extrato.

## Exemplo de Uso

```
    Sistema Bancário
    [d] Depositar
    [s] Sacar
    [e] Exibir Extrato
    [q] Sair

    => d
    Informe o valor do depósito: R$ 100
    Depósito de R$100.00 realizado com sucesso.

    => s
    Informe o valor do saque: R$ 50
    Saque de R$50.00 realizado com sucesso.

    => e
    ================ EXTRATO ===============
    Depósito: R$ 100.00
    Saque: R$ 50.00

    Saldo: R$ 50.00
    ==========================================

    => q
    Saindo do sistema...
```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests e sugestões.

## Licença
Este projeto está licenciado sob a MIT License.

***

Desenvolvido por João Victor Cosme Neres de Sousa para o bootcamp da DIO de Engenharia de Dados com Python.
