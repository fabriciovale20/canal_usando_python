"""
Crie um programa Python para Trocar Dois Números sem usar Variável Temporária
"""

# Entrada de dados
num1 = int(input('Informe o valor de num1: '))
num2 = int(input('Informe o valor de num2: '))

# Troca dos números usando
num1, num2 = num2, num1

# Exibição do resultado
print('Depois da troca:')
print(f'num1 = {num1}')
print(f'num2 = {num2}')


### ABAIXO A FORMA REALIZADA PELO CANAL ###
# Trocar dois números sem variável temporária
a = 5
b = 8

print('Antes da troca:')
print(f'a = {a}')
print(f'b = {b}')

a = a + b
b = a - b
a = a - b

print('\nDepois da troca:')
print(f'a = {a}')
print(f'b = {b}')