nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print ('Que nome bonito, eu também tenho um amigo com esse nome!')
elif nome in 'Pedro' 'Maria' 'Paulo' 'José':
    print( 'Seu nome é muito comum no meu pais! ')    
else:
    print ('Olha que legal, eu ainda não tenho amigos com esse nome!')

print ('Tenha um bom dia {}'.format(nome))