"""
Crie um programa Python para Converter temperatura de Fahrenheit para Celsius.
"""

# Solkicite ao usuário que insira a temperatura em graus Fahrenheit
fahrenheit = float(input('Temperatura em Fahrenheit: '))

# Converta a temperatura de Fahrenheit para Celsius
celsius = 5/9 * (fahrenheit - 32)

# Exiba a temperatura em graus Celsius na tela
print(f'A temperatura em Celsius é: {celsius:.2f} graus Celsius')