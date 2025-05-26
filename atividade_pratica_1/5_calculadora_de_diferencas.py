"""
5- Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B
pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros.
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""

valorA = int(input("Valor de A: "))
valorB = int(input("Valor de B: "))
valorC = int(input("Valor de C: "))
valorD = int(input("Valor de D: "))
diferenca = valorA * valorB - valorC * valorD

print(f"DIFERENCA = {diferenca}")