"""
Identifique o erro no programa e corrija-o. Além disso, demostre a saída esperada quando o programa estiver corrigido

Resposta: O erro estava nas variáveis, pois não estavam com a tipagem de FLOAT, dessa forma, as variáveis estavam armazenando os valores como STRING.
Realizado ajuste e o programa funcionou normalmente.

### ERRADO ###
numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')
numero3 = input('Digite o terceiro número: ')

### CORRETO ###
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
"""

# Solicita ao usuário para inserir três números
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

# Calcula a média dos três números
media = (numero1 + numero2 + numero3) / 3

# Exibe a média
print(f'A média é: {media:.2f}')
