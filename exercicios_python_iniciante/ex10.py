"""
Identifique o erro no programa e corrija-o.

Qual é a saída esperada?

Resposta: A variável 'numero' está como tipagem STRING, dessa forma ocorre o erro.

### ERRADO ###
numero = input('Digite um número: ')

### CERTO ###
numero = float(input('Digite um número: '))
"""

# Solicita ao usuário para inserir um número
numero = float(input('Digite um número: '))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    resultado = 'par'
else:
    resultado = 'ímpar'

# Exibe o resultado
print(f'O número é: {resultado}')