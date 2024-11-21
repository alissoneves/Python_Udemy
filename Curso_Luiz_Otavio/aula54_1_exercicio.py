num1 = input ('Digite um número: ')

if num1.isdigit():
    num1_int = int(num1)
    par_impar = num1_int % 2 == 0
    par_impar_texto = 'Ímpar'

    if par_impar: 
        par_impar_texto = 'par'

    print (f'O número {num1_int} é {par_impar_texto}')

else:
    print ('Você não digitou um numero inteiro')


    