# Faça um programa que simule um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios,
# simulando os lançamentos dos dados.

from random import randint

def gerador_de_jogadas():
    lancamentos = []
    print('JOGADAS :')
    
    for i in range(1,101):
        c = randint(1, 6)

        print(f'{i}º jogada : {c}')

        lancamentos.append(c)


    print(f'''
O numero 1 apareceu {lancamentos.count(1)} vezes 
O numero 2 apareceu {lancamentos.count(2)} vezes 
O numero 3 apareceu {lancamentos.count(3)} vezes 
O numero 4 apareceu {lancamentos.count(4)} vezes 
O numero 5 apareceu {lancamentos.count(5)} vezes 
O numero 6 apareceu {lancamentos.count(6)} vezes 
''')
gerador_de_jogadas()

#comentário do Hélion
#este código está tão bem executado e escrito que aplicaria ele no lugar do meu
#a função está clara e a apresentação do código rodando muito bonita.
#entendi o código na primeira leitura
