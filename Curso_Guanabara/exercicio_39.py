from datetime import date

ano_nascimento = int(input('Digite o ano que você nasceu: '))
genero = str(input('Digite o seu sexo: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
alistamento = 18 - idade
alistamento_faltante = ano_atual + alistamento

if idade < 18 and genero == 'Masculino': 

    print (f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
    print (f'Ainda faltam {alistamento} para o seu alistamento')
    print (f'Seu alistamento será em {alistamento_faltante}')

elif idade > 18 and genero == 'Masculino':

    print (f'O seu tempo de alistamento já passou, obrigado!')
    print (f'Seu alistamento deveria ter sido em {alistamento_faltante}')

elif idade == 18 and genero == 'Masculino':
    print (f'Você precisa se alistar IMEDIATAMENTE! ')

elif genero == 'Feminino':
    print (f'Não se preocupe, você é do sexo feminimo e não precisa se alistar! ')

else: 
    print (f'Você não digitou uma data correta, favor verificar digitar novamente!')