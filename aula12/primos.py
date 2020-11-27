# Faça um programa que gera uma lista dos números primos existentes entre 1 e
# um número inteiro informado pelo usuário.


def mostrarPrimos():
   
    numerofinal = int(input("Verificar números primos de 1 até: "))

    lista_de_primos = []

    for i in range(2,numerofinal+1):
        cont = 0
        for x in range(1, i+1):
            if i%x == 0:
                cont +=1
        if cont <=2:
            lista_de_primos.append(i)
    
    print(f'''Os números primos de 1 até {numerofinal} são:
{lista_de_primos}''')

mostrarPrimos()