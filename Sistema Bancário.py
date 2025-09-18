
import datetime

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
mascara = "%d/%m/%Y %a %H:%M"
diahoje = "01/01/2000"
transacoes = 0

# || FUNCOES  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def numtransacoes():
    global diahoje, transacoes
    timenow = datetime.datetime.now()
    if timenow.date() != diahoje:
        diahoje = timenow.date()
        print("A DATA É NOVA E FOI SUBSTITUIDA")
    if timenow.date() == diahoje:
        transacoes += 1
        print("Transacoes", transacoes)





def depositar(valor):
    global saldo
    numtransacoes()
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
    numtransacoes()
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
