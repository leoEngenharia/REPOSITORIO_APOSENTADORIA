''' NA VERSÃO 3 ESTOU USANDO UM LOOP PERGUNTANDO SE O USUARIO DESEJA CADASTRAR OUTRA EMPRESA,
OU DESEJA ENCERRAR O PROGRAMA , CALCULA A MEDIA DOS SALARIOS, e salva o arquivo
 em csv para um preenchimento posterior dando a possibilidade de continuar o q começou ou fazer um novo'''
import csv
import os
from datetime import datetime

ano_referencia = 1967  # Você pode alterar este valor conforme necessário
# Defina a classe Empresa aqui
class Empresa:
    def __init__(self, nome, data_admissao, data_demissao, salario, insalubridade):
        self.nome = nome
        self.data_admissao = data_admissao
        self.data_demissao = data_demissao
        self.salario = salario
        self.insalubridade = insalubridade

# Verifique se o arquivo CSV existe
if os.path.exists('dados_empresas.csv'):
    resposta = input("Deseja continuar com o relatório existente? (S/N): ").lower()
    if resposta == 's':
        # Carrega os dados do CSV
        empresas = []
        with open('dados_empresas.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                nome, data_admissao, data_demissao, salario, insalubridade = row
                empresas.append(Empresa(nome, data_admissao, data_demissao, float(salario), insalubridade.upper() == 'S'))
    else:
        # Se o usuário não quiser continuar com o relatório existente, cria uma lista vazia
        empresas = []
else:
    # Se o arquivo CSV não existir, cria uma lista vazia
    empresas = []

# Resto do seu código aqui...


# Defina o caminho completo para o arquivo
file_path = r'C:\Users\leoat\OneDrive\Documentos\REPOSITORIOS_CALCULOS_APOSENTADORIA\REPOSITORIO_APOSENTADORIA\dados_empresas.csv'

# Código para salvar os dados das empresas em CSV
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for empresa in empresas:
        writer.writerow([empresa.nome, empresa.data_admissao, empresa.data_demissao, empresa.salario, empresa.insalubridade])

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

# Realize os cálculos para tempo de emprego e conversão de moeda aqui
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
        return valor
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
    return valor

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

#print(f"Valor do salário em reais: R$ {valor_salario_em_reais:.2f}")
print(f"Soma de todos os salários: R$ {soma_salarios:.2f}")
print(f"Média dos salários: R$ {media_salarios:.2f}")

# Salvar os dados no arquivo CSV na área de trabalho
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Data Admissão", "Data Demissão", "Salário", "Insalubridade"])
    for empresa in empresas:
        writer.writerow([empresa.nome, empresa.data_admissao, empresa.data_demissao, empresa.salario, empresa.insalubridade])

print(f'Dados salvos em {file_path}')