"""
Crie um programa que executa o seguite:
• Peça a um usuário para isnerir um número.
• Se o número estiver entre 0 e 10, escreva a palavra azul.
• Se o número estiver entre 10 e 20, escreva a palavra vermelho.
• Se o número estiver entre 20 e 30, escreva a palavra verde.
• Se for qualquer outro número, escreva que não é uma opção de cor correta.
"""

# Entrada de dados
numero = int(input('Digite um número: '))

# Verificação qual a cor selecionada
if 0 < numero < 10:
    print('Azul')
elif 10 < numero < 20:
    print('Vermelho')
elif 20 < numero < 30:
    print('Verde')
else:
    print('Não é uma opção de cor correta.')