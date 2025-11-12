# Sistema Bancário em Python

## Descrição

Este é um **sistema bancário simples em Python**, seguindo paradigma procedural, que permite gerenciar usuários, contas correntes, depósitos, saques e extratos.  
O sistema mantém o histórico de operações de cada conta e suporta múltiplas contas por usuário.


## Funcionalidades

- **Cadastro de Usuário**  
  - Nome completo, data de nascimento, CPF e endereço.  
  - CPF é armazenado apenas com números e não permite duplicidade.  
  - Ao cadastrar um usuário, uma conta corrente é criada automaticamente.

- **Login**  
  - Login realizado via CPF do usuário.  
  - É possível selecionar a conta desejada caso o usuário possua mais de uma.

- **Gestão de Contas**  
  - Criar novas contas correntes para um usuário existente.  
  - Cada conta possui agência (`0001`), número sequencial único, saldo inicial, limite de saque e histórico de transações.

- **Operações Bancárias**  
  - **Depósito**: Adiciona valor à conta.  
  - **Saque**: Subtrai valor respeitando saldo, limite de saque e limite de número de saques.  
  - **Extrato**: Mostra histórico de transações e saldo atual.


## Como usar

1. **Executar o sistema**:

```bash
python main.py
