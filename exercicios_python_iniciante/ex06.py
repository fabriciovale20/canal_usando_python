"""
Crie um programa em Python que calcula o custo total e o troco, de itens comprados.
"""

# Valor da unidade do produto
preco_por_und = float(input('Valor da unidade do produto: R$ '))

# Quantidade de produtos
qnt_produtos = int(input('Quantidade de produtos: '))

# Valor a se pago
valor_pago = float(input('Informe quanto o valor pago: R$ '))

# Cálculo o custo total
custo_total = preco_por_und * qnt_produtos

# Cálculo do troco
troco = valor_pago - custo_total

# Exibição da quantidade de itens comprados, custo total e o troco
print(f'Quantidade de itens comprados: {qnt_produtos}')
print(f'Custo total dos itens R$ {custo_total:.2f}')
print(f'Troco R$ {troco:.2f}')
