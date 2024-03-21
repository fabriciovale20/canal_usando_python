"""
Crie um programa para imprimir n número pares.
"""

# Entrada de dados
numero = int(input('Digite um número: '))

# Contador de números pares
contador = 0

print('\nNúmero pares:')

# Laço de repetição FOR para identificar todos os números pares entre 0 e o número informado.
for c in range(numero+1):
    if c % 2 == 0:
        print(c)

        contador += 1

print(f'\n{contador} números pares.')
# Obs.: Zero é considerado número PAR