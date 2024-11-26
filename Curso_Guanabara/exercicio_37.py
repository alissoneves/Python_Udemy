numero_escolhido = int(input('Digite um número inteiro:'))
conversor_escolhido = int(input(
    'Escolha uma das bases para conversão: \n'
    '[1] Converter para BINÁRIO\n'
    '[2] Converter para OCTAL\n'
    '[3] Converter para HEXADECIMAL\n'
    'Sua Opção: '))

if conversor_escolhido == 1: 

    print (f'{numero_escolhido} convertido para BINÁRIO é igual a {bin(numero_escolhido)[2:]}')

elif conversor_escolhido == 2:

    print (f'{numero_escolhido} convertido para OCTAL é igual a {oct(numero_escolhido)[2:]}')

elif conversor_escolhido == 3:

    print (f'{numero_escolhido} convertido para OCTAL é igual a {hex(numero_escolhido)[2:]}') 

else: 
    print ('Você não digitou nenhuma opção válida, favor tentar novamente!')    