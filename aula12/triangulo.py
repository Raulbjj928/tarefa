# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

def triangulo():
    A = float(input('Digite a primeira medida : '))
    B = float(input('Digite a segunda medida : '))
    C = float(input('Digite a terceira medida : '))
    if (A + B) > C and (A + C) > B and (B + C) > A:
        if ((A == B)  and A != C) or ((C == B)  and C != A):
            print('É um triangulo Isóceles.')
        elif A == B and B == C :
            print('É um triangulo Equilátero.')
        elif A != B and C != B and A != C :
            print('É um triangulo Escaleno.')
    else:
        print('Não é um triângulo !')
triangulo()