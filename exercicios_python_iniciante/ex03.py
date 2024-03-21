"""
Crie um programa Python para calcular a área de um círculo com raio r.
"""

import math

# Solicite ao usuário que insira o valor do raio do círculo
r = float(input('Valor do Raio: '))

# Calcule a área do círculo
area = math.pi * (r**2)

# Exiba a área do círculo na tela
print(f'Área do círculo com raio {r} é {area:.2f}')