nome = input ('Digite seu nome: ')
hora = input ('Digite sua hora local: ')

try:

    hora = int(hora)

    if hora >= 0 and hora <= 11: 
     
        print (f'Bom dia {nome}, seja bem vindo a nossa loja!')

    elif hora >= 12 and hora <=17: 
     
        print (f'Boa tarde {nome}, seja bem vindo a nossa loja!')

    elif hora >= 18 and hora <=23: 
        print (f'Boa noite {nome}, seja bem vindo a nossa loja!')

    else: 
        print ('Essa hora não existe, favor validar novamente')

except:
    print ('Você não digitou sua hora')