from datetime import date

ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
alistamento = 18 - idade
alistamento_faltante = ano_atual + alistamento

if idade < 18: 

    print (f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    print (f'Ainda faltam {alistamento} para o seu alistamento')
    print (f'Seu alistamento será em {alistamento_faltante}')

elif idade > 18:

    print (f'O seu tempo de alistamento já passou, obrigado!')
    print (f'Seu alistamento deveria ter sido em {alistamento_faltante}')

elif idade == 18:
    print (f'Você precisa se alistar IMEDIATAMENTE! ')

else: 
    print (f'Você não digitou uma data correta, favor verificar digitar novamente!')