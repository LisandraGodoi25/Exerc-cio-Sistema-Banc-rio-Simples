'''
Precisaremos fazer 3 funcoes: deposito, saque e extrato
Apenas um usuário

Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato

O sistema deve permitir 3 saques diários com limite de 500 reais por saque. 
Se o usuário não tiver saldo, precisa-se enviar uma mensagem informando.
Todos os saques devem ser armazenados em uma variável saque para extrato.

O extrato deve listar todas as operações de saque e deposito feitas na conta. 
E no final da listagem deve aparecer o saldo atual
Todos os valores devem ser exibidos no formato R$XXX.00
'''

menu = """

|                                      
|  MENU                                
|                                      
|  [d] Depositar                       
|  [s] Sacar                           
|  [e] Extrato                         
|  [q] Sair                            
|                                      

=>"""


shortmenu = """
|
| [m] Menu        [q] Sair
|
=>"""



# || VARIÁVEIS ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
saldo = 0
limite = 500
numeros_saques = 0
LIMITE_SAQUES = 3


# || FUNCOES  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def depositar(valor):
    global saldo
    saldo += valor
    depositos.append(f"|  Deposito: R${valor}")
    extrato.append(f"|  Deposito: R${valor}")
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
    numeros_saques += 1

    if valorsaque <= saldo:
        saldo -= valorsaque
        saques.append(f"|  Saque: -R${valorsaque}")
        extrato.append(f"|  Saque: -R${valorsaque}")
        print(f"""
|                                      
| Saque                            
|                                      
| Valor de saque: -R${valorsaque:}        
| Saldo final: R${saldo:}               
|
        """)
    else: 
        print("Saldo Indisponivel")

# || LISTAS |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

depositos = []
saques = []
extrato = []

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

print ("""
|
|  Bem-vindo ao seu sistema bancário!
|""")

while True:

    opcao = input(shortmenu).lower()
    if opcao == "m":
        opcao = input(menu).lower()
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
    elif opcao == "s": # SACAR ================================================================
        if numeros_saques >= LIMITE_SAQUES:
            print(""" 
|  
|Lamentamos! Número de saques diários atingido!
|""")
        
        if numeros_saques < LIMITE_SAQUES:
            try:
                valorsaque = float(input("""
|
|  Insira o valor de saque: 
|
|=> """))
                sacar(valorsaque)
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
