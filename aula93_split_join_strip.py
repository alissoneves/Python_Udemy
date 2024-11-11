"""
* split e join com list e str
* split - divide uma string
* strip, lstrip, rstrip - Remove o espaço dentro de uma variavel, 
l na esquerda e r na direita
* join - une uma string
"""

frase = 'Olha essa, frase aqui'
listas_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(listas_frases_cruas):
     lista_frases.append(listas_frases_cruas[i].strip())       

print(listas_frases_cruas)
print(lista_frases)

frases_unidas = ', '.join (lista_frases)
print (frases_unidas)