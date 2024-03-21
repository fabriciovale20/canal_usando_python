"""
Crie um programa para encontrar o maior valor entre três número em Python.
"""

# Entrada de dados
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

# Verificação qual é o maior valor entre os três números
if num1 > num2:
    if num1 > num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 > num3:
        maior = num2
    else:
        maior = num3

# Exibiação do maior valor
print(f'O maior número é o {maior}')