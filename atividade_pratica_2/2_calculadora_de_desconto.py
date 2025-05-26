"""
2- Calculadora de Desconto Desenvolva um programa
que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% O programa deve calcular
o valor do desconto e o preço final, exibindo todos os detalhes.

"""

nomeProduto = "Camiseta"
precoOriginal = 50
desconto = 0.2

valorDesconto = precoOriginal * desconto
precoFinal = precoOriginal - valorDesconto

print(f"O produto {nomeProduto}, tem valor original de R$ {precoOriginal:.2f}. Com desconto de {desconto * 100}%, seu valor final é de R$ {precoFinal:.2f}")