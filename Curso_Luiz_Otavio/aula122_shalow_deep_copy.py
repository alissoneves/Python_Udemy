
# copy - retorna uma cópia rasa (shallow copy)
#utilizando .copy apenas trata-se de uma copia rasa
#pode notar que a lista l1 foi alterada para 99999 no indice 1
# e isso afetou não só a d2 mas também o dicionario d1.
# isso não iria acontecer se fosse utilizado um d1.deepcopy()

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()
#d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)