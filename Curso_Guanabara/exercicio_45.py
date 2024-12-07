import os
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print ('Escolha uma opção: \n'
'[0] Pedra\n'
'[1] Papel\n'
'[2] Tesoura\n')

print ('-=' * 10)

jogador = int(input('Qual é a sua escolha? '))

print ('-=' * 10)

print(f'A opção escolhida por você foi {itens[jogador]}')

print ('JO ')
sleep (1.5)
print ('KEN ')
sleep (1.5)
print ('PO !!!!')
sleep (1.5)
print(f'A opção escolhida pelo computador foi {itens[computador]}\n')

print ('-=' * 10)

if computador == jogador: 
    print ('VOCÊS ESCOLHERAM O MESMO, JOGO EMPATADO!')


elif computador == 1 and jogador == 0:
    
    print ('COMPUTADOR GANHOU!')

elif computador == 0 and jogador == 1:
    
    print ('VOCÊ GANHOU!')

elif computador == 2 and jogador == 1:
    
    print ('COMPUTADOR GANHOU!')

elif computador == 1 and jogador == 2:
    
    print ('VOCÊ GANHOU!')

elif computador == 0 and jogador == 2:
    
    print ('COMPUTADOR GANHOU!')

elif computador == 2 and jogador == 0:
    
    print ('VOCÊ GANHOU!')

else: 

    print('Digite uma opção válida!')    