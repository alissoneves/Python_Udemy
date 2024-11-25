numero_escolhido = int(input('Digite um número inteiro:'))
conversor_escolhido = int(input(
    'Escolha uma das bases para conversão: \n'
    '[1] Converter para BINÁRIO\n'
    '[2] Converter para OCTAL\n'
    '[3] Converter para HEXADECIMAL\n'
    'Sua Opção: '))

if conversor_escolhido == 1: 
    binario = ""
    while numero_escolhido > 0:
        resto = numero_escolhido % 2
        binario = str(resto) + binario
        numero_escolhido //= 2

    print (f'{numero_escolhido} convertido para BINÁRIO é igual a {binario}')

elif conversor_escolhido == 2:

    octal = ""
    while numero_escolhido > 0:
        resto = numero_escolhido % 8
        octal = str(resto) + octal
        numero_escolhido //= 8
    print (f'{numero_escolhido} convertido para OCTAL é igual a {octal}')

else: 
    conversor_escolhido == 3

    hexa = ""
    while numero_escolhido > 0:
        resto = numero_escolhido % 16
    if resto < 10:
        hexa = str(resto) + hexa
    else:
        hexa = chr(55 + resto) + hexa  # Converte 10-15 em A-F
        numero_escolhido//= 16

    print (f'{numero_escolhido} convertido para OCTAL é igual a {hexa}') 