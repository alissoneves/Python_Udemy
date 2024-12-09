perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print ('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    resposta_pessoa = input ('Digite sua resposta, baseado nas opções acima: ')
  
    acertou = False
    resposta_pessoa_int = None
    qtd_opcoes = len(opcoes)
   
    if resposta_pessoa.isdigit():
        resposta_pessoa_int = int(resposta_pessoa)

    if resposta_pessoa_int is not None:    
        if resposta_pessoa_int >= 0 and resposta_pessoa_int < qtd_opcoes:
            if opcoes[resposta_pessoa_int] == pergunta['Resposta']:
                    acertou = True      
            print()

    if acertou:
        qtd_acertos += 1
        print (f'Parabéns, a resposta correta é {pergunta['Resposta']}' ' ,e você acertou sua resposta!!')    
        print()
    else:
         print ('Que pena, você errou a alternativa, tente novamente')
        

print (f'Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')
  