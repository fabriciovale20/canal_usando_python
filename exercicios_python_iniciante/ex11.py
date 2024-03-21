"""
Crie um programa para Trpcar Dois Números usando uma Variável Temporária.
"""

# Entrada de dados
num1 = int(input('Informe o valor de num1: '))
num2 = int(input('Informe o valor de num2: '))

# Troca dos números usando uma variável temporária
temp = num1
num1 = num2
num2 = temp

# Exibição do resultado
print('Depois da troca:')
print(f'num1 = {num1}')
print(f'num2 = {num2}')