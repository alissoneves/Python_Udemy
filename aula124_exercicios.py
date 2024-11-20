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
    resposta_pessoa = input ('Digite sua resposta, baseado nas opções acima:')
  
    acertou = False
    resposta_pessoa_int = None
    qtd_opcoes = len(opcoes)
   

    if resposta_pessoa.isdigit():
        resposta_pessoa_int = int(resposta_pessoa)

        if resposta_pessoa_int is not None:    

            if resposta_pessoa_int >= 0 and resposta_pessoa_int < qtd_opcoes:
     
                if resposta_pessoa_int == pergunta['Resposta']:
                    acertou = True
                    print (f'Parabéns, a resposta correta é {pergunta['Resposta']}' 'você acertou sua respost!!')
                    qtd_acertos += 1
                else:
                    acertou = False
                    print ('Que pena, você errou a alternativa, tente novamente')

                    print('Você acertou', qtd_acertos)
                    print('de', len(perguntas), 'perguntas.')       