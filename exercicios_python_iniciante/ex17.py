"""
Cire um programa para verificar se determinado número é +ve, -ve ou zero.
"""

# Entrada de dados
numero = float(input('Digite um número: '))

# Verificação se o número é positivo, negativo ou zero
if numero > 0:
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')