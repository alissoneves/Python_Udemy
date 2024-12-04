import os
preco_item = float(input('Digite o preço do seu produto:R$ '))
pagamento = int(input(
    'Escolha uma das formas de pagamento: \n'
    '[1] À Vista no Dinheiro/Cheque\n'
    '[2] À Vista no Cartão de Credito/Débito\n'
    '[3] Em até 2x no cartão \n'
    '[4] 3x ou mais no cartão\n'
    '[5] Cancelar Operação\n'
    'Sua Opção: '))

if pagamento == 1:
    
    desconto1 = preco_item * 0.1
    valor1 = preco_item - desconto1

    print ('Como você optou por pagar à vista no dinheiro ou cheque, você ganhou 10 % de desconto no preço total do produto.')
    print (f'Preço Normal é R${preco_item:.2f} com o desconto passou a ser de R${valor1:.2f}')
    print ('Obrigado por comprar conosco, e tenha uma excelente semana!')

elif pagamento == 2:

    desconto2 = preco_item * 0.05
    valor2 = preco_item - desconto2

    print ('Como você optou por pagar à vista no cartão, você ganhou 5 % de desconto no preço total do produto.')
    print (f'Preço Normal é R${preco_item:.2f} com o desconto passou a ser de R${valor2:.2f}')
    print ('Obrigado por comprar conosco, e tenha uma excelente semana!')

elif pagamento == 3:

    desconto3 = preco_item
    valor3 = desconto3

    print ('Como você optou por pagar em até 2x no cartão SEM JUROS, mas infelizmente você não ganhou desconto nessa compra.')
    print (f'O Preço se mantem e é de R${preco_item:.2f}.')
    print ('Obrigado por comprar conosco, e tenha uma excelente semana!')


elif pagamento == 4:

    acrescimo1 = preco_item * 0.2
    valor4 = preco_item + acrescimo1
    totparcela = int(input('Quantas parcelas você deseja? '))
    parcela = valor4 / totparcela

    print (f'Como você optou por pagar em {totparcela}x no cartão, infelizmente o seu produto ficara 20 % mais caro.')
    print (f'Preço Normal é R${preco_item:.2f} com o acrescimo passou a ser de R${valor4:.2f}')
    print (f'As parcelas serão de R${parcela:.2f} por um periodo de {totparcela} meses.')
    print ('Obrigado por comprar conosco, e tenha uma excelente semana!')    

elif pagamento == 5:

        print ('Ok, vamos te retonar ao menu principal!')

else: 
        print ('Você não digitou uma opção válida, favor verificar!')  
        os.system('cls')