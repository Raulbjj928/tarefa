# Conta espaços e vogais. 
# Dado uma string com uma frase informada pelo usuário 
# (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 

def conta_espacos_vogais():
    f = input('Digte uma frase : ').upper()
    v = 0
    e = 0 
    for caractere in f :
        if caractere == ' ':
            e = e + 1
        elif caractere in 'AEIOU':
            v = v + 1
    print (f'Nesta frase existe {e} espaços e {v} vogais.')
conta_espacos_vogais()


#comentário do Hélion:
#o codigo está super limpo, organizado. Eu entendi ele na primeira leitura. As variáveis com a primeira letra
#do que ela representa também deixa fácil e o código claro. 