nome = input ('Digite seu nome: ')
contagem_nome = len(nome)

if contagem_nome > 2:

    if contagem_nome >= 0 and contagem_nome <= 4: 
     
        print (f'Bom dia {nome}, o seu nome é curto!')

    elif contagem_nome >= 5 and contagem_nome <=6: 
     
        print (f'Boa tarde {nome}, o seu nome é normal!')

    elif contagem_nome >= 6:
     
        print (f'Boa tarde {nome}, o seu nome é grande!')

else: 

    print ('Digite seu nome, infelizmente não entendi!')        