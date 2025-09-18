# Exercício Sistema Bancário Simples
Exercício de criação de sistema bancário em Python com criação de sistema de depósito, saque e extrato. 

## Específicações 01:
|Função|Detalhes|
|---|---|
|Depósito|Realizar depósitos e armazenar a operação em Extratos :heavy_check_mark:|
|Saque|Realizar 3 saques limitados a 500 reais :heavy_check_mark:|
|Usuário|Sendo inicialmente um exercício simples, será considerado a existência de apenas UM usuário :heavy_check_mark:|

# Atualização Data e Hora 01:
- Limite de 10 transações diárias totais entre saques e depósitos :heavy_check_mark:
- Se usuário tentar após 10 tentativas, ele deve ser informado por meio de uma mensagem :heavy_check_mark:
- mostre no extrato a data e hora de todas as transações :heavy_check_mark:

# Atualização Desafio 02:
Criar duas novas funções:
- Criar usuário (cliente do banco)
O programa deve armazenar os usuários em uma lista, ele deve conter NOME, CPF E ENDEREÇO, O endereço deve ter LOGRADOURO, NÚMERO - BAIRRO - CIDADE/SIGLA DO ESTADO. Devem ser armazenados apenas os números do CPF. Não podem haver dois clientes com CPFs iguais. 
- Criar conta corrente (vinculada ao usuário)
O programa deve armazenar as contas compostas por AGENCIA, NUMERO DA CONTA E USUÁRIO, a agência fixa é fixa 0001, o número da conta é sequencial iniciando em 11111. **O usuário pode ter mais de uma conta, mas cada conta deve pertencer a um usuário**
