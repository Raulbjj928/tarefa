# Faça um programa que gera uma lista dos números primos existentes entre 1 e
# um número inteiro informado pelo usuário.


def mostrarPrimos():
   
    numerofinal = int(input("Digite um numero inteiro: "))

    lista_de_primos = []

    for i in range(2,numerofinal+1):
        cont = 0
        for x in range(1, i+1):
            if i%x == 0:
                cont +=1
        if cont <=2:
            lista_de_primos.append(i)
    
    print(f'''De 1 até {numerofinal} os numeros primos são:
{lista_de_primos}''')

mostrarPrimos()