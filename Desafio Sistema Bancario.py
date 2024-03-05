MENU = '''
Escolha uma das opções abaixo:
[D]epositar
[S]acar
[E]xtrato
[Q]sair
===>'''

saldo = 0
limite = 500
extrato = 'Extrato Bancário de Transações\n'
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(MENU)
    if opcao.upper() == 'D':
        print('Depósito escolhido')
        valor = int(input('Informe o valor do depósito: '))
        if int(valor) > 0:
            saldo += valor 
            transacao = f'Deposito no valor de {valor} confirmado. Saldo atual é de {saldo}.'
            extrato = extrato + transacao + '\n'
            print(transacao)
        else:
            print('Valor inválido. Depósito não realizado')
    elif opcao.upper() == 'S':
        print('Saque escolhido')
        valor = int(input('Informe o valor do saque: '))
        if int(valor) > 0:
            if numero_saques < 3:
                if saldo >= valor:
                    saldo -= valor 
                    numero_saques += 1
                    transacao = f'Saque no valor de {valor} confirmado. Saldo atual é de {saldo}.'
                    extrato = extrato + transacao + '\n'
                    print(transacao)
                else:
                    print('Saldo insuficiente. Saque não realizado')
            else:
                print('Limite de saques diários ultrapassado. Saque não realizado')
        else:
            print('Valor inválido. Saque não realizado')
    elif opcao.upper() == 'E':
        print('Extrato escolhido')
        print(extrato)
    elif opcao.upper() == 'Q':
        break
    else:
        print('Opção Invalida')