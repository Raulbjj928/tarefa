# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$



def salario():
    valor_hora = float(input('Digite o valor ganho por hora trabalhada : '))
    horas_mes = int(input('Digite a quantidade de horas tabalhadas no mês : '))
    saldo_bruto = horas_mes * valor_hora
    ir = (saldo_bruto * 0.11)
    inss = (saldo_bruto * 0.08)
    sindicato = (saldo_bruto * 0.05)
    liquido = saldo_bruto - (ir + inss + sindicato)

    print(f'''
{35 * '='}
SALÁRIO BRUTO :R$ {saldo_bruto:.2f} 
{35 * '='}
        DESCONTOS
IR : R$ {ir:.2f} (11%)
INSS : R$ {inss:.2f} (8%)
SINDICATO : R$ {sindicato:.2f} (5%)
{35 * '='}
SALÁRIO LÍQUIDO : R$ {liquido:.2f}
{35 * '='}

''')
salario()

#comentário do Hélion
#fácil entendimento, as variáveis com nomes fáceis.
#a impressão ficou muito bonita, Raul tem mão pra frontend também
#*uma vez vi num vídeo que dizem pra deixar duas linhas em branco depois do def, porque alguns idle as
#vezes dão erro, mas não sei se é verdade, se for é a única coisinha