"""
Crie um programa para verificar se o número é positivo ou negativo.
"""

# Entrada de dados
numero = float(input('Informe um número: '))

# Verificação se o número é positivo, negativo ou zero.
if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')