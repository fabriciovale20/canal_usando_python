"""
Crie um programa para determinar se um aluno passou no exame ou não.
"""

# Entrada de dados
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação se o aluno passou ou não
nota_aprovacao = 60 # Definindo a nota mínima para aprovação

if media > nota_aprovacao:
    print(f'O aluno passou no exame! Média: {media:.2f}')
else:
    print(f'O aluno não passou no exame. Média: {media:.2f}')