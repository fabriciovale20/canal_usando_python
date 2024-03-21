"""
Identifique o erro no programa e corrija-o.

Qual é a saída esperada?

Resposta: A variávels 'numero' não estava com tipagem, dessa forma, estava amazenando o valor como STRING.

### ERRADO ###
numero = input('Digite um número: ')

### CORRETO ###
numero = float(input('Digite um número: '))
"""

# Solicita ao usuário para inserir um número
numero = float(input('Digite um número: '))

# Calcula a raiz quadrada
raiz = numero ** 0.5

# Exibe a raiz quadrada
print(f'A raiz quadrada é: {raiz}')