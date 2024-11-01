while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    operador = input ('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try: 
        num_1_float = float(num1)
        num_2_float = float(num2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None: 
        print('Um ou ambos os números digitados são inválidos.')        
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Inválidos.')        
        continue

    if len(operador) > 1:
        print ('Digite apenas um Operador')
        continue

    print ('Realizando sua conta. Configura o resultado abaixo:')    

    if operador == '+':
        
        print(f'{num_1_float} + {num_2_float} =',num_1_float + num_2_float)

    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)

    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)

    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)

    else:
        print('Nunca deveria chegar até esse ponto!')

    sair = input ('Quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break
