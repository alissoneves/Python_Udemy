# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')


if entrada == 'E' or entrada =='e':
    senha_digitada = input('Senha:')
    senha_permitida = '123456'
    
if entrada == 'E' or entrada == 'e' and senha_digitada  == senha_permitida:

    print('Bem vindo ao ambiente') 
    

if entrada == 'E' or entrada =='e' and senha_digitada != senha_permitida:

    print('Você não está permitido a entrar no sistema, verifique sua senha.')

if entrada == 'S'or entrada == 's':
        print('Volte sempre jogador!') 