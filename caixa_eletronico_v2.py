# # DADOS
saldo = 1000  # Exemplo de saldo inicial
extrato = []  # Lista para armazenar transações

# USUARIOS
usuarios = {
    "45888846899" : {"nome": "João", "idade": 30, "cep": "03974-160"}
}
print(usuarios)

# MENU
def menu():
    return int(input(f"""\n
===== MENU =====
1 - Saque
2 - Depósito
3 - Extrato
4 - Criar Usuario
5 - Criar Conta                
================                                                               
Digite o número da operação desejada: """))

# # SAQUE
def sacar(valor):
    global saldo, extrato   # variaveis globais
    saque_diario = 3    # limite de saque diario
    print(f'Saldo Atual: {saldo}')  # exibir saldo atual
    if (valor > 0 and valor <= saldo) and (saque_diario > 0 and saque_diario <= 3): # verificacao do valor
        saldo -= valor  # subtracao do valor do saldo
        saque_diario -= 1   # saque diario diminuido
        extr_saque = str(f'Saque: {valor}')  # convertendo em string
        extrato.append(extr_saque)  # salvando transacao no extrato
        print(f'Saque de R${valor} realizado com sucesso.')
        print(f'Saldo Atual: {saldo}')
    else:
        print('Saldo Insuficiente ou limite de saque diário excedido.')

# # DEPÓSITO
def depositar(valor):
    global saldo, extrato   # variaveis globais
    saldo += valor  # adicao do valor ao saldo
    extr_deposito = str(f'Depósito: {valor}') # convertendo em string
    extrato.append(extr_deposito)   # salvando transacao no extrato
    print(f'Depósito de R${valor} realizado com sucesso.')
    print(f'Saldo Atual: {saldo}')

# # EXTRATO
def exibir_extrato():
    for transacao in extrato:   # exibir todas transacoes salvas no extrato
        print(transacao)

# CRIAR USUARIO
def criar_usuario():
    global usuarios
    cpf = str(input('Digite o CPF do usuário: ')) # digitar cpf
    if cpf in usuarios: # se cpf estiver em USUARIOS
        print('CPF já cadastrado.')
    else:
        nome = str(input('Digite o nome do usuário: '))
        idade = str(input('Digite a idade do usuário: '))
        cep = str(input('Digite o CEP do usuário: '))
        novo_usuario = cpf, nome, idade, cep
        print(novo_usuario)
        usuarios[cpf] = novo_usuario
        print('Usuário criado com sucesso.')
        print(usuarios)

# CRIAR CONTA
def criar_conta():
    cpf = str(input('Digite o CPF do usuário: '))
    if cpf not in usuarios:
        print('CPF não cadastrado.')
        return
    num_agencia = str(input('Digite o número da agencia: '))
    num_conta = str(input('Digite o número da conta: '))
    usuarios[cpf]['contas'].append({'num_agencia': num_agencia, 'numero_conta': num_conta})
    print('Conta criada com sucesso.')
    
# # MAIN
def main():
    escolha = menu()
    if escolha == 1:
        print(('='*10), f'\n- Saque -')
        sacar(int(input(f'Digite um valor: ')))  # Solicitando um valor para saque
    elif escolha == 2:
        print(('='*10), f'\n- Deposito -')
        depositar(int(input(f'Digite um valor: ')))  # Solicitando um valor para deposito
    elif escolha == 3:
        print(('='*10), f'\n- Extrato -')
        exibir_extrato()  # Exibir extrato
    elif escolha == 4:
        print(('='*10), f'\n- Criar Usuario -')
        criar_usuario()
    elif escolha == 5:
        print(('='*10), f'\n- Criar Conta -')
        criar_conta()
    else:
        print(('='*10), f'Opção inválida. Por favor, selecione uma operação válida (1, 2 ou 3).')  # exibindo que houve um erro
main()