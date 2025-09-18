import datetime

menu = """

|                                      
|  MENU                                
|         
|  [c] Adicionar Conta Corrente                             
|  [d] Depositar                       
|  [s] Sacar                           
|  [e] Extrato                         
|  [q] Sair                            
|                                      

=>"""


shortmenu = """
|
| [m] Menu   [u] Novo Usuário    [q] Sair
|
=>"""



# || VARIÁVEIS ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
saldo = 0
limite = 500
numeros_saques = 0
saques_per_account = {}
LIMITE_SAQUES = 3
mascara = "%d/%m/%Y %a %H:%M"
diahoje = "01/01/2000"
transacoes = 0
users_info = {}
users = []
num_conta = 11111
contas_correntes = {}
depositos = []
saques = []
extrato = []

# || FUNCOES  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def velhonumtransacoes(): 
    global diahoje, transacoes 
    timenow = datetime.datetime.now()
    if timenow.date() != diahoje:
        diahoje = timenow.date()
        print("A DATA É NOVA E FOI SUBSTITUIDA") 
    if timenow.date() == diahoje:
        transacoes += 1 
        print("Transacoes", transacoes) 

def numtransacoes(cpf,conta): 
    global diahoje, transacoes 
    timenow = datetime.datetime.now()

    for key in saques_per_account.keys():
        if key == cpf:
            if timenow.date() != diahoje:
                diahoje = timenow.date()
                print("A DATA É NOVA E FOI SUBSTITUIDA") 
            if timenow.date() == diahoje:
                transacoes = saques_per_account['transacoes'] + 1
                print(transacoes)
                saques_per_account[cpf] = {transacoes}
        else:
            continue

def create_user():
    global users
    global users_info
    cpf = 0
    nome_user = ''
    logradouro = ''
    num_casa = 0
    bairro = ''
    cidade = ''
    estado = ''

    instruction = """Insira seu CPF:  *apenas números
    =>"""

    cpf = int(input(instruction))
    if cpf not in users:
        users.append(cpf)
            
        nome_user = input("""Insira o nome do novo usuário: 
    =>""")
        logradouro = input("""Insira o logradouro: 
    =>""")
        num_casa = int(input("""Insira o número da casa: 
    =>"""))
        bairro = input("""Insira o bairro: 
    =>""")
        cidade = input("""Insira a cidade: 
    =>""")
        estado = input("""Insira a sigla do estado: 
    =>""")
        endereço = f"{logradouro},{num_casa} - {bairro} - {cidade}/{estado}"
        print(endereço)

        users_info[cpf] = {'nome':nome_user,'endereco':endereço}
        print("| Usuário Cadastrado com sucesso!!")

    else:
        print("CPF já cadastrado!")

def criar_conta_corrente(cpf):

    global users
    global num_conta
    if cpf in users:
        contas_correntes[num_conta] = {'agencia':'0001','cpf': cpf}
        saques_per_account[cpf] = {'transacoes': 0}
    num_conta+=1
    print(contas_correntes)

def depositar(valor):
    global saldo
    
    cpff = int(input("Confirme seu CPF: "))
    conta_bancoo = int(input("Confirme sua conta bancária: "))

    numtransacoes(cpf=cpff,conta=conta_bancoo)

    if transacoes > 10:
        print("Sentimos muito! Número de transações diárias alcançado!")

    elif transacoes <= 10:
        saldo += valor
        timenow = datetime.datetime.now()
        depositos.append(f"|  Deposito: R${valor}   {timenow.strftime(mascara)}")
        extrato.append(f"|  Deposito: R${valor}   {timenow.strftime(mascara)}")
        print(f"""
    |                                      
    | Depósito                             
    |                                      
    | Valor de depósito: R${valor:}        
    | Saldo final: R${saldo:}               
    |
            """)
        return 
    
def sacar(valorsaque):
    global numeros_saques 
    global saldo
    
    cpff = int(input("Confirme seu CPF: "))
    conta_bancoo = int(input("Confirme sua conta bancária: "))

    numtransacoes(cpf=cpff,conta=conta_bancoo)

    if transacoes > 10:
        print("Sentimos muito! Número de transações diárias alcançado!")
    elif transacoes <= 10:
        numeros_saques += 1

        if valorsaque <= saldo:
            saldo -= valorsaque
            timenow = datetime.datetime.now()
            saques.append(f"|  Saque: R${valorsaque}   {timenow.strftime(mascara)}")
            extrato.append(f"|  Saque: R${valorsaque}   {timenow.strftime(mascara)}")
            print(f"""
    |                                      
    | Saque                            
    |                                      
    | Valor de saque: R${valorsaque:}        
    | Saldo final: R${saldo:}               
    |
            """)
        else: 
            print("Saldo Indisponivel")
    
def gomenu():
    while True:

        opcao = input(shortmenu).lower()
        if opcao == "m":
            opcao = input(menu).lower()
        elif opcao == "u":
            create_user()
            continue
        elif opcao == "q":
            print("""
        |
        |  Saindo...
        |""")
            break
        else:
            print("Ops, tente novamente!")
            continue

    #============================================================================================
        if opcao == "d": # DEPOSITO ============================================================
            try:
                valor = float(input("""
        |        
        |  Insira o valor de depósito:
        |
        => """))
                depositar(valor)
            except:
                print("""
        |
        |  Por favor insira um valor numérico!
        |""")
            continue

    #============================================================================================
        if opcao == "c": # CONTA CORRENTE ============================================================
            criar_conta_corrente()

    #============================================================================================
        elif opcao == "s": # SACAR ================================================================
            if numeros_saques >= LIMITE_SAQUES:
                print(""" 
        |  
        |Lamentamos! Número de saques diários atingido!
        |""")
            
            if numeros_saques < LIMITE_SAQUES:
                    while True:
                        try:
                            valorsaque = float(input("""
        |
        |  Insira o valor de saque : 
        |* Limite de R$500.00
        |=> """))  
                            if valorsaque > 500:
                                print("""
        |
        |  Valor acima do limite de R$500.00!
        |""")
                            elif valorsaque <= 500:
                                sacar(valorsaque)
                                break
                        except:
                            print("""
        |
        |  Por favor insira um valor numérico!
    |""")

    #============================================================================================
        elif opcao == "e": # EXTRATO ==============================================================
            print("""
        |
        |  Extrato
        |
        """)
            for item in extrato:
                print(item)
            continue

    #============================================================================================
        elif opcao == "q": # QUIT =================================================================
            print("""
        |
        |  Saindo...
        |""")
            break
        else:
            print("""
        |
        |  Operação Inválida, por favor selecione novamente a operação desejada.
        |""")

        print("")
        continue

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# PRA VALER MESMOOOOOO


print ("""
|
|  Bem-vindo ao seu sistema bancário!
|""")
gomenu()

