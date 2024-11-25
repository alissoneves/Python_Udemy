valor_casa = float(input('Favor informar o valor da casa desejada: R$ '))
salario = float(input ('Favor informe o seu salário liquido: R$ '))
anos = int(input ('Você quer pagar a casa em quantos anos? '))


calculo_prestacao = valor_casa / (anos * 12)
percentual_salario = salario * 0.3

print ('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print (' a prestação será de R${:.2f}'.format(calculo_prestacao))
print ('A título de informação, você precisa pagar {:.2f} e a sua parcela máxima tem que ser: R${:.2f}'.format (calculo_prestacao, percentual_salario))

if calculo_prestacao <= percentual_salario:
    print ('Você está apto para efetuar esse financiamento, consulte o banco mais próximo!')
else:
    print ('Infelizmente o seu salario não se enquadra dentro das políticas de financiamento.')    
