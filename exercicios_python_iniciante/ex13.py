"""
Crie um programa para encontrar o maior número entre dois números.
"""

# Entrada de dados
num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

# Verificação e encontro do maior número
if num1 > num2:
    maior = num1
else:
    maior = num2

print(f'O maior número é: {maior}')