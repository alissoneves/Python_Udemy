nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

print ('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media <= 5.0:
    
    print (f'Olá Aluno, sua média de notas foi de {media:.1f} e infelizmente você foi REPROVADO!')

elif media >= 5.1 and media <= 6.9:
    
    print (f'Olá Aluno, sua média de notas foi de {media:.1f} e infelizmente você está em RECUPERAÇÃO!')

elif media >= 7.0:
    
    print (f'Olá Aluno, sua média de notas foi de {media:.1f} e PARABÉNS, você foi APROVADO!')

else:

    print ('Não consegui compreender algumas das notas informadas, favor digitar novamente!')   