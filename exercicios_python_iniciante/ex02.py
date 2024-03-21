"""
Crie um programa Python para calcular os juros de um depósito bancário.
"""

# Solicite ao usuário que insira o valor principal
valor = float(input('Valor do produto: R$ '))

# Número de anos
anos = int(input('Valor em anos a ser pago: '))

# Taxa de juros
taxa = float(input('Taxa aplicada: '))

# Calcule os juros anuais
juros = valor*anos*(taxa/100)

# Calcule o montante total
valor_juros = valor + juros

# Exiba o montante total e os juros
print(f'O montante total após {anos} anos é R$ {valor_juros:.2f}')
print(f'Os juros acumulados nesse período são R$ {juros:.2f}')