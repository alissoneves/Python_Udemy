"""
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
não permita que o programa quebra com erros de indices inexistestes na lista.

"""
import os

lista = []
while True:

    print ('Selecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [f]inalizar Compra: ')


    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append (valor)
    elif opcao == 'a':
        indice_str = input (
            'Escolha o índice para apagar:'
        )    

        try:
            indice = int(indice_str)
            del lista[indice]
        except: 
            print ('Não foi possível apagar esse índice, escolha outro!')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:

            print('Infelizmente a sua lista está vazia, inclua itens!')

        for i, valor in enumerate(lista):
            print (i,valor)

    elif opcao == 'f':
        os.system('cls')

        for valor in lista:
            print (lista)
        print ('Deseja finalizar sua compra? ')
        carrinho = input ('[S]im [N]ão: ')

        if carrinho == 's' and lista:
            os.system('cls')
            print ('Compra realizada com sucesso, volte sempre aos supermercados guanaraba')
            lista.clear ()

        elif carrinho == 's' and not lista:
            os.system('cls')
            print ('Você não pode fechar um carrinho sem ter itens dentro dele, favor inserir itens!')    

        if carrinho == 'n':
             os.system('cls')

    else: 
        print ('Escolha apenas as opções: I, A, L ou F para seguir com o processo de compra!')

              
