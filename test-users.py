users_info = {}
users = []

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
        print(users)
        print(users_info)

    else:
        print("CPF já cadastrado!")


num_conta = 11111
contas_correntes = {}

def criar_conta_corrente(cpf):

    global users
    global num_conta
    if cpf in users:
        contas_correntes[num_conta] = {'agencia':'0001','cpf': cpf}
    num_conta+=1
    print(contas_correntes)




create_user()
create_user()
criar_conta_corrente(45404866837)
criar_conta_corrente(1234)