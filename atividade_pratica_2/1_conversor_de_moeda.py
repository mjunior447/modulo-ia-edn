"""
1- Conversor de Moeda Crie um programa que converte
um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.20
Taxa do euro: R$ 6.15 O programa deve calcular e exibir
os valores convertidos, arredondando para duas casas decimais.

"""

valorReais = 100
taxaDolar = 5.20
taxaEuro = 6.15

valorDolar = 100 / 5.20
valorEuro = 100 / 6.15

print(f"100 reais em dolar: {valorDolar:.2f} dolares")
print(f"100 reais em euro: {valorEuro:.2f} euros")