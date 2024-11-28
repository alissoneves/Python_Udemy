from datetime import date

ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento


if idade <= 9: 

    print (f'A sua idade é {idade}, portanto a sua categoria é MIRIM!')

elif idade > 9 and idade <= 14:

    print (f'A sua idade é {idade}, portanto a sua categoria é INFANTIL!')

elif idade > 15 and idade <= 19:

    print (f'A sua idade é {idade}, portanto a sua categoria é JUNIOR!')   

elif idade > 20 and idade <= 25:

    print (f'A sua idade é {idade}, portanto a sua categoria é SÊNIOR!') 

elif idade >= 26:
    print (f'A sua idade é {idade}, portanto a sua categoria é MASTER!')

else: 
    print (f'Você não digitou uma data correta, favor verificar digitar novamente!')