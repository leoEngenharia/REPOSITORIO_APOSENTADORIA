''' NA VERSÃO 3 ESTAMOS USANDO UM LOOP PERGUNTANDO SE O USUARIO DESEJA CADASTRAR OUTRA EMPRESA,
OU DESEJA ENCERRAR O PROGRAMA , CALCULA A MEDIA DOS SALARIOS'''
from datetime import datetime

# Defina o ano de referência para a conversão da moeda aqui
ano_referencia = 1967  # Você pode alterar este valor conforme necessário

class Empresa:
    def __init__(self, nome, data_admissao, data_demissao, salario, insalubridade):
        self.nome = nome
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.salario = salario
        self.insalubridade = insalubridade

# Lista para armazenar as empresas cadastradas
empresas = []

while True:
    def cadastrar_empresa():
        nome = input("Digite o nome da empresa: ")
        data_admissao = input("Digite a data de admissão (dd/mm/aaaa): ")
        data_demissao = input("Digite a data de demissão (dd/mm/aaaa): ")
        salario = float(input("Digite o salário: "))
        insalubridade = input("A empresa tem insalubridade? (S/N): ").upper()

        if insalubridade == "S":
            tem_insalubridade = True
        else:
            tem_insalubridade = False

        nova_empresa = Empresa(nome, data_admissao, data_demissao, salario, tem_insalubridade)
        empresas.append(nova_empresa)
        print("Empresa cadastrada com sucesso!")

    cadastrar_empresa()

    resposta = input("Deseja cadastrar outra empresa? (S/N): ").lower()
    if resposta != "s":
        break

# Realize os cálculos aqui fora do loop de cadastro
soma_salarios = sum(empresa.salario for empresa in empresas)
contador_salarios = len(empresas)

if contador_salarios > 0:
    media_salarios = soma_salarios / contador_salarios
else:
    media_salarios = 0

# Função para calcular o tempo de emprego em anos, meses e dias
def calcular_tempo_emprego(data_admissao, data_demissao):
    if data_admissao == "" or data_demissao == "":
        return 0, 0, 0  # Retorna zero anos, zero meses e zero dias se as datas não estiverem disponíveis
    formato_data = "%d/%m/%Y"
    data_admissao_obj = datetime.strptime(data_admissao, formato_data)
    data_demissao_obj = datetime.strptime(data_demissao, formato_data)
    tempo_emprego = (data_demissao_obj - data_admissao_obj).days
    anos = tempo_emprego // 365
    meses = (tempo_emprego % 365) // 30
    dias = (tempo_emprego % 365) % 30
    return anos, meses, dias

# Função para calcular o tempo com insalubridade
def calcular_tempo_com_insalubridade(tempo_emprego_total):
    return int(tempo_emprego_total * 1.4)  # Arredonda para baixo para o número inteiro mais próximo

# Função para converter moeda antiga para reais
def converter_moeda_para_real(valor, data_demissao):
    if data_demissao == "" or datetime.strptime(data_demissao, "%d/%m/%Y") < datetime(ano_referencia, 1, 1):
        return valor  # Se a data de demissão não estiver disponível ou for anterior ao ano de referência, não faz a conversão
    data_demissao_obj = datetime.strptime(data_demissao, "%d/%m/%Y")
    if data_demissao_obj >= datetime(1967, 2, 13) and data_demissao_obj <= datetime(1970, 5, 14):
        return valor / (1000 ** 5 * 2.75)
    elif data_demissao_obj >= datetime(1970, 5, 15) and data_demissao_obj <= datetime(1989, 2, 27):
        return valor / (1000 ** 4 * 2.75)
    elif data_demissao_obj >= datetime(1986, 2, 28) and data_demissao_obj <= datetime(1989, 1, 15):
        return valor / (1000 ** 3 * 2.75)
    elif data_demissao_obj >= datetime(1989, 1, 16) and data_demissao_obj <= datetime(1990, 3, 15):
        return valor / (1000 ** 2 * 2.75)
    elif data_demissao_obj >= datetime(1990, 3, 16) and data_demissao_obj <= datetime(1993, 7, 31):
        return valor / (1000 ** 2 * 2.75)
    elif data_demissao_obj >= datetime(1993, 8, 1) and data_demissao_obj <= datetime(1994, 6, 30):
        return valor / (1000 * 2.75)
    elif data_demissao_obj >= datetime(1994, 7, 1):
        return valor * 1
    return valor  # Se a data não se encaixar em nenhuma faixa ou não for especificada, retorna o valor original

# Exemplo de cálculos
nova_empresa = empresas[-1]  # Pega a última empresa cadastrada
tempo_emprego_anos, tempo_emprego_meses, tempo_emprego_dias = calcular_tempo_emprego(nova_empresa.data_admissao, nova_empresa.data_demissao)

# Imprimir tempo de emprego em anos, meses e dias
print(f"Tempo de emprego: {tempo_emprego_anos} anos, {tempo_emprego_meses} meses, {tempo_emprego_dias} dias")

if nova_empresa.insalubridade:
    tempo_emprego_total = (tempo_emprego_anos * 365) + (tempo_emprego_meses * 30) + tempo_emprego_dias
    tempo_com_insalubridade = calcular_tempo_com_insalubridade(tempo_emprego_total)
    anos_bonus, meses_bonus, dias_bonus = calcular_tempo_emprego(nova_empresa.data_admissao, nova_empresa.data_demissao)

    print(f"Tempo com insalubridade: {tempo_com_insalubridade // 365} anos, {(tempo_com_insalubridade % 365) // 30} meses, {(tempo_com_insalubridade % 365) % 30} dias")

# Converter o valor do salário para reais com 2 casas decimais
valor_salario_em_reais = converter_moeda_para_real(nova_empresa.salario, nova_empresa.data_demissao)

print(f"Valor do salário em reais: R$ {valor_salario_em_reais:.2f}")
print(f"Soma de todos os salários: R$ {soma_salarios:.2f}")
print(f"Média dos salários: R$ {media_salarios:.2f}")