casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
parcela = casa / (tempo * 12) #vezes 12 para poder converter ano em meses, pois salário é mensal
porcentagem = parcela / salario
if porcentagem <= 0.3:
    emprestimo = 'PODE SER CONCEDIDO'
else:  
    emprestimo = 'NEGADO!'

print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}, empréstimo {}'.format(casa, tempo, parcela, emprestimo))