from datetime import datetime


class Empresa:
    def __init__(self, nome, data_admissao, data_demissao, salario, insalubridade):
        self.nome = nome
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.salario = salario
        self.insalubridade = insalubridade


# Lista para armazenar as empresas cadastradas
empresas = []


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


# Chamada da função de cadastro
cadastrar_empresa()


# Cálculo do tempo total de emprego
def calcular_tempo_emprego(data_admissao, data_demissao):
    formato_data = "%d/%m/%Y"
    data_admissao_obj = datetime.strptime(data_admissao, formato_data)
    data_demissao_obj = datetime.strptime(data_demissao, formato_data)
    tempo_emprego = (data_demissao_obj - data_admissao_obj).days
    return tempo_emprego


# Converter dias para anos, meses e dias
def converter_dias_para_anos_meses_dias(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias_restantes = (dias % 365) % 30
    return anos, meses, dias_restantes


# Exemplo de cálculos
nova_empresa = empresas[-1]  # Pega a última empresa cadastrada
tempo_emprego = calcular_tempo_emprego(nova_empresa.data_admissao, nova_empresa.data_demissao)

# Imprimir tempo de emprego em dias
print("Tempo de emprego:", tempo_emprego, "dias")

if nova_empresa.insalubridade:
    tempo_com_insalubridade = tempo_emprego * 1.4
    anos_bonus, meses_bonus, dias_bonus = converter_dias_para_anos_meses_dias(int(tempo_com_insalubridade))
    print("Tempo com  insalubridade: {} anos, {} meses, {} dias".format(anos_bonus, meses_bonus, dias_bonus))
