# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões,
#     de forma que o desperdício de tinta seja menor.
#     Acrescente 10% de folga e sempre arredonde os valores para cima,
#     isto é, considere latas cheias.

def tinta():
    metros = float(input(f"Digite o tamanho da área em m² a ser pintada : "))
    resultado = (metros / 6)
    resultado += resultado * 0.1
    resultado = round(resultado)
    lata = resultado // 18
    n = resultado - lata * 18
    galao = n // 3.6

    if resultado >= 18:
        print(f'Você precisará de {lata} lata(s) de 18L e {galao} galão(ões) de 3,6L')
    else:
        print(f'Você precisara de {galao} galão(ões) de 3,6L')

tinta()
