"""

2- Classificador de Idade

Crie um programa que solicite a idade do usuário
e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

"""

idade = int(input("informe sua idade: "))

if idade > 0 and idade < 13:
    print("voce é uma Criança")
elif idade > 12 and idade < 18:
    print("voce é um Adolescente")
elif idade > 17 and idade < 60:
    print("voce é um Adulto")
else:
    print("voce é um Idoso")