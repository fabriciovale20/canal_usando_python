"""
Identifique o erro no programa e corrija-o.

Qual é a saída esperada?

Resposta: O erro estava no PRINT, pois estava faltando o fechamento das aspas.

### ERRADO ###
print(f'O número de caracteres é: {contagem})

### CORRETO ###
print(f'O número de caracteres é: {contagem}')
"""

# Solicita ao usuário para inserir uma string
texto = input('Digite uma string: ')

# Conta o número de caracteres
contagem = len(texto)

# Exibe a contagem de caracteres
print(f'O número de caracteres é: {contagem}')